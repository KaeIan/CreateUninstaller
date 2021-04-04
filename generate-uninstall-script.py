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

excludePaths = set([".git", "bin", "obj", ".vs", ".vscode"])

for subdir,dirs,files in os.walk(rootPath, True):
	dirs[:] = [d for d in dirs if d not in excludePaths]
	for file in files:
		relPath = os.path.relpath(os.path.join(subdir, file), rootPath)
		f.write(removeCommand + "\"" + relPath + "\"" + "\n")
f.close()
print("generated uninstall script to: " + uninstallPath)