import os
import subprocess


filename = ".ssh/config"

if not os.path.exists(".ssh"):
    os.makedirs(".ssh")
    print("ssh folder created\n")

if os.path.exists(filename):
    print("""
    Config File exists
    Now We Editing the same Config file
    Creating The ssh config File
    """)
    config = open(filename, 'a')
else:
    config = open(filename, 'w')
    print(config)

if input("Do you want to create ssh key [y/N]. You can skip with Enter: ") == 'y':
    os.system("ssh-keygen -t rsa")

print("\n")

scan1 = input("Enter your IP to scan your network for open ssh: ")
os.system("nmap -v " + str(scan1) + "/24" + "| grep " + " 'ssh'")

print("\n")

scan2 = input("Scan Your network for IP Addresses: ")
process = subprocess.Popen(
    "nmap -v  " + str(scan2) + "/24  |  grep  'port 22'",
    shell=True,
    stdout=subprocess.PIPE,
)

stdout_list = process.communicate()[0].decode('utf-8')
command = stdout_list.split('\n')


def ask_for_input(text):
    user_input = None
    while not user_input:
        user_input = input(text)
    return user_input


template = """
Host {machine_name}
Hostname {selected_ip}
Port {port}
User {user}
"""

try:
    for ip_string in command:
        if ip_string:
            ip = ip_string.split()[-1]
            if input("Discovered IP: " + "(" + ip + ")" + "\n" + "Do you want to select this IP Address [y/N]:") == 'y':
                selected_ip = ip

                machine_name = ask_for_input("Please Enter Machine Name: ")
                root_user = ask_for_input("This for the root user:")
                port = input("Please Enter The Port Number. Skip with Enter: ") or '22'
                user = ask_for_input("Please Enter The User: ")
                shh_to_machine = input("Copy the ssh id to the machine. Do you want to continue (y) ").lower()
                shh_to_root = input("Copy the ssh id to root. Do you want to continue (y):").lower()

                normal_config = template.format(
                    machine_name=machine_name,
                    root_user=root_user,
                    port=port,
                    user=user,
                    selected_ip=selected_ip,
                )
                config.write(normal_config)

                if shh_to_root == 'y':
                    root_config = template.format(
                        machine_name=machine_name,
                        root_user=root_user,
                        port=port,
                        user='root',
                        selected_ip=selected_ip,
                    )
                    config.write(root_config)

                if shh_to_machine:
                    os.system("ssh-copy-id " + user + "@" + selected_ip)

                if shh_to_root:
                    os.system("ssh -t root@" + selected_ip + " " + " " " 'sudo cp --parents .ssh/authorized_keys /root/' ")

                print("Finished and starting with the new machine\n\n")

except KeyboardInterrupt:
    config.close()
print("Information saved")

