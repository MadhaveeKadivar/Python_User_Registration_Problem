'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-22 23:05:29
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-22 23:05:57
    @Title : Email samples Testing 
'''
import unittest
import User_Registration

class TestArithmeticOperation(unittest.TestCase):
    def test_email(self):
        """ 
            Description: 
                This function is testing user's email
            Parameter:
                self as argument
            Return:
                None
        """
        # Valid Emails Testing
        self.assertEqual(User_Registration.email_check("abc@yahoo.com"),True)
        self.assertEqual(User_Registration.email_check("abc-100@yahoo.com"),True)
        self.assertEqual(User_Registration.email_check("abc.100@yahoo.comm"),True)
        self.assertEqual(User_Registration.email_check("abc111@abc.com"),True)
        self.assertEqual(User_Registration.email_check("abc-100@abc.net"),True)
        self.assertEqual(User_Registration.email_check("abc.100@abc.com.au"),True)
        self.assertEqual(User_Registration.email_check("abc@1.com"),True)
        self.assertEqual(User_Registration.email_check("abc@gmail.com.com"),True)
        self.assertEqual(User_Registration.email_check("abc+100@gmail.com"),True)

        # Invalid Email Testing
        self.assertEqual(User_Registration.email_check("abc@.com.my"),False)
        self.assertEqual(User_Registration.email_check("abc123@gmail.a"),False)
        self.assertEqual(User_Registration.email_check("abc123@.com"),False)
        self.assertEqual(User_Registration.email_check("abc123@.com.com"),False)
        self.assertEqual(User_Registration.email_check(".abc@abc.com"),False)
        self.assertEqual(User_Registration.email_check("abc()*@gmail.com"),False)
        self.assertEqual(User_Registration.email_check("abc..2002@gmail.com"),False)
        self.assertEqual(User_Registration.email_check("abc.@gmail.com"),False)
        self.assertEqual(User_Registration.email_check("abc@gmail.com.1a"),False)
        self.assertEqual(User_Registration.email_check("abc@abc@gmail.com"),False)
        self.assertEqual(User_Registration.email_check("abc@%*.com"),False)
        self.assertEqual(User_Registration.email_check("abc"),False)
        self.assertEqual(User_Registration.email_check("abc@gmail.com.aa.au"),False)


if __name__ == "__main__":
    unittest.main()
