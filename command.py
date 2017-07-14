######################### class for executing commands ######################
class commands:
 def changePass(fqdn,u_name,u_pw,n_pw):
	c=s_connection(u_name,u_pw,fqdn)
	ssh=c.getCon()
	stdin, stdout, stderr =ssh.exec_command("passwd")
	stdin.write(u_pw+'\n')
	stdin.write(n_pw+'\n')
	stdin.write(n_pw+'\n')
	stdin.flush()
	out = stdout.readlines()
	for line in out:
          print line
