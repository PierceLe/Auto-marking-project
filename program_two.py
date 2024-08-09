'''
Interface of the exam
'''
import os
import exam
import setup
import program_one

def assign_exam(obj_exam):
    try:
        path_to_directory: str = obj_exam.path_to_dir
        path_to_csv: str = path_to_directory + "/students.csv"
        fobj = open(path_to_csv, "r")
    except:
        return None
    list_of_candidates: list = setup.extract_students(fobj)
    if list_of_candidates == []:
        print("No candidates found in the file")
        return None
    elif obj_exam.shuffle == False:
        print("Assigning exam to candidates...")
        i = 0
        while i < len(list_of_candidates):
            exam_for_each_student = obj_exam.copy_exam()
            list_of_candidates[i].exam = exam_for_each_student
            i += 1
        print(f"Complete. Exam allocated to {len(list_of_candidates)} candidates.")
        return list_of_candidates

    elif obj_exam.shuffle == True:
        print("Assigning exam to candidates...")
        i = 0
        while i < len(list_of_candidates):
            # copying a new object exam
            exam_for_each_student = obj_exam.copy_exam()
            list_of_questions = exam_for_each_student.questions
            j = 0 
            while j < len(list_of_questions):
                list_of_questions[j].shuffle_answers()
                j += 1
            exam_for_each_student.set_questions(list_of_questions)
            list_of_candidates[i].exam = exam_for_each_student
            i += 1
        print(f"Complete. Exam allocated to {len(list_of_candidates)} candidates.")
        return list_of_candidates
        
def main(args):
    commandline: tuple = program_one.parse_cmd_args(args)
    if commandline != None:
        exam_obj = program_one.main(args)
        if exam_obj != None:
            list_of_candidates: list = assign_exam(exam_obj)
            while True:
                actions: str = input("Enter SID to preview student's exam (-q to quit): ")
                if actions == "-q":
                    return list_of_candidates
                elif actions == "-a":
                    i = 0
                    while i < len(list_of_candidates):
                        list_of_candidates[i].do_exam()
                        print("")
                        i += 1
                elif not isinstance(actions, str):
                    print("SID is invalid.")
                    print("")
                elif len(actions) != 9:
                    print("SID is invalid.")
                    print("")
                elif int(actions) <= 0:
                    print("SID is invalid.")
                    print("")
                else:
                    i = 0
                    finding: int = 0
                    while i < len(list_of_candidates):
                        if list_of_candidates[i].sid == actions:
                            list_of_candidates[i].do_exam()
                            print("")
                        elif list_of_candidates[i].sid != actions:
                            finding += 1
                        i += 1
                    if finding == len(list_of_candidates):
                        print("SID not found in list of candidates.")
                        print("")
        elif exam_obj == None:
            return 1
    elif commandline == None:
        return 1


if __name__ == "__main__":
    main(sys.argv)
