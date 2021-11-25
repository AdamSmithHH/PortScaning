import os
import time

os.system("apt-get install figlet")
os.system("figlet PORT SCANING")

print("""
How to use port scaning?
1) Port Scaning Fast
2) Service and Version info
3) OS INFO

""")
vote=input("Choose :")
if vote =='1':
    attackip=input("Attack IP :")
    os.system("nmap -sC -sV "+attackip)

elif vote =="2":
    attackip = input("Attack IP :")
    os.system("nmap -sS -sV "+attackip)
elif vote=="3":
    attackip = input("Attack IP :")
    os.system("nmap -0 "+attackip)
else:
    print("404 not found")