'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-22 21:13:20
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-22 21:13:56
    @Title : User Registration Problem
'''
import re

def first_name(fname):
    """ 
        Description: 
            This function is matching User's First name(Minimum 3 character having first character as capital) with regex pattern
        Parameter:
            It takes one string as argument
        Return:
            returns True or False
    """
    pattern = "^[A-Z][a-z]{2,}$"
    if re.match(pattern,fname):
        return True
    else:
        return False

if __name__=="__main__":
    # First Name
    fname = input("\nEnter first name : ")
    is_fname_valid = first_name(fname)
    if is_fname_valid:
        print(f"\n{fname} : Valid")
    else :
        print(f"\n{fname} : Invalid")

