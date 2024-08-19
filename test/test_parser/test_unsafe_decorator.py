import tempfile
import unittest
from pathlib import Path
from apps.uniq import Uniq
from unsafe_decorator import UnsafeDecorator
from application_factory import ApplicationFactory


class TestUnsafe(unittest.TestCase):
    def setup(self, contents):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        self.test_file = []
        for i in range(len(contents)):
            self.test_file.append(str(self.temp_path) + f"/test-{i}.txt")
            with open(self.test_file[i], "w") as f:
                f.write(contents[i])
        return []

    def teardown(self):
        self.test_dir.cleanup()

    def test_unsafe_uniq(self):
        out = self.setup(["AAA\nAAA\nBBB\nBBB\nCCC\nCCC\n"])
        expected_output = "AAA\nBBB\nCCC\n"
        UnsafeDecorator(Uniq()).execute([self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_unsafe_uniq_throw(self):
        out = self.setup(["AAA\nAAA\nBBB\nBBB\nCCC\nCCC\n"])
        expected_output = (
            "An exception occurred: Wrong flags [uniq -i <file>?]\n"
        )
        UnsafeDecorator(Uniq()).execute(["-c", self.test_file[0]], out)
        self.assertEqual(
            expected_output,
            "".join(out),
        )
        self.teardown()

    def test_safe_application(self):
        self.setup([])
        appfactory = ApplicationFactory(unsafe=False)
        self.assertFalse(isinstance(appfactory.application_map["uniq"], Uniq))
        self.teardown()

    def test_unsafe_application(self):
        self.setup([])
        appfactory = ApplicationFactory(unsafe=True)
        self.assertTrue(
            isinstance(appfactory.application_map["_uniq"], UnsafeDecorator)
        )
        self.teardown()
