#!/usr/bin/env python3

from sys import argv
import atexit
import os
import subprocess
script, filename = argv
import base64
import string

if not os.path.exists(".ssh"):
    os.makedirs(".ssh")
    print ("ssh folder created")
    print ("\n")


if os.path.exists('.ssh/' + filename):
    print ("Config File exists in .ssh/")
    print ("Now We Editing the same Config file")
    print ("\n")

filename = ".ssh/config"



def exit_handler():
    print ('Information Saved')


if os.path.exists:
    config = open(filename, 'a')
    print ("Creating The ssh config File")
    print ("\n")
else: 
    config = open(filename, 'w')
    print (config)

if input("Do you want to create ssh key [Y/n]. You can skip with Enter: ") == 'Y':
    os.system("ssh-keygen -t rsa")
print ("\n")

scan1 = input("Enter your IP to scan your network for open ssh: ")
os.system("nmap -v " + str(scan1) + "/24" + "| grep " + " 'ssh'")
print ("\n")

#scan2 = input("Scan Your network for IP Addresses: ")
#This only for testing 
scan2 = "192.168.56.1"
os.system("nmap -v " + scan2 + "/24" + "| grep" + " 'port 22'")


#process = subprocess.Popen("nmap -v  "+ scan2 +"/24  |  grep  'port 22'",
 #                            shell=True,
  #                           stdout=subprocess.PIPE,
   #                        )
#stdout_list = process.communicate()[0].decode('utf-8')

#print(stdout_list)

#splitlines()     


#scan2 = input("Scan Your network for IP Addresses: ")
process = subprocess.Popen("nmap -v  "+ str(scan2) +"/24  |  grep  'port 22'",
                             shell=True,
                             stdout=subprocess.PIPE,
                           )
stdout_list = process.communicate()[0].decode('utf-8')
  #string.split(inputString, '\n') 
command = stdout_list.split('\n')

selected_ip = None
for ip_string in command:
    if ip_string:
    #print('ass', ip_string)
      ip = ip_string.split()[-1]
    #print(ip_string, ip)  
      if input(ip + "Do you want to select this IP Address [Y/n]:") == 'y':
        selected_ip = ip
print(selected_ip, ip) 
#command = ['nmap', '-v', scan2 + '/24', '|' , 'grep'+ " " + "'port 22'"]
#result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
#print (result.stdout.decode('utf-8'))
#print (command)
#print(' '.join(command))
print ("\n")
try:
    while True:
            ip_string
            first = input("Please Enter Machine Name: ")
            zero = input("This for the root user:")
            #second = input("Please Enter The Hostname Of the Machine Or IP Address: ")
            second = input
            third = input("Please Enter The Port Number. Skip with Enter: ")
            fourth = input("Please Enter The User: " )
            fifth = input("Copy the ssh id to the machine. Do you want to continue (y) ")
            sixth = input("Copy the ssh id to root. Do you want to continue (y):")
            if first:
                config.write("Host " + first)
                config.write("\n")
            if second:
                config.write("Hostname " + ip + "\n")
                #config.write("Hostname " + second)
                #config.write("Hostname " + ip + selected_ip) 
                #config.write("\n")
            if third: 
                config.write("Port " + third)
                config.write("\n")
            if fourth:
                config.write("User " + fourth)
                config.write("\n")
                config.write("\n")
            if zero:
                config.write("\n")
                config.write("Host " + zero + "\n" + "Hostname " + ip + "\n" + third + "\n" + "User " + "root" + "\n")
                config.write("\n")   
            if fifth:
                    os.system("ssh-copy-id " + fourth + "@" + ip)
            if sixth:
                    os.system("ssh -t " + fourth + "@" + ip  + " " + " " " 'sudo cp --parents .ssh/authorized_keys /root/' ")    
            print ("Finished and starting with the new machine")
            print ("\n")
            if first == fourth:
                config.write("\n")
                config.write("\n")
except KeyboardInterrupt:
  config.close()
atexit.register(exit_handler)

