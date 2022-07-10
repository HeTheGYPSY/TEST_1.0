import time
import socket
from datetime import datetime as dt
hosts_path = "/etc/hosts"  # change hosts path according to your OS
redirect = socket.gethostbyname(socket.gethostname())
website_list = ["www.facebook.com", "mobile.facebook.com", "dub119.mail.live.com", "www.dub119.mail.live.com"]

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
		print("Working hours...")
		with open(hosts_path, 'r+') as file:
			content = file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect + " " + website + "\n")  # mapping hostnames to your localhost IP address
	else:
		with open(hosts_path, 'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()  # removing hostnames from host file

		print("Fun hours...")
	time.sleep(5)
