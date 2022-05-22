'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-22 21:13:20
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-22 21:33:01
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

def last_name(lname):
    """ 
        Description: 
            This function is matching User's Last name(Minimum 3 character having first character as capital) with regex pattern
        Parameter:
            It takes one string as argument
        Return:
            returns True or False
    """
    pattern = "^[A-Z][a-z]{2,}$"
    if re.match(pattern,lname):
        return True
    else:
        return False

def email_check(email):
    """ 
        Description: 
            This function is matching User's email with regex pattern
        Parameter:
            It takes one email string as argument
        Return:
            returns True or False
    """
    pattern =  "^[0-9a-zA-Z]+[./+_-]{0,1}[0-9a-zA-Z]+[@][a-zA-Z0-9-]+[.][a-zA-Z]{2,}([.][a-zA-Z]{2,}){0,1}$"
    if re.match(pattern,email):
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

    # =Email
    email = input("\nEnter last name : ")
    is_email_valid = email_check(email)
    if is_email_valid:
        print(f"\n{email} : Valid")
    else :
        print(f"\n{email} : Invalid")