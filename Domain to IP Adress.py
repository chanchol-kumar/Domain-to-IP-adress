# Domain-to-IP-addresses

import socket
import pyfiglet

banner = pyfiglet.figlet_format("Domain    to    IP")
print(banner)

domain = input("Enter domain : ")
ip = socket.gethostbyname(domain)

print("IP : " + ip)


