#!/usr/bin/python3.5




## Rygel, My Personal Assitant
##
##
##

#import modules
import re
import os
import sys


def settings_open():
	## Open Files
	settings_file = open("settings.rygel.config","r+")
	return settings_file

def settings_close(settings_file):
	settings_file.close()
	
def settings_init(settings_file):

	## Check settings_file
	settings_file_output = settings_file.read()

	name_match = re.match("name=[a-zA-Z0-9]{1,15}$",settings_file_output)

	if(name_match):
		print("Successfully recalled settings...")
		name_split = re.split(r"=",name_match.group(0))
		name = name_split[1]
		print("Hello, " + name)
   
	else:
		print("No settings found...")
   
	while(name == ""):
		name = input("What can I call you? ")

		if(re.match("[^a-zA-Z0-9]{1,15}$",name)):
			print("That is too complex to say, please use a short name between 1-15 alphanumeric characters. ")
		elif(name != ""):
			print("Hello, " + name)
			settings_file.seek(0,0)
			settings_file.write("name=" + name)
	
	return {'name': name,}


# Main Function

def main():
	settings_config = settings_open()
	session_vars = settings_init(settings_config)
	settings_config.close()
	
	
	while True:

		# Process Command
   
		# Get Input
		command = input("---?> ")

		if(re.match(r'!exit',command,re.I)):
			print("Live Long and Prosper, " + session_vars["name"])
			break
		else:
			print("Unknown Command, please try again.")

	
       
   
if __name__ == '__main__':
	main()
   


   


