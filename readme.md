# deleteTempFile.py

# Language used:
Python 3.11.2
Runs on your Python interpreter.
Made executable with pyinstaller
You can use the executable named deleteTempFile.exe

# About the program:
This script allows you to clean the temporary folders on your system, including the logged-in user's local Temp folder and the Windows Temp folder. It deletes files and folders within these directories, freeing up disk space.
pyinstaller --onefile deleteTempFile.py

# Functions:

# main:

    The main function calls the other two functions (clean_windows_temp_folder && clean_local_temp_folder).
    A waiting time of 60 seconds is added for the user to review the deleted files.

# clean_local_temp_folder:

    Gets the path to the local user's Temp folder using the LOCALAPPDATA environment variable.
    Iterates through the directory structure within the Temp folder using os.walk().
    Deletes files within each directory using os.remove().
    Deletes subfolders within each directory using shutil.rmtree().
    Counts the number of deleted files and folders and displays a message for each deleted file or folder.
    Shows the total number of deleted files and folders.
    clean_windows_temp_folder()
    This function cleans the Windows Temp folder. It performs similar actions to the clean_local_temp_folder function but specifically for the Windows Temp folder located at C:\Windows\Temp.

# clean_windows_temp_folder:

    Sets the path of the Windows Temp folder as C:\Windows\Temp.
    Uses os.walk() to recursively iterate through the directory structure within the Windows Temp folder.
    The topdown=False argument is provided to ensure that files and folders are processed from bottom to top, allowing files to be deleted before folders.
    The outer loop iterates through each directory within the Windows Temp folder.
    The inner loop iterates through the files within each directory.
    Attempts to delete each found file using os.remove().
    If a PermissionError occurs (permission error), the except block is triggered, and the exception is ignored with the pass command.
    Attempts to delete each found folder using shutil.rmtree().
    If a PermissionError occurs (permission error), the except block is triggered, and the exception is ignored with the pass command.
    If any other exception occurs during the execution of the function, it is caught by the except Exception as block, and an error message is printed.

# Notes:

Some files or folders within the Temp folders may be in use by other processes and cannot be deleted until those processes are terminated. Make sure no critical process is using these files before running this script.

