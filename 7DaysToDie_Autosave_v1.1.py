# READ THE README

import shutil
import os
import re
import psutil
import datetime
import winsound
import errno
import time


# CONFIG

autosave_interval_seconds = 15*60		# autosave interval in seconds
autosaves_max = 15				# number of autosaves to keep. oldest ones will get deleted if you get over the limit

tone_frequency = 500		# Set beep frequency in Hertz
duration = 500			# Set beep duration in ms

bool_ask = False		# if enabled, will not delete anything automatically, but beep and ask everytime and show the path that will be deleted
bool_test = False		# debug option, ignore


src_fold = os.path.join("C:\\", "Users", "Kenira", "AppData", "Roaming", "7DaysToDie")		# put in your own path here! script does NOT double check for you so triple check!
dest_fold = os.path.join("E:\\", "bak", "7 Days To Die", "_Python")				# select a path to save the autosaves. make sure it's a folder with nothing else in it! don't just choose a path like C:\\, make a folder!


# END OF CONFIG


if bool_test:
	src_fold = os.path.join("F:\\", "Temp", "test1")
	dest_fold = os.path.join("F:\\", "Temp", "test2")
	autosave_interval_seconds = 5
	print("TESTING")
	print("Source: ", src_fold)
	print("Target: ", dest_fold)
	print("Interval: ", autosave_interval_seconds)
	print([p.name() for p in psutil.process_iter()])
	print("7DaysToDie.exe" in [p.name() for p in psutil.process_iter()])


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)
			
def get_autosave_directories(folder):
	directories = [d for d in os.listdir(folder) if (os.path.isdir(os.path.join(folder, d)) and "_autosave" in d)]
	return directories
	
def get_autosave_number(directories):
	autosaves = 0
	for dir in directories:
		if "_autosave" in dir:
			autosaves += 1
	return autosaves

while("7DaysToDie.exe" in [p.name() for p in psutil.process_iter()] or bool_test):
	new_folder_name = str(datetime.datetime.now().isoformat())
	new_folder_name = new_folder_name.replace(":", "_")
	new_folder_name = new_folder_name.replace(".", "_")
	new_folder_name += "___autosave"
	
	#print("New folder name after replacing: ", new_folder_name)
	#input()
	new_folder_path = os.path.join(dest_fold, new_folder_name)
	#print("New folder path: ", new_folder_path)
	os.makedirs(new_folder_path)
	if not os.path.exists(new_folder_path):
		print("ERROR: Creation Failed!")
		winsound.Beep(tone_frequency, duration)
		break
	else:
		copytree(src_fold, new_folder_path)
		print("Backed up in ", new_folder_path, ". Wait ", autosave_interval_seconds, " seconds.")
	
	directories = get_autosave_directories(dest_fold)
	autosaves = get_autosave_number(directories)
	
	if autosaves > autosaves_max:
		directories.sort()
		while get_autosave_number(directories) > autosaves_max:
			directories = get_autosave_directories(dest_fold)
			delete_path = os.path.join(dest_fold, directories[0])
			if bool_ask:
				winsound.Beep(tone_frequency, duration)
				print("To delete: ", delete_path, ". Agree? (y/n)")
				if input() == "y":
					shutil.rmtree(delete_path)
					autosaves = get_autosave_number(directories)
				else:
					print("Not deleting, continuing script.")
					break
			else:
				shutil.rmtree(delete_path)
				print("Deleted: ", delete_path)
				autosaves = get_autosave_number(directories)
	
	time.sleep(autosave_interval_seconds)

print("7d2d closed, ending script. Press Enter to exit.")
winsound.Beep(tone_frequency, duration)
input()
