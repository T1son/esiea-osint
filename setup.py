#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### IMPORTS -----------------------------------------------------------------------------------------------------------------------------------------

import os, sys, subprocess, math

# Check the current version of Python
if sys.version_info[0] < 3:
    print("Please, use Python 3.")
    # Quit the program
    exit()

### MAIN --------------------------------------------------------------------------------------------------------------------------------------------

# Absolut path to the modules directory
modulesPath = os.sep.join([os.path.dirname(os.path.abspath(__file__)), "modules"])
# List of modules
modulesList = os.listdir(modulesPath)

# If there at least one module
if len(modulesList) > 0:
	# Print the banner
	print(" Download of requirements:\n")
	# Lenght of the longest module name for esthetical printing purpose
	longestModuleName = max(modulesList, key=len)

	# For each module in the list
	for module in modulesList:
		# Set the path to the requirements file
		filePath = os.sep.join((modulesPath, module, "requirements.txt"))
		# If a requirements file exist
		if os.path.exists(filePath):
			# Print the current module name
			print("\t■ {}".format(module) + " " * (len(longestModuleName) - len(module)), end="\t\t")
			
			# Open the requirements file
			with open(filePath, "r") as file:
				# Set the list of packages
				packages = file.read().split("\n")
				# Remove the empty names
				packages = [package for package in packages if package != ""]
				# Set the count of package for printing purpose
				packagesCount = len(packages)
				# Set a current package index for printing purpose
				currentPackageIndex = 0

				# For each package in the list
				for package in packages:
					# Start the download
					output = subprocess.Popen([sys.executable, "-m", "pip", "install", package], stdout=open(os.devnull, "wb"), stderr=subprocess.PIPE)
					# Get the errors
					error = output.communicate()[1].decode()
					# If there is at least one error
					if error != "":
						# Print them
						print("\n\n{}".format(error))
					# If there is no error
					else:
						# Increase the current package index for printing purpose
						currentPackageIndex += 1
						# Set the current download progress for printing purpose
						currentProgress = int(currentPackageIndex * 100 / packagesCount)
						# If these is not the first package of the list
						if (currentPackageIndex > 1):
							# Erase the previous progress
							sys.stdout.write("\b" * 20)
							sys.stdout.flush()
						# Print the new progress
						print("{}%\t[".format(currentProgress) + ("■" * int(currentProgress / 10)) + (" " * math.ceil((100 - currentProgress) / 10)) + "]{}".format("\n" if packagesCount == currentPackageIndex else ""), end="")
		
		# If no requirements file found
		else:
			print("No requirements found for the {} module".format(module))

# If no modules fond
else:
	print("No modules found at {}.".format(modulesPath))