from question import Question

class Exam:
    def __init__(self, duration, path, shuffle):
        self.duration = duration
        self.path_to_dir = path
        self.shuffle = shuffle
        self.exam_status = False
        self.questions = []

        self.name = None
        self.set_name(path)

    def set_name(self, path):
        """
        Sets the name of the exam. 
        """
        path_to_list = path.split("/")
        name_str = path_to_list[len(path_to_list) - 1]
        name_list = name_str.split(" ")
        name_of_exam = ""
        
        i = 0
        while i < len(name_list):
            name_of_exam += name_list[i] + "_"
            i += 1

        # you'll need to add some code here
        self.name = name_of_exam[0 : len(name_of_exam) - 1]

    def get_name(self):
        """
        Returns formatted string of exam name.
        """
        name_of_exam = self.name.upper()
        i = 0
        check = 0 
        while i < len(name_of_exam):
            if name_of_exam[i] == "_":
                check = 1
            i += 1
        if check == 1:
            str_out = ""
            change_to_whitespaces = name_of_exam.split("_")
            i = 0
            while i < len(change_to_whitespaces):
                str_out += change_to_whitespaces[i] + " "
                i += 1
            return str_out[0 : len(str_out) - 1]
        else:
            return name_of_exam.upper()
    
    def set_exam_status(self):
        '''
        Set exam_status to True only if exam has questions.
        '''
        if self.questions != []:
            self.exam_status = True
    def copy_exam(self):
        '''
        Create a new exam object using the values of this instances' values.
        '''
        # TODO: make a new exam object (call the constructor)
        new_exam = Exam(self.duration, self.path_to_dir, self.shuffle)
        

        # make a new list of questions to reassign to the attribute
        new_questions = []
        i = 0
        while i < len(self.questions):
            original_question = self.questions[i]
            # call the copy method for this question
            # TODO: (you'll need to write this instance method in Question)
            new_question = original_question.copy_question()

            # insert this into new list of questions
            new_questions.append(new_question)
            i += 1

        # TODO: assign this new question list to the new exam
        new_exam.set_questions(new_questions) 

        # return the new exam
        return new_exam


        
    
    def set_duration(self, t):
        '''
        Update duration of exam.
        Parameter:
            t: int, new duration of exam.
        '''
        if type(t) == int:
            if t > 0:
                self.duration = t


    def set_questions(self, ls):
        '''
        Verifies all questions in the exam are complete.
        Parameter:
            ls: list, list of Question objects
        Returns:
            status: bool, True if set successfully.
        '''
        if not(isinstance(ls, list)):
            return False

        if ls[len(ls) - 1].qtype != Question.END:
            print("End marker missing or invalid")
            return False
        
        elif (ls[len(ls) - 1].description != None
            or ls[len(ls) - 1].answer_options != []
            or ls[len(ls) - 1].correct_answer != None
            or ls[len(ls) - 1].marks != None):


            print("End marker missing or invalid")
            return False

        i = 0
        while i < len(ls) - 1:

            if ls[i].qtype == Question.END:
                
                print("End marker missing or invalid")
                return False
                 
            if ((ls[i].description == None)
                or (ls[i].correct_answer == None)):

                print("Description or correct answer missing")
                return False

            

            if (ls[i].qtype == Question.MULTIPLE
                or ls[i].qtype == Question.SINGLE):

                if len(ls[i].answer_options) != 4:
                    
                    print("Answer options incorrect quantity")
                    return False
            
            elif(ls[i].qtype == Question.SHORT):
                
                if ls[i].answer_options != []:

                    print("Answer options should not exist")
                    return False
                
            i += 1

        self.questions = ls
        return True
                
    def preview_exam(self):
        '''
        Returns a formatted string.
        '''
        list_questions = self.questions
        formatted_string = f"{self.get_name()}\n"
        i = 0
        while i < len(list_questions):
            formatted_string += f"{list_questions[i].preview_question(i + 1)}"\
                             + "\n\n"
            i += 1
        return formatted_string

