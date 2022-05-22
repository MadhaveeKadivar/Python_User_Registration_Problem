'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-22 21:11:20
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-22 21:11:11
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
    
if __name__ == "__main__":
    unittest.main()