############# class for ssh connection for perticular host 
import paramiko  
class s_connection:
  def __init__(self,u_name,u_pw,fqdn):  #### here fqdn is fully qualified domain name
	self.ssh = paramiko.SSHClient()
	self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	self.ssh.connect(fqdn,username=u_name,password=u_pw)
  def getCon(self):
	return self.ssh
	 
