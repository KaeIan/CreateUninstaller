import os

# get user input to determine the root path for the uninstall script.
rootPath = input("Enter Path: ")

scriptType = ""
while(scriptType != "bash" and scriptType != "powershell") :
	scriptType = input("bash or powershell: ")

extension = ".ps1" if scriptType == "powershell" else ".sh"
removeCommand = "Remove-Item " if scriptType == "powershell" else "rm "

# create the uninstaller in the root path of the project.
uninstallPath = rootPath + "/uninstall" + extension
f= open(uninstallPath,"w+")

for roots,dirs,files in os.walk(rootPath):
	if(files and dirs) :
		fullPath = ""
		# join the directory paths together.
		for dir in dirs:
			fullPath = dir + "/"
		for file in files:
			# we want to write a removal for each file.
			print(fullPath + file)
			f.write(removeCommand + fullPath + file + "\n")
f.close()
print("generated uninstall script to: " + uninstallPath)
