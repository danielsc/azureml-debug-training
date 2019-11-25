import sys
import os
from os.path import expanduser
home = expanduser("~")

def create_ssh_folder():
    try:
        os.mkdir(home+"/.ssh/")
    except FileExistsError:
        print("Already have an .ssh folder")
    
    dir_path = os.path.join(home,".ssh","config")
    if os.path.exists(dir_path):
        print("Already have an .ssh config file")
    else:
        f= open(dir_path,"w+")
        f.close() 
        

def create_RSA_file(IP_address,RSA_key):
    dir_path = os.path.join(home,".ssh","id_rsa"+IP_address)
    f= open(dir_path,"w")
    for line in RSA_key:
        f.write(line)
    f.close
    return dir_path
    
def create_config_file(IP_address,RSA_key):
    config_text = "\n#"+"---"*10 + "\n" + "Host " + IP_address + "\n      HostName " + IP_address + " \n      Port 22 \n      User azureuser \n      IdentityFile " + create_RSA_file(IP_address,RSA_key) + "\n"
    dir_path = os.path.join(home,".ssh","config")
    f= open(dir_path,"a")
    f.write(config_text)
    f.close
    
def run():
    create_ssh_folder()
    IP_address = input("Paste IP address: ")
    print("Paste RSA Key: ")
    RSA_key = sys.stdin.readlines()
    create_config_file(IP_address,RSA_key)

run()