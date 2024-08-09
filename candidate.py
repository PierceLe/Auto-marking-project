import os
class Candidate:
    def __init__(self, sid, name, time):
        self.sid = sid
        self.name = name
        self.extra_time = time
        self.exam = None
        self.confirm_details = False
        self.results = []

    def get_duration(self):
        '''
        Returns total duration of exam.
        '''
        return self.extra_time + self.exam.duration
            
    def edit_sid(self, sid):
        '''
        Update attribute sid
        '''
        # int_of_sid is an int of sid
        int_of_sid: int = int(sid)
        # use conditional statement to check
        if (isinstance(sid, str) and len(sid) == 9 and int_of_sid > 0):
            self.sid = sid
    
    def edit_extra_time(self, t):
        '''
        Update attribute extra_time
        '''
        if isinstance(t, int) and t > 0:
            self.extra_time = t

    def set_confirm_details(self, sid, name):
        '''
        Update attribute confim_details
        '''
        if self.sid == sid and self.name == name:
            self.confirm_details = True
        else:
            self.confirm_details = False
        return self.confirm_details

    def log_attempt(self, data):
        '''
        Save data into candidate's file in Submissions.
        '''
        path_to_directory: str = self.exam.path_to_dir
        path_to_folder: str = path_to_directory + "/submissions"
        # check the exist of folder, if not, create folder
        if not (os.path.exists(path_to_folder)):
            os.mkdir(path_to_folder)

        sid_of_students: str = self.sid
        file_students_name: str = sid_of_students + ".txt"
        fobj = open(path_to_folder + "/" + file_students_name, "w")
        fobj.write(data)
        fobj.close()
    
    def set_results(self, ls):
        '''
        Update attribute results if confirm_details are True
        '''
        if self.confirm_details == True:
            self.results = ls
        return self.results

    def do_exam(self, preview = True):
        '''
        Display exam and get candidate response from terminal during the exam.
        '''
        if preview == True:
            formatted_string: str = f"Candidate: {self.name}({self.sid})\n"\
                                    +f"Exam duration: {self.get_duration()} minutes\n"\
                                    +f"You have {self.get_duration()} minutes to complete the exam.\n"
            

            preview_exam_list: list = self.exam.preview_exam().split("\n")
            index_preview: int = 0
            preview_exam_str: str = ""
            question_number: int = 1
            while index_preview < len(preview_exam_list):
                if preview_exam_list[index_preview].startswith("Expected Answer:") == True:
                    preview_exam_list[index_preview] = f"Response for Question {question_number}: "
                    question_number += 1
                index_preview += 1
            index_preview = 0
            while index_preview < len(preview_exam_list):
                preview_exam_str += preview_exam_list[index_preview] + "\n"
                index_preview += 1
            do_exam_string = formatted_string + preview_exam_str
            print(do_exam_string[0 : len(do_exam_string) - 3])

        elif(preview == False):
            formatted_string: str = f"Candidate: {self.name}({self.sid})\n"\
                                    +f"Exam duration: {self.get_duration()} minutes\n"\
                                    +f"You have {self.get_duration()} minutes to complete the exam."
            print(formatted_string)
            preview_exam_list: list = self.exam.preview_exam().split("\n")
            index_preview: int = 0
            question_number: int = 1
            list_of_questions: list = self.exam.questions
            index_questions = 0
            preview: str = ""
            while index_preview < len(preview_exam_list):
                if preview_exam_list[index_preview].startswith("Expected Answer:") == True:
                    response = input(f"Response for Question {question_number}: ")
                    preview += f"Response for Question {question_number}: " + response + "\n"
                    preview += "You have scored " + str('{0:.2f}'.format(list_of_questions[index_questions].mark_response(response))) + " marks.\n"
                    index_questions += 1
                    question_number += 1
                elif preview_exam_list[index_preview].startswith("-End-"):
                    print(preview_exam_list[index_preview])
                    preview += preview_exam_list[index_preview] + "\n"
                    break
                else:
                    print(preview_exam_list[index_preview])
                    if index_preview != 0:
                        preview += preview_exam_list[index_preview] +"\n"
                index_preview += 1
            self.log_attempt(preview)



    def __str__(self):
        name = f"Candidate: {self.name}({self.sid})\n"
        t = self.set_duration()
        duration = f"Exam duration: {t} minutes\n"
        duration += "You have " + str(t) + " minutes to complete the exam.\n"
        if self.exam == None:
            exam = f"Exam preview: \nNone\n"
        else:
            exam = self.exam.preview_exam()
        str_out = name + duration + exam
        return str_out

