'''
Interface of the exam
'''
import setup
import sys
import os
from exam import Exam

def parse_cmd_args(args):
    '''
    Parameters:
        args: list, command line arguments
    Returns:
        result: None|tuple, details of the exam

    >>> parse_cmd_args(['program.py', '/home/info1110/', '60', '-r'])
    ('/home/info1110/', 60, True)

    >>> parse_cmd_args(['program.py', '/home/info1110/', 'ab', '-r'])
    Duration must be an integer

    >>> parse_cmd_args(['program.py', '/home/info1110/'])
    Check command line arguments
    '''
    list_of_commandline: list = args
    if len(list_of_commandline)  < 3:
        print("Check command line arguments")
        return None
    elif list_of_commandline[2].isdigit() == False:
        print("Duration must be an integer")
        return None
    elif len(list_of_commandline) >= 4 and list_of_commandline[3] == "-r":
        return (list_of_commandline[1], int(list_of_commandline[2]), True)
    elif len(list_of_commandline) != 4:
        return (list_of_commandline[1], int(list_of_commandline[2]), False)

def setup_exam(obj):
    '''
    Update exam object with question contents extracted from file 
    Parameter:
        obj: Exam object
    Returns:
        (obj, status): tuple containing updated Exam object and status
        where status: bool, True if exam is setup successfully. Otherwise, False.
    '''
    directory_path: str  = obj.path_to_dir
    fobj: str = directory_path + "/questions.txt"
    duration: int = obj.duration
    list_of_question_object: list = setup.extract_questions(open(fobj))

    # set name for obj
    obj.set_name(directory_path)

    # set questions
    obj.set_questions(list_of_question_object)

    # set exam status
    obj.set_exam_status()

    # set duration
    obj.set_duration(duration)

    # Return tuple containing updated
    # Exam object and status
    if obj.exam_status:
        return obj, True
    else:
        return obj, False

def main(args):
    '''
    Implement all stages of exam process.
    '''
    # commandline is a tuple have three
    # variables, which is path to directory,
    # duration and boolen for shuffle or not
    commandline: tuple = parse_cmd_args(args)
    if commandline != None:
        path: str = commandline[0] # path to directory

        #list_of_file is a list that each element in a list
        # is a file that have in a directory
        try:
            list_of_file = os.listdir(path)
        except FileNotFoundError:
            print("Missing files")
            return 
        the_duration: int = commandline[1] # the duration of the exam
        shuffle_mode: bool = commandline[2] # the shuffle mode is a boolen

        # create an exam object 
        exam_obj = Exam(the_duration, path, shuffle_mode)
        if (os.path.exists(path + "/questions.txt")) == False or (os.path.exists(path + "/students.csv")) == False:
            print("Missing files")
            return None 

        else:
            print("Setting up exam...")
            # set up exam is a tuple that have two elements,
            # updated exam object and status
            set_up_exam: tuple = setup_exam(exam_obj)
            if set_up_exam[1]:
                print("Exam is ready...")
                while True:
                    options = input("Do you want to preview the exam [Y|N]? ")
                    if options.lower() != "y" and options.lower() != "n":
                        print("Invalid command.")
                    elif options.lower() == "n":
                        return exam_obj
                        break
                    elif options.lower() == "y":
                        print(exam_obj.preview_exam(), end = "")
            else:
                print("Error setting up exam")
                return None
                    
    
if __name__ == "__main__":
    '''
    DO NOT REMOVE
    '''
    main(sys.argv)
