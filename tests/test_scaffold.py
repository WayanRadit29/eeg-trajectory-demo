import unittest
from contextlib import redirect_stdout
from importlib import import_module
from io import StringIO

from trajdemo.app import main


class ScaffoldTests(unittest.TestCase):
    def test_subpackages_are_importable(self) -> None:
        for name in ("bundle", "inference", "playback", "scene", "ui"):
            with self.subTest(name=name):
                import_module(f"trajdemo.{name}")

    def test_placeholder_entry_point(self) -> None:
        output = StringIO()
        with redirect_stdout(output):
            main()

        self.assertEqual(output.getvalue(), "EEG Trajectory Demo: Phase 0 scaffold\n")
