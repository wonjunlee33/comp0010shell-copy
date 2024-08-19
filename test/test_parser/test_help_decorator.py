import unittest
from help_decorator import HelpDecorator
from apps.uniq import Uniq
from application_factory import ApplicationFactory


class TestApplicationFactory(unittest.TestCase):
    def test_helper_uniq(self):
        out = []
        expected_output = Uniq().__doc__ + "\n"
        HelpDecorator(Uniq()).execute(["-h"], out)
        self.assertEqual(
            expected_output,
            "".join(out),
        )

    def test_helpful_application(self):
        appfactory = ApplicationFactory(helpful=False)
        self.assertFalse(
            isinstance(appfactory.application_map["uniq"], HelpDecorator)
        )
