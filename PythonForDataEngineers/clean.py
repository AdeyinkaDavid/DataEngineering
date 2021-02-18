import os

#This class is used to extract the file from our Filepath and then save it int a class 
class File_saver: 
    current_path = os.path.abspath('Cleaner.py')
    curr = os.getcwd() #getcwd is an example of a method within a function
    Base_dir= os.path.dirname(current_path)

    #Code to create a folder
    def clean_folder(self,filename="clean_data"):
        clean_path = os.path.join(Base_dir,dirname)