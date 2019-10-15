import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import pandas as pd
import time
import traceback

"""
SMTP
!!!
You should allow less secure apps before start
!!!
https://myaccount.google.com/lesssecureapps

"""


df = pd.read_excel (r'Example.xlsx') 
mailarray = []
totalmail = 0

for index, row in df.iterrows():
	mailarray.append(row['MAIL ADDRESSES'])

for i in mailarray:
	message = MIMEMultipart()

	message["From"] =  "YOUR GMAİL ADDRESS WILL BE HERE" # From
	
	message["To"] = i # To

	message["Subject"] = "Subject"  # Subject

	# Content of our mail
	text = """
	
	"""

	text_body =  MIMEText(text,"plain") 

	message.attach(text_body) 

	try:
		mail =  smtplib.SMTP("smtp.gmail.com",587) 

		mail.ehlo() 
	 
		mail.starttls() 

		mail.login("YOUR GMAİL","YOUR PASSWORD") # your gmail and password

		mail.sendmail(message["From"],message["To"],message.as_string())  # sending
		print("Mail sent successfully.... " + str(message["To"]))
		mail.close() 

	except:
		traceback.print_exc()
		sys.stderr.write("Mail delivery failed... "+ str(message["To"]) ) 
		sys.stderr.flush()
	totalmail = totalmail + 1
	if(mailarray[-1] != i):
		time.sleep(20)
	
print("Number of mail sent: " + str(totalmail))	
