# 7D2D-Autosave

HOW TO USE

0. Install latest Python 3 version
1. Don't even use if you're not comfortable having a script automatically delete things! Some computer / programming knowledge recommended, don't use if you have no idea what this script is even doing.
2. change src_fold to the folder where the 7 Days to Die savegames are located on your computer while keeping the format of the path, i.e.:
src_fold = os.path.join("C:\\", "Users", "Kenira", "AppData", "Roaming", "7DaysToDie")
3. Create a new folder on a drive to save the autosaves, and change dest_fold to that path, i.e.:
dest_fold = os.path.join("E:\\", "bak", "7 Days To Die", "_Python")
4. If you want to make the script ask you before deleting everytime and also show you what it will delete, change "bool_ask = False" to "bool_ask = True"
5. choose how frequent you want your autosaves in seconds and change autosave_interval_seconds accordingly
6. Start 7 Days to Die, then start the script. The script will detect when 7 Days to Die is no longer running and will automatically stop.
