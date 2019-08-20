#!/usr/bin/python3

## import Paramiko for SSH, import OS for operating system
import paramiko,os


## shortcut issuing commands to remote
def commandissue(sshsession, command_to_issue):
    ssh_std, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

## list of targets
def gettargets():
    targetlist = []
    targetip = input("What IP address do you want to connect to? ")
    targetlist.append(targetip)
    targetuser = input("What Username would you like to use? ")
    targetlist.append(targetuser)
    return targetlist

def main():
    ## begin collecting information to connect.
    connectionlist = []
    while(True):
        connectionlist.append(gettargets()) ## creds to connect
        zvarquit = input("Do you want to continue? (y/N): ")
        if (zvarquit.lower() == 'n') or (zvarquit == ""):
            break


    ## prepare requirements file
    # reqlocation = input("Please provide the path to the requirements file to deploy: ")
    reqfile = input("What is the name of the requirements file: Press ENTER for default (requirement.txt): ")
    if reqfile == "":
        reqfile = "requirements.txt"

    ## define SSH session
    sshsession = paramiko.SSHClient()

    ################ IF YOU WANT TO CONNECT USING UN/PW #######################
    #sshsession.connect(server, username=username, password=password)
    ############### IF USING KEYS #############

    ## mykey is our private key
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    ## if we never went to this SSH host, add the fingerprint to the known host file
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ##  connectionlist = [["10.10.2.3", "bender"]["10.10.2.4", "fry"]]
    for x in range(len(connectionlist)):
        sshsession.connect(hostname=connectionlist[x][0], username=connectionlist[x][1], pkey=mykey)
        print(commandissue(sshsession, "ls"))
        ftp_client=sshsession.open_sftp()
        ftp_client.put(reqfile,reqfile)
        print(commandissue(sshsession, "ls -lrth"))
        ftp_client.close()

        commandissue(sshsession, "sudo apt-get update -y")
        commandissue(sshsession, "sudo apt install python3-pip -y")  # ensure pip is installed
        commandissue(sshsession, "python3 -m pip install -r " + reqfile)

if __name__ == "__main__":
    main()
