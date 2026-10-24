"""Exercise the real installer without touching personal Claude Code settings."""

import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class DistributionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="fable install ")
        self.addCleanup(self.temp.cleanup)
        self.workspace = Path(self.temp.name)
        self.checkout = self.workspace / "checkout with spaces"
        self.checkout.mkdir()
        shutil.copy2(ROOT / "install.sh", self.checkout)
        shutil.copytree(ROOT / "skills", self.checkout / "skills")
        self.config = self.workspace / "new config"

    def install(self):
        return subprocess.run(
            ["bash", str(self.checkout / "install.sh")],
            cwd=self.workspace,
            env={**os.environ, "CLAUDE_CONFIG_DIR": str(self.config)},
            capture_output=True,
            text=True,
            check=False,
        )

    def assert_success(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_fresh_install_copies_every_skill_and_reference(self):
        result = self.install()
        self.assert_success(result)
        source = self.checkout / "skills"
        destination = self.config / "skills"
        files = {p.relative_to(source) for p in source.rglob("*") if p.is_file()}
        installed = {
            p.relative_to(destination)
            for p in destination.rglob("*")
            if p.is_file()
        }
        self.assertEqual(installed, files)
        self.assertTrue((destination / "fable-plan-mode" / "SKILL.md").is_file())
        for path in files:
            with self.subTest(path=path):
                self.assertEqual(
                    (destination / path).read_bytes(), (source / path).read_bytes()
                )

    def test_reinstall_updates_managed_files_and_preserves_other_content(self):
        self.assert_success(self.install())
        skills = self.config / "skills"
        unrelated = skills / "personal-skill"
        unrelated.mkdir()
        (unrelated / "SKILL.md").write_text("Personal skill\n", encoding="utf-8")
        extra = skills / "fable-core" / "personal-notes.md"
        extra.write_text("Keep this\n", encoding="utf-8")
        installed = skills / "fable-core" / "SKILL.md"
        installed.write_text("Old version\n", encoding="utf-8")
        self.assert_success(self.install())
        self.assertEqual(
            installed.read_bytes(),
            (self.checkout / "skills/fable-core/SKILL.md").read_bytes(),
        )
        self.assertEqual(extra.read_text(encoding="utf-8"), "Keep this\n")
        self.assertEqual(
            (unrelated / "SKILL.md").read_text(encoding="utf-8"), "Personal skill\n"
        )
        self.assertFalse((skills / "fable-core" / "fable-core").exists())

    def test_missing_skill_fails_before_creating_destination(self):
        shutil.rmtree(self.checkout / "skills/fable-plan-mode")
        result = self.install()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("fable-plan-mode/SKILL.md", result.stderr)
        self.assertFalse(self.config.exists())

    def test_missing_entrypoint_leaves_existing_install_untouched(self):
        self.assert_success(self.install())
        installed = self.config / "skills/fable-core/SKILL.md"
        installed.write_text("Local edit\n", encoding="utf-8")
        (self.checkout / "skills/fable-skill-refactorer/SKILL.md").unlink()
        result = self.install()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("fable-skill-refactorer/SKILL.md", result.stderr)
        self.assertEqual(installed.read_text(encoding="utf-8"), "Local edit\n")

    def test_destination_error_does_not_report_success(self):
        self.config.write_text("Not a directory\n", encoding="utf-8")
        result = self.install()
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("Done.", result.stdout)

    def test_readme_inventory_matches_installable_skills(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        advertised = set(re.findall(r"^\| `(fable-[a-z-]+)` \|", readme, re.M))
        skills = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
        self.assertEqual(skills, advertised)
        count = re.search(r"## Skills \((\d+) total\)", readme)
        self.assertIsNotNone(count)
        self.assertEqual(int(count.group(1)), len(skills))
        for name in skills:
            entrypoint = (ROOT / "skills" / name / "SKILL.md").read_text(
                encoding="utf-8"
            )
            self.assertRegex(entrypoint, rf"(?m)^name: {re.escape(name)}$")

    def test_supporting_documents_are_reachable_within_each_skill(self):
        for skill in (ROOT / "skills").iterdir():
            if not skill.is_dir():
                continue
            visited = set()
            pending = [skill / "SKILL.md"]
            while pending:
                document = pending.pop().resolve()
                if document in visited:
                    continue
                visited.add(document)
                for link in re.findall(
                    r"\[[^\]]+\]\(([^)]+\.md)\)", document.read_text(encoding="utf-8")
                ):
                    if "://" in link:
                        continue
                    target = (document.parent / link).resolve()
                    with self.subTest(document=document, link=link):
                        self.assertTrue(target.is_relative_to(skill.resolve()))
                        self.assertTrue(target.is_file(), f"Missing reference: {target}")
                    pending.append(target)
            self.assertEqual(visited, {p.resolve() for p in skill.rglob("*.md")})


if __name__ == "__main__":
    unittest.main()
