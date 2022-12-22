from unittest import TestCase

from app.domain.adapters.base import BaseAdapter


class TestBaseAdapter(TestCase):
    def test_base_adapter__logs_and_throws(self):

        with self.assertRaises(TypeError) as exception_context:
            BaseAdapter()  # pyright: ignore (reportGeneralTypeIssues)

        self.assertEqual(
            str(exception_context.exception),
            "Can't instantiate abstract class BaseAdapter "
            + "with abstract methods get, post",
        )
