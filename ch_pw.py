##################################### password change class ...responsible for reading csv and changing password
import csv
from con import s_connection
from csvpath import path
from command import commands
############## finding path of csv #############
chpw_path=path("ch_pw")
createuser_path=path("create_user")
deleteuser_path=path("delete_user")
deletegroup_path=path("delete_group")
################## changing password of perticular users from csv ############ 
with open(chpw_path.getPath()) as csvfile:     
    readCSV = csv.DictReader(csvfile)     ################## changing rows of csv in dictionary
    for row in readCSV:
	u_name=row["Username"]
	u_pw=row["Password"] 
	n_pw=row["NewPassword"]	
        fqdn=row["Hostname"]+"."+row["domain"]+".com"
	obj1=commands(fqdn,u_name,u_pw)  ##### creating connection #########
	obj1.changePassword(n_pw,u_pw) ####### change password command execution
################## creating new users from csv ############ 
with open(createuser_path.getPath()) as csvfile:
    readCSV=csv.DictReader(csvfile)
    for row in readCSV:
        u_name=row["user_Username"]
        u_pw=row["user_Password"]
        administrator=row["Admin_Username"] #### require admin username and password 
        administrator_pw=row["Admin_Password"]
        fqdn=row["Hostname"]+"."+row["domain"]+".com"
        obj1=commands(fqdn,administrator,administrator_pw)
        obj1.createUser(u_name,u_pw)
################## deleting users from csv ############
with open(deleteuser_path.getPath()) as csvfile:
    readCSV=csv.DictReader(csvfile)
    for row in readCSV:
        u_name=row["user_Username"]
        administrator=row["Admin_Username"] ######## establishing connection with admin authentcation of perticular domain
        administrator_pw=row["Admin_Password"]
        fqdn=row["Hostname"]+"."+row["domain"]+".com"
        obj1=commands(fqdn,administrator,administrator_pw)
        obj1.deleteUser(u_name)
################## deleting groups from csv ############
with open(deletegroup_path.getPath()) as csvfile:
    readCSV=csv.DictReader(csvfile)
    for row in readCSV:
        g_name=row["Groupname"]
        administrator=row["Admin_Username"] ######## establishing connection with admin authentcation of perticular domain
        administrator_pw=row["Admin_Password"]
        fqdn=row["Hostname"]+"."+row["domain"]+".com"
        obj1=commands(fqdn,administrator,administrator_pw)
        obj1.deleteGroup(g_name)
