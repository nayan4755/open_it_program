import os

txt = raw_input("Enter your command: ")

lst = [txt]

for x in lst:
	if (("open" in x) or ("run" in x) or ("execute" in x)) and ("calculator" in x):
		os.system('bash -c gnome-calculator')

	elif (("open" in x) or ("run" in x) or ("execute" in x)) and ('camera' in x):
		os.system('bash -c cheese')

	elif (("open" in x) or ("run" in x) or ("execute" in x)) and ('settings' in x):
		os.system('bash -c gnome-control-center')

	elif (("open" in x) or ("run" in x) or ("execute" in x)) and ('browser' in x):
		os.system('bash -c sensible-browser')
	
	elif (("open" in x) or ("run" in x) or ("execute" in x)) and ('chrome' in x):
		os.system('bash -c sensible-browser')

	elif (("open" in x) or ("run" in x) or ("execute" in x)) and ('google' in x):
		os.system('bash -c sensible-browser')
	
	elif (("open" in x) or ("run" in x) or ("execute" in x)) and ('file' in x):
		os.system('bash -c nautilus')

	elif ("exit" in x) or ("quit" in x):
		print "Have a good day!"
		break

	else:
		print ("out of my powers")
