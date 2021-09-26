import paramiko
import os
import sys
import time
import json
from getpass import getpass


try:
 print("==============================")
 print("Monitoring Network Device")
 print("==============================")

 while True:
  try:
   ip=input("masukkan address : ")
   r_ip=open(ip,"r").readlines()
   break
  except IOError:
   print("file tidak di temukan!!!")
   continue
  
 ip_list=[] 
 for x in r_ip:
   ip_list.append(x.strip())

 ip_list_ok=[]
 print("\n\ncek koneksi")
 for ip in ip_list:
  response=os.system("\nping -c 3 {}".format(ip)) 

  if response == 0:
   print("\n{} is up  ".format(ip))
   ip_list_ok.append(ip)
  else:
   print("\n{} is down  ".format(ip))
  print("========================================================")
 while True:
  try:
   syntax=input("masukkan nama file syntax: ")
   r_syntax=open(syntax,"r").readlines()
   break
  except IOError:
   print("File tidak ditemukan!!")
   continue

 username=input("Username: ")
 password=getpass()
 port=input("Port: ")
 print("Melakukan ekseskusi syntax....\n")
 for ip in ip_list_ok:
  ssh_client=paramiko.SSHClient()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh_client.connect(hostname=ip,username=username,password=password,port=port,allow_agent=False,look_for_keys=False)
  print("Sukses Login ke {}".format(ip))
  for config in r_syntax:
   stdin, stdout, stderr=ssh_client.exec_command(config)
   hasil=stdout.readlines()
   temporary_hasil=[s.replace("\r\n", "") for s in hasil]
   new_hasil=[s.replace(" ", "") for s in temporary_hasil]
   time.sleep(1)
   if new_hasil!="":
    print(new_hasil)
   else:
    print("There was no output for this command")
  print("Sukses Pengecekan {}\n".format(ip))
  print("================================")
except KeyboardInterrupt:
 print("program sudah keluar")
 sys.exit()
