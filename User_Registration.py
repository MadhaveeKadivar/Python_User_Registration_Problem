'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-22 21:13:20
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-22 21:21:23
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

def last_name(fname):
    """ 
        Description: 
            This function is matching User's Last name(Minimum 3 character having first character as capital) with regex pattern
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

    # Last Name
    lname = input("\nEnter last name : ")
    is_lname_valid = last_name(lname)
    if is_lname_valid:
        print(f"\n{lname} : Valid")
    else :
        print(f"\n{lname} : Invalid")