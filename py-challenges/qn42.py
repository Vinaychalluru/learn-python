# Question 42

# Question
# Assuming that we have some email addresses in the "username@companyname.com" format, 
# please write program to print the user name of a given email address.
# Both user names and company names are composed of letters only.

import re
import traceback

try :
    emailID=input('Enter an email ID :')
    # \w - Matches Alpha numeric and Underscore [a-zA-Z0-9_]
    # searchObj = re.search(r'(\w+)@(\w+)\.com',emailID)
    searchObj = re.search(r'([a-zA-Z]+)@([a-zA-Z]+)\.com',emailID)
    if searchObj:
        print('The Username is', searchObj.group(1))
except Exception as e:
    print('Encountered an exception - ' + repr(e))
    traceback.print_exc()