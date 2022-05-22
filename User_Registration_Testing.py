'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-22 21:11:20
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-22 21:33:14
    @Title : User Registration Testing 
'''
import unittest
import User_Registration

class TestArithmeticOperation(unittest.TestCase):

    def test_firstname(self):
        """ 
            Description: 
                This function is testing user's first name 
            Parameter:
                self as argument
            Return:
                None
        """
        self.assertEqual(User_Registration.first_name("Madhavee"),True)
        self.assertEqual(User_Registration.first_name("madhavee"),False)
        self.assertEqual(User_Registration.first_name("Ma"),False)
        self.assertEqual(User_Registration.first_name("ma"),False)
        self.assertEqual(User_Registration.first_name("MADHAVEE"),False)
        
    def test_lastname(self):
        """ 
            Description: 
                This function is testing user's last name 
            Parameter:
                self as argument
            Return:
                None
        """
        self.assertEqual(User_Registration.last_name("Kadivar"),True)
        self.assertEqual(User_Registration.last_name("kadivar"),False)
        self.assertEqual(User_Registration.last_name("Km"),False)
        self.assertEqual(User_Registration.last_name("mk"),False)
        self.assertEqual(User_Registration.last_name("KADIVAR"),False)
        
    def test_email(self):
        """ 
            Description: 
                This function is testing user's email
            Parameter:
                self as argument
            Return:
                None
        """
        self.assertEqual(User_Registration.email_check("abc@gmail.com"),True)
        self.assertEqual(User_Registration.email_check("abc.com.in"),False)
        
if __name__ == "__main__":
    unittest.main()