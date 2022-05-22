'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-22 21:11:20
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-22 22:55:24
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
        
    def test_mobile_number(self):
        """ 
            Description: 
                This function is testing user's mobile number
            Parameter:
                self as argument
            Return:
                None
        """
        self.assertEqual(User_Registration.mobile_number_check("91 9615145122"),True)
        self.assertEqual(User_Registration.mobile_number_check("919635245125"),False)
        self.assertEqual(User_Registration.mobile_number_check("9856235648"),False)
        self.assertEqual(User_Registration.mobile_number_check("91 1258521452"),False)
        self.assertEqual(User_Registration.mobile_number_check("91 89561285"),False)

    def test_password_rule_1(self):
        """ 
            Description: 
                This function is testing user's password for rule 1
            Parameter:
                self as argument
            Return:
                None
        """
        self.assertEqual(User_Registration.password_rule_1_check("sadfg85sdfg"),True)
        self.assertEqual(User_Registration.password_rule_1_check("sdswdf"),False)
        self.assertEqual(User_Registration.password_rule_1_check("ADFfvc865"),True)

    def test_password_rule_2(self):
        """ 
            Description: 
                This function is testing user's password for rule 2
            Parameter:
                self as argument
            Return:
                None
        """
        self.assertEqual(User_Registration.password_rule_2_check("Awdfergt85846"),True)
        self.assertEqual(User_Registration.password_rule_2_check("sdswdf85"),False)
        self.assertEqual(User_Registration.password_rule_2_check("Adsf69"),False)

    def test_password_rule_3(self):
        """ 
            Description: 
                This function is testing user's password for rule 3
            Parameter:
                self as argument
            Return:
                None
        """
        self.assertEqual(User_Registration.password_rule_3_check("Awdfergt8"),True)
        self.assertEqual(User_Registration.password_rule_3_check("A56235623"),True)
        self.assertEqual(User_Registration.password_rule_3_check("Adsf69"),False)

    def test_password_rule_4(self):
        """ 
            Description: 
                This function is testing user's password for rule 4
            Parameter:
                self as argument
            Return:
                None
        """
        self.assertEqual(User_Registration.password_rule_4_check("dfgDnjvbn"),False)
        self.assertEqual(User_Registration.password_rule_4_check("A5sdf@df"),True)
        self.assertEqual(User_Registration.password_rule_4_check("F5G@f"),False)
        self.assertEqual(User_Registration.password_rule_4_check("85ADcv*gj5"),True)
        self.assertEqual(User_Registration.password_rule_4_check("*&&d*fgADDd845"),False)
        self.assertEqual(User_Registration.password_rule_4_check("885@dfvvvb"),False)
        
if __name__ == "__main__":
    unittest.main()