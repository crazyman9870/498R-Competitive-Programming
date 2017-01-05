import unittest
# This is another way of importing a package. You can rename the imported
#    package. This is useful when you want to try out different libraries
#    with identical api's. (ie. json and simplejson)
import examplemodule.hello as hello


class TestingTest (unittest.TestCase):
    """Example UnitTest class
    """

    def test_hello_world(self):
        """Basic test for verifying that our local module works
        """

        self.assertEquals(
            hello.hello_world(), "Hello World")


if __name__ == '__main__':
    unittest.main()
# run with python test.py
