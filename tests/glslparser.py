"""A profile that runs only GLSLParserTest instances."""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from framework.test import GLSLParserTest
from tests.all import profile

__all__ = ['profile']

profile.filter_tests(lambda _, t: isinstance(t, GLSLParserTest))
