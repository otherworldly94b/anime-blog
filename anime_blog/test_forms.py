from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    """
    Unit tests for the CommentForm class.
    """

    def test_form_is_valid(self):
        """
        Test that a form with a body is valid.
        """
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self):
        """
        Test that a form with an empty body is invalid.
        """
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg='Form is valid')
