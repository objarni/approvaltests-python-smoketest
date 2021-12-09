import unittest
from approvaltests import verify

class SmokeTest(unittest.TestCase):
  def test_hello_world(self):
    verify("hello world")

unittest.main()
