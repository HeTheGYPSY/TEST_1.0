import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib


port = int(input("Which mail port would you like to use (578/465)? "))
Email = input("Which email would you like to use? ")
Password = str(input("Enter the password: "))
smtp = smtplib.SMTP('smtp.gmail.com', port)
smtp.starttls()
smtp.ehlo()
smtp.login(Email, Password)


def message(subject="Python Notification", text="", img=None, attachment=None):
	to = []
	count = 0
	while count < 10:
		recp = input("Enter a mail recipient: ")
		if recp is not None:
			recp = input("Enter a mail recipient: ")
			to.append(recp)
			count += 1
	print("The address list is: {}".format(to))
	msg = MIMEMultipart()
	msg['Subject'] = subject
	msg.attach(MIMEText(text))
	if img is not None:
		if type(img) is not list:
			img = [img]

		for one_img in img:
			img_data = open(one_img, 'rb').read()
			msg.attach(MIMEImage(img_data, name=os.path.basename(one_img)))

	if attachment is not None:
		if type(attachment) is not list:
			attachment = [attachment]

		for one_attachment in attachment:
			with open(one_attachment, 'rb') as f:
				file = MIMEApplication(
					f.read(),
					name=os.path.basename(one_attachment)
				)
			file['Content-Disposition'] = f'attachment;\
			filename="{os.path.basename(one_attachment)}"'
			msg.attach(file)
	smtp.sendmail(from_addr=Email, to_addrs=to, msg=msg.as_string())
	smtp.quit()


message(subject="THIS IS IT!", text="Hear me now")
