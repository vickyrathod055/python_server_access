##################################### password change class ...responsible for reading csv and changing password
import csv
from con import s_connection
from csvpath import path
from command import commands
f_path=path("ch_pw")  ############## finding path of password change csv
with open(f_path.getPath()) as csvfile:     
	readCSV = csv.DictReader(csvfile)     ################## changing rows of csv in dictionary
	for row in readCSV:
	  	u_name=row["Username"]
		u_pw=row["Password"] 
		n_pw=row["NewPassword"]	
          	fqdn=row["Hostname"]+"."+row["domain"]+".com"
		commands.changePass(fqdn,u_name,u_pw,n_pw) ####### change password command execution 
		
	   	
	  
