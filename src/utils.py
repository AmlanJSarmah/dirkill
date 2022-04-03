import os
import platform

def traverse_file_system(path,folder_name):
	platform_sys = platform.system()
	directories = []
	try:
		for dirpaths, dirnames, filenames in os.walk(rf'{path}'):
			if dirnames.count(folder_name) > 0:
				if platform_sys=='Windows': 
					directories.append(dirpaths +  '\\' + folder_name)
				else:
					directories.append(dirpaths + '/' + folder_name)
		return directories
	except:
		return []