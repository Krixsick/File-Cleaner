import os, shutil, send2trash, pprint, time, re
from datetime import datetime, date


download_directory = 'C:\\Users\\flame\\Downloads'
desktop_directory = 'C:\\Users\\flame\\Desktop'
folder_PNG = 'C:\\Users\\flame\\Desktop\\Folder PNG'
folder_PDF = 'C:\\Users\\flame\\Desktop\\Folder PDF'
folder_DOCX = 'C:\\Users\\flame\\Desktop\\Folder DOCX'
folder_TRASH = 'C:\\Users\\flame\\Desktop\\Folder Trash'
pp = pprint.PrettyPrinter(indent=1)

def display_download_files(): #1
    """Changes directory to the download folder and prints out all the files and folders
    within that download directory"""
    move_file = 0
    os.chdir(download_directory) 
    pp.pprint(os.listdir(download_directory))
    while move_file not in ('y', 'n'):
        move_file = input("Would you like to move the files/folders in the download directory? (y/n): ").lower()
    if move_file == 'y':
        move_download_files()
    
def pdf_regex(file):
    """periods matches any character except newline character and you need a \ to search for
    metacharacters which a period is.""" 
    os.chdir(download_directory)
    """Checks whether the end of the files contain the types below in the tuple"""
    types = (".+\.pdf$", ".+\.PDF$", ".+\.png$", ".+\.PNG$", ".+\.docx$", ".+\.DOCX$")
    for each_type in types:
        #Checks to see if they match with any of the types in the tuple
        general_type_pattern = re.compile(r'{0}'.format(each_type))
        general_matches = general_type_pattern.finditer(file)
        """Sorts the files accordingly below from seeing which specific type
        of file it is and moves them to their own respective directory"""
        for item in general_matches:
            if item.group(0)[-4:] == ".png" or item.group(0)[-4:] == ".PNG":
                shutil.move(item.group(0), folder_PNG)
            elif item.group(0)[-4:] == ".pdf" or item.group(0)[-4:] == ".PDF":
                shutil.move(item.group(0), folder_PDF)
            elif item.group(0)[-5:] == ".docx" or item.group(0)[-5:] == ".DOCX":
                shutil.move(item.group(0), folder_DOCX)



def move_download_files(): #4 
    for item in os.listdir(download_directory):
        pdf_regex(item)

def create_appropriate_directories(): #2
    folder_png = False
    folder_docx = False
    folder_pdf = False
    folder_trash = False
    #changes directory to desktop
    os.chdir(desktop_directory)
    """For every file inside the desktop directory, it checks whether there is a
    folder of a PNG, TXT, and PDF within that directory, if not it creates one."""
    desktop_files = os.listdir(desktop_directory)
    for file in desktop_files:
        if file in ('Folder PNG', 'Folder DOCX', 'Folder PDF'):
            if file == 'Folder PNG':
                folder_png = True
            elif file == 'Folder DOCX':
                folder_docx = True
            elif file == 'Folder PDF':
                folder_pdf = True
            elif file == "Folder Trash":
                folder_trash = True
    #Creates the directories
    if folder_pdf == False:
        os.makedirs(desktop_directory + '\\Folder PDF')
    if folder_docx == False:
        os.makedirs(desktop_directory + '\\Folder DOCX')
    if folder_png == False:
        os.makedirs(desktop_directory + '\\Folder PNG')
    if folder_trash == False:
        os.makedirs(desktop_directory + "\\Folder Trash")


def show_specific_directory(specific_directory):  #3
    """Prints out the content inside the files. If nothing is inside it will print nothing, otherwise it will print all the files
    inside the specified directory"""
    if specific_directory in ('Folder PNG', 'Folder DOCX', 'Folder PDF'):
        if os.listdir(desktop_directory + '\\' + specific_directory) == []:
            print("The " + str(specific_directory) + " is empty.")
        else:
            print(os.listdir(desktop_directory + '\\' + specific_directory))
        

def move_sortedfiles_to_trash(specific_directory, file_name): #5
    confirmation_to_move_file = 0
    """Changed directory to the one provided in the arguments and checks the files inside that directory to see if the file
    the user had provided in their arguments are inside the directory they provided"""
    os.chdir(desktop_directory + "\\" + specific_directory) 
    if file_name in os.listdir():
        print("File {0} is found".format(file_name))
        while confirmation_to_move_file not in ('y', 'n'):
            confirmation_to_move_file = input("Would you like to move this file in to the Folder Trash directory? (y/n): ").lower()
        if confirmation_to_move_file == 'y':
            #moves the file the user provided in the Folder Trash
            shutil.move(file_name, folder_TRASH)
        elif confirmation_to_move_file == 'n':
            print("Did not move file.")
    else:
        print("File could not be located, please double check the name")



def delete_sortedfiles(): # 6
    os.chdir(folder_TRASH)
    for file in os.listdir():
        send2trash.send2trash(file)

def show_recent_files(specific_directory):
    os.chdir(desktop_directory)
    creation_time_for_files = {}
    """os.path.getctime gets the time of the directory or file we want"""
    for file in os.listdir(specific_directory):
        """creation_time gets the creation time of the files of where it was first created and the creation_time_human_readable is used to turn the time obtained
        from creation_time and format it into readable text for the user to observe."""
        creation_time = os.path.getctime(desktop_directory + "\\" + specific_directory + "\\" + file)
        creation_time_human_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(creation_time))
        creation_time_for_files[creation_time_human_readable] = file
    sorted_files = sorted(creation_time_for_files.items())
    for key, value in sorted_files:
        print("Creation Time: {0}, File Name: {1}".format(key, value))





    

        
           
       
