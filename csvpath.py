import re
class path:
 def __init__(self,task):
	self.task=task
 def getPath(self):
	p = re.compile(self.task)
	file = open("path.conf", 'r') ########## path.conf is paths configuration file
	for line in file: 
	  m = p.match( line )
	  if m:
    	   a=line.split('=')
	   t=a[1].strip()
	   return t
	  else:
    	   return "" 

	
