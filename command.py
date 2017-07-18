######################### class for executing commands ######################
import paramiko
class commands:
    def __init__(self,fqdn,u_name,u_pw):  #### here fqdn is fully qualified domain name
     self.ssh = paramiko.SSHClient()
     self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     self.ssh.connect(fqdn,username=u_name,password=u_pw)
    ###      changing password             ########
    def changePass(self,n_pw,u_pw):
	stdin, stdout, stderr =self.ssh.exec_command("passwd")
	stdin.write(u_pw+'\n')
	stdin.write(n_pw+'\n')
	stdin.write(n_pw+'\n')
	stdin.flush()
	out = stdout.readlines()
	for line in out:
          print line
########creating new user ############
    def createUser(self,u_name,u_pw):
        stdin,stdout,stderr=self.ssh.exec_command("adduser "+u_name)
        stdin.write(u_pw)
        stdin.write(u_pw)
        stdin.flush()
        out=stdout.readlines()
        for line in out:
          print line
######## deleting users ########
    def deleteUser(self,u_name):
        stdin,stdout,stderr=self.ssh.exec_command("deluser --remove-home "+u_name)
        out=stdout.readlines()
        for line in out:
          print line
############ deleting groups #########
    def deleteGroup(self,g_name):
        stdin,stdout,stderr=self.ssh.exec_command("groupdel "+g_name)
        out=stdout.readlines()
        for line in out:
          print line
