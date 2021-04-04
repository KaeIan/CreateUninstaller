import os

# get the root path.
rootPath = input("Enter Path: ")

# bash or powershell
scriptType = ""
while(scriptType != "bash" and scriptType != "powershell") :
	scriptType = input("bash or powershell: ")

extension = ".ps1" if scriptType == "powershell" else ".sh"
removeCommand = "Remove-Item " if scriptType == "powershell" else "rm "

# create the uninstaller script in the root path of the project.
uninstallPath = rootPath + "/uninstall" + extension
f= open(uninstallPath,"w+")

for subdir,dirs,files in os.walk(rootPath):
	if(".git" in subdir) :
		continue
	for file in files:
		relPath = os.path.relpath(os.path.join(subdir, file), rootPath)
		print(relPath)
		f.write(removeCommand + "\"" + relPath + "\"" + "\n")
f.close()
print("generated uninstall script to: " + uninstallPath)