################################################## executing commands on linux host using python ##############
  This source is written by considering following csv formate:
  a) change password csv ----> Hostname , domain , username , password , newpassword;  
  b) create user csv ----> Hostname , domain , username , adminstartor, administrator_password ;
  c) delete user csv ----> Hostname , domain , username , adminstartor, administrator_password ;
  b) delete group csv ----> Hostname , domain , groupname , adminstartor, administrator_password ;
 
 source contains following classes:
  
  main class (ch_pw) : responsible for reading csv and runing all commands
			  csvpath  : 	reading path.conf for finding path of perticular csv
			  connection :  establishing ssh connection with server
			  command :  using connection established by connection class to execute commands on server
			configuration file:
			path.conf : contains all paths of csv  
1)----> password changing:
			changing password of perticular user requires following field 
				a) username
				b) password
				c) fully qualified domain name
			using command passwd password change is possible
2) ----> creating user:
			creating user in unix required to execute following command:
			####  adduser newusername
			for executing this command needs administrator log in or sudo user, our csv should contains administrator 				authentication. 
3) ----> deleting user:
			deleting user in unix required to execute following command:
			####  deluser username
			for executing this command needs administrator log in or sudo user, our csv should contains administrator 				authentication. 
4) ----> deleting group:
			deleting group in unix required to execute following command:
			####  delgroup groupname
			for executing this command needs administrator log in or sudo user, our csv should contains administrator 				authentication. 
			
