import paramiko
import os
import sys
import time
from getpass import getpass


try:
 print("==============================")
 print("Check Signal Streght Ubiquity ")
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
   ubiquity=input("masukkan nama file syntax: ")
   r_ubiquity=open(ubiquity,"r").readlines()
   break
  except IOError:
   print("File tidak ditemukan!!")
   continue

 username=input("Username: ")
 password=getpass()


 print("Melakukan Konfigurasi....\n")
 for ip in ip_list_ok:
  ssh_client=paramiko.SSHClient()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh_client.connect(hostname=ip,username=username,password=password)
  print("Sukses Login ke {}".format(ip))
  for config in r_ubiquity:
   stdin, stdout, stderr=ssh_client.exec_command(config)
   hasil=stdout.readlines()
   time.sleep(1)
   if hasil!="":
    #print("Hasil:{}\n ".format(hasil))
    print(hasil)
   else:
    print("There was no output for this command")
  print("Sukses Pengecekan {}\n".format(ip))
  print("================================")
except KeyboardInterrupt:
 print("program sudah keluar")
 sys.exit()
