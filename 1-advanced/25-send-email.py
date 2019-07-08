# Python has Built in Module smtplib
# For mail server, we can use localhost or smtp.gmail.com:587 provided by Google

# Test the email
#     - Use local SMTP debugging server or using the smtpd module that comes preinstalled
#     - Command : `python -m smtpd -c DebuggingServer -n localhost:1025` (Ctrl + C to stop)
#     - It discards sending them to the email and prints their content to the console
#     - Running a local server doesn't require you to configure encryption of messages or to login to email server

import re
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

USERNAME = ''
PASSWORD = ''

# MAILSERVER = 'smtp.gmail.com'
# PORT = 587

# The advantage of using smtpd utility is that you can test but no mail is sent to the recipient
# Mail sent from the script was discarded and the output is shown in the console
MAILSERVER = 'localhost'
PORT = 1025

def sendmail(pMailParams):
    try:
        vFinalRec = pMailParams.get(
            'to') + pMailParams.get('cc') + pMailParams.get('bcc')
        objMime = MIMEMultipart()
        objMime['From'] = pMailParams.get('from')
        objMime['To'] = ",".join(pMailParams.get('to'))
        objMime['Cc'] = ",".join(pMailParams.get('cc'))
        objMime['Bcc'] = ",".join(pMailParams.get('bcc'))
        objMime['Subject'] = pMailParams.get('sub')
        objMime['Date'] = formatdate(localtime=True)
        objMime.attach(MIMEText(pMailParams.get('body'), 'html'))
        print('Connecting to ', MAILSERVER)

        objSMTP = smtplib.SMTP(MAILSERVER, PORT)
        # To identify yourself to the server, .helo() (SMTP) or .ehlo() (ESMTP) should be called after creating an .SMTP() object, and again after .starttls()
        # This function is implicitly called by .starttls() and .sendmail()
        # Un-comment below section for encryption of messages or to log in to an email server
        
        # objSMTP.ehlo()		# HELO to eSMTP server
        # objSMTP.starttls()  # Start Transport Layer Security
        # objSMTP.ehlo()		# HELO to eSMTP server
        # objSMTP.login(USERNAME, PASSWORD)

        objSMTP.sendmail(pMailParams.get('from'),
                         vFinalRec, objMime.as_string())
        objSMTP.quit()
    except Exception as e:
        print('Error: Error occurred while sending mail!\nSee details: ', str(e))
    else:
        print('\nMail sent successfully!')


def main():
    global USERNAME, PASSWORD
    try:
        vEmailPat = r"^([a-zA-Z0-9\.\-_]+)@([a-zA-Z0-9\.\-_]+)\.([a-zA-Z]{2,5})$"
        vToEmailId = input('Give Email-Id of Recipient: ')

        if re.match(vEmailPat, vToEmailId):
            vSubject = input('Enter Subject: ')
            vMessage = input('Enter Message: ')
            USERNAME = input('Enter Username to Login: ')  # gmail Id
            PASSWORD = getpass.getpass('Enter Password to Login: ')
            vParams = {
                'from': USERNAME,
                'to': [vToEmailId],
                'cc': ['indranil.paul@cognizant.com', 'Ashwini.D2@cognizant.com'],
                'bcc': [USERNAME],
                'sub': vSubject,
                'body': 'Hello,<br><br>{0}<br><br>-- Python'.format(vMessage)
            }
            sendmail(vParams)
        else:
            print('Warn: Please provide valid email id!')
    except Exception as e:
        print('Error.main: ', str(e))


main()
