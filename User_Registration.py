'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-22 21:13:20
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-22 22:52:09
    @Title : User Registration Problem
'''
import re
import logging
# Logging
logging.basicConfig(filename = 'file.log',format = '%(asctime)s | %(levelname)s | %(lineno)d: %(message)s')
logger = logging.getLogger("root_logger")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
log_format = '%(message)s'
console_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(console_handler)
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
    pattern =  "^[0-9a-zA-Z]+[./+_-]{0,1}[0-9a-zA-Z]+[@][a-zA-Z0-9]+[.][a-zA-Z]{2,}([.][a-zA-Z]{2,}){0,1}$"
    if re.match(pattern,email):
        return True
    else:
        return False

def mobile_number_check(mobile_no):
    """ 
        Description: 
            This function is matching User's mobile number with regex pattern
        Parameter:
            It takes one mobile number string as argument
        Return:
            returns True or False
    """
    pattern = "^[9][1][ ][6-9][0-9]{9}$"
    if re.match(pattern,mobile_no):
        return True
    else:
        return False

def password_rule_1_check(password):
    """ 
        Description: 
            This function is matching User's paasword for rule 1(Minimum 8 character) with regex pattern
        Parameter:
            It takes one password string as argument
        Return:
            returns True or False
    """
    pattern = "^[0-9a-zA-Z@#$%^&*!+=]{8,}"
    if re.match(pattern,password):
        return True
    else:
        return False

def password_rule_2_check(password):
    """ 
        Description: 
            This function is matching User's paasword for rule 2(Atleast one upper case) with regex pattern
        Parameter:
            It takes one password string as argument
        Return:
            returns True or False
    """
    pattern = "^(?=.*[A-Z])[0-9a-zA-Z@#$%^&*!+=]{8,}$"
    if re.match(pattern,password):
        return True
    else:
        return False

def password_rule_3_check(password):
    """ 
        Description: 
            This function is matching User's paasword for rule 3(Atleast one digit) with regex pattern
        Parameter:
            It takes one password string as argument
        Return:
            returns True or False
    """
    pattern = "^(?=.*[A-Z])(?=.*[0-9])[0-9a-zA-Z@#$%^&*!+=]{8,}$"
    if re.match(pattern,password):
        return True
    else:
        return False

def password_rule_4_check(password):
    """ 
        Description: 
            This function is matching User's paasword for rule 4(has exactly one special character) with regex pattern
        Parameter:
            It takes one password string as argument
        Return:
            returns True or False
    """
    pattern = "^(?=.{8,}$)(?=.*[0-9])(?=.*[A-Z])[A-Za-z0-9]{0,}[@~!#$%^&*+=\/-]{1}[a-zA-Z0-9]{0,}$"
    if re.match(pattern,password):
        return True
    else:
        return False
    
if __name__=="__main__":
    # First Name
    fname = input("\nEnter first name : ")
    is_fname_valid = first_name(fname)
    if is_fname_valid:
        logger.info(f"\n{fname} : Valid")
    else :
        logger.info(f"\n{fname} : Invalid")

    # Last Name
    lname = input("\nEnter last name : ")
    is_lname_valid = last_name(lname)
    if is_lname_valid:
        logger.info(f"\n{lname} : Valid")
    else :
        logger.info(f"\n{lname} : Invalid")

    # Email
    email = input("\nEnter Email : ")
    is_email_valid = email_check(email)
    if is_email_valid:
        logger.info(f"\n{email} : Valid")
    else :
        logger.info(f"\n{email} : Invalid")

    # Mobile Number
    mobile_no = input("\nEnter Mobile Number : ")
    is_mobile_no_valid = mobile_number_check(mobile_no)
    if is_mobile_no_valid:
        logger.info(f"\n{mobile_no} : Valid")
    else :
        logger.info(f"\n{mobile_no} : Invalid")

    # Password rule 1
    password = input("\nEnter password : ")
    is_password_valid = password_rule_4_check(password)
    if is_password_valid:
        logger.info(f"\n{password} : Valid")
    else :
        logger.info(f"\n{password} : Invalid")