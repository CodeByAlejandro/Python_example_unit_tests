import unittest
import main


class TestSuccesfulGuess(unittest.TestCase):

    def setUp(self):
        print("\npre-test initialization")


    def test_succesful_guess(self):
        print("running test : test_succesful_guess")
        result = main.chk_succesful_guess(5, 5)
        self.assertTrue(result)


    def test_wrongh_guess(self):
        print("running test : test_wrongh_guess")
        result = main.chk_succesful_guess(3, 5)
        self.assertFalse(result)


    def test_out_of_range_lower_bound_guess(self):
        print("running test : test_out_of_range_lower_bound_guess")
        self.assertRaisesRegex(
            ValueError, 'Got value out of range',
            main.chk_succesful_guess, 0, 5
        )


    def test_out_of_range_upper_bound_guess(self):
        print("running test : test_out_of_range_upper_bound_guess")
        self.assertRaisesRegex(
            ValueError, 'Got value out of range',
            main.chk_succesful_guess, 11, 5
        )


    def test_string_value_guess(self):
        print("running test : test_string_value_guess")
        self.assertRaises(ValueError, main.chk_succesful_guess, 'dkjfalk', 5)


    def test_bool_value_guess(self):
        print("running test : test_bool_value_guess")
        self.assertRaisesRegex(
            TypeError, 'Got boolean, expected int',
            main.chk_succesful_guess, True, 5
        )


    def test_none_value_guess(self):
        print("running test : test_none_value_guess")
        self.assertRaises(TypeError, main.chk_succesful_guess, None, 5)


    def tearDown(self):
        print("post-test cleanup")


if __name__ == '__main__':
    unittest.main()
