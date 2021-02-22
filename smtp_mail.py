import dns.resolver
import telnetlib
import time

mx_records = []

print(colored("Welcome", "red"))

email = b"zworkrowz@gmail.fr"

#Get MX records for a specific domain
for data in dns.resolver.resolve('gmail.com', 'MX'):
	mx_records.append(''.join(str(data).split(' ')[1][:-1]))


#Check for every read if it's the intended output
telnet = telnetlib.Telnet(mx_records[0], 25, timeout=5)
telnet.set_debuglevel(1)
telnet.read_until(b"220")
telnet.write(b"EHLO test\r\n")
telnet.read_until(b"250")
telnet.write(b"mail from:<random@gmail.com>\r\n")
telnet.read_until(b"250")
time.sleep(1)
telnet.write(b"rcpt to:<" + email + b">\r\n")
data = telnet.read_until(b"550", timeout=1)

#print(data)

#550 is the code for non existing email address
if("550" in str(data)):
	print("Not exists")
else:
	print("Exists")

telnet.close()