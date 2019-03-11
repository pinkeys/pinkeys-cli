""" Unit Testd """
import unittest
import pinkeys


class UserTestCase(unittest.TestCase):
    """ Unit test to validate CLI """
    def test_with_empty_args(self):
        """ User passes no args, should fail with SystemExit"""
        output = pinkeys.main(user='test')
        print("TEXT" + str(output))
        self.assertIsNotNone(output)
        self.assertEqual(output['name'], 'testSSH')

    def test_with_empty_args_bad_user(self):
        """ User passes an invalid user, should fail with SystemExit"""
        self.assertIsNone(pinkeys.main(user='invaliduser'), '')

    # def test_without_file(self):
    #     self.fail('not implemented')

    # def test_with_file(self):
    #     self.fail('not implemented')

    # def test_output_txt_format_on_screen(self):
    #     self.fail('not implemented')

    # def test_output_json_format_on_screen(self):
    #     self.fail('not implemented')

    # def test_output_txt_format_on_file(self):
    #     self.fail('not implemented')

    # def test_output_json_format_on_file(self):
    #     self.fail('not implemented')

    # def test_pgp_type_on_screen(self):
    #     self.fail('not implemented')

    # def test_ssh_type_on_file(self):
    #     self.fail('not implemented')

    # def test_api_lockout_message(self):
    #     self.fail('not implemented')


def main():
    """ Main function """
    unittest.main()

if __name__ == '__main__':
    main()
