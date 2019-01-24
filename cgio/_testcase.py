import sys
import unittest
from unittest.mock import patch
from contextlib import contextmanager
from io import StringIO


class TestCase(unittest.TestCase):
    @contextmanager
    def assertOutput(self, expected, *, argv=["-"], strip_trailing=True):
        fake_stdout = StringIO()
        with patch.object(sys, "argv", argv):
            with patch.object(sys, "stdout", fake_stdout):
                yield fake_stdout
        output = fake_stdout.getvalue()
        if strip_trailing:
            output_lines = [line.rstrip() for line in output.rstrip().splitlines()]
        else:
            output_lines = output.splitlines()
        self.assertEqual(output_lines, expected.splitlines())

    def assertQuine(self, src):
        with self.assertOutput(src, strip_trailing=False):
            exec(src)
