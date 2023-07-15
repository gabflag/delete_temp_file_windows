import os
import shutil
import time


def clean_windows_temp_folder():
    '''
    Delete files from folder C:/Windows/Temp
    '''
    windows_temp_path = r'C:\Windows\Temp'
    try:
        deleted_files = 0
        deleted_folders = 0

        for root, dirs, files in os.walk(windows_temp_path, topdown=False):
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    deleted_files += 1
                    print(f"Deleted file: {file_path}")
                except PermissionError:
                    pass

            for folder in dirs:
                try:
                    folder_path = os.path.join(root, folder)
                    shutil.rmtree(folder_path)
                    deleted_folders += 1
                    print(f"Deleted folder: {folder_path}")
                except PermissionError:
                    pass

        print(f"Total files deleted: {deleted_files}")
        print(f"Total folders deleted: {deleted_folders}")
    except Exception as e:
        print("An error occurred while cleaning the Windows Temp folder: " +
              f"{str(e)}")


def clean_local_temp_folder():
    '''
    teste C:/Users/LoggedUser/AppData/Local/Temp
    '''
    temp_path = os.path.join(os.environ.get('LOCALAPPDATA'), 'Temp')
    try:
        deleted_files = 0
        deleted_folders = 0

        for root, dirs, files in os.walk(temp_path, topdown=False):
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    deleted_files += 1
                    print(f"Deleted file: {file_path}")
                except PermissionError:
                    pass

            for folder in dirs:
                try:
                    folder_path = os.path.join(root, folder)
                    shutil.rmtree(folder_path)
                    deleted_folders += 1
                    print(f"Deleted folder: {folder_path}")
                except PermissionError:
                    pass

        print(f"Total files deleted: {deleted_files}")
        print(f"Total folders deleted: {deleted_folders}")
    except Exception as e:
        print("An error occurred while" +
              f"cleaning the local Temp folder: {str(e)}")


def main():
    clean_local_temp_folder()
    clean_windows_temp_folder()
    time.sleep(60)


main()
