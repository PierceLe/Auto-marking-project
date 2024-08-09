import random

class Question:
    SINGLE: str = "single"
    MULTIPLE: str = "multiple"
    SHORT: str = "short"
    END: str = "end"
    ALLOWED_OPTIONS: list = ["A", "B", "C", "D"]

    def __init__(self, qtype):
        # you'll need to check if qtype is valid before assigning it
        self.qtype = None
        self.set_type(qtype)
        # attribute 
        self.description = None

        self.answer_options = []

        self.correct_answer = None
        
        self.marks = None
       
    def set_type(self, update_qtype):
        """
        Update instance variable qtype.
        """
        if (update_qtype == Question.SINGLE 
            or update_qtype == Question.MULTIPLE 
            or update_qtype == Question.SHORT 
            or update_qtype == Question.END):

            self.qtype = update_qtype
            return True
        else:
            return False
    
    def set_description(self, update_desc: str):
        """
        Update instance variable description.
        """
        if self.qtype == Question.END:
            return False

        elif isinstance(update_desc, str) and update_desc != "":
            self.description = update_desc
            return True 
        else:
            return False
    
    def set_correct_answer(self, ans):
        """
        Update instance variable correct_answer.
        """

        if not isinstance(ans, str):
            return False

        elif self.qtype == Question.SINGLE:
            if (ans == "A"
                or ans == "B"
                or ans == "C"
                or ans == "D"):
                
                self.correct_answer = ans
                return True
            else:
                return False
        
        elif self.qtype == Question.MULTIPLE:
            # For each answer, loop through allowed options
            # check if the answer is one of them
            # if not, return false
            answers_split = ans.split(",")
            i: int = 0 # the index of the answers 
            j: int = 0 # the index of the allowed options 
            check = 0
            while i < len(answers_split):
                while j < len(Question.ALLOWED_OPTIONS):
                    if (answers_split[i].strip() == Question.ALLOWED_OPTIONS[j]):
                        check += 1
                        break
                    j += 1
                i += 1
            if check == len(answers_split):
                self.correct_answer = ans
                return True

            else:
                return False
        
        elif self.qtype == Question.SHORT:
            self.correct_answer = ans
            return True               
    
    def set_marks(self, num):
        """
        Update instance variable marks.
        """
        if isinstance(num, int) and num >= 0:
            self.marks = num
            return True
        else:
            return False
    
    def set_answer_options(self, opts):
        """
        Update instance variable answer_options.

        opts should have all flags equal to False when passed in.
        This method will update the flags based on the correct answer.
        Only then do we check that the number of correct answers is correct.
        """
        
        # using conditional statement to check the question type, 
        # if question type is short or end,
        # opts will be assigned to the attribute 
        if self.qtype == Question.SHORT or self.qtype == Question.END:
            self.answer_options = opts
            return True

        # check the format of opts, opts have to be a list and the length of 
        # opts is exactly 4. If not, the agrument opts will not assign 
        #to the attribute and return False
        elif ((not isinstance(opts, list)) 
                or (len(opts) != 4)):

            return False

        i = 0  #the index of the opts

        # create the loop to check each element in opts is a tuple or not and 
        # the length of each element have to be 2. If not, he agrument opts 
        # will not assign to the attribute and return False
        while i < len(opts):
            if (not isinstance(opts[i], tuple)
                or len(opts[i]) != 2):

                return False

            # check the type of each element in each tuple. The first element
            # in each tuple have to be a string and start with A. or B. or C. or D. 
            # and have to have the order from A to D and the second element in each 
            # tuple have to be a boolen and first all of such are False. 
            # If not, return False
            if (opts[i][0][0 : 2] != Question.ALLOWED_OPTIONS[i] + "."
                or opts[i][1] != False):

                    return False
            i += 1
            
        j = 0
        new_answer_options: list = []
        while j < len(opts):
            change_to_list: list = list(opts[j])
            new_answer_options.append(change_to_list)
            j += 1

        if self.correct_answer == None:
            return False

        multiple_answer: list = self.correct_answer.split(",")

        if ((not (self.qtype == Question.SINGLE and len(multiple_answer) == 1)) 
             and (not (self.qtype == Question.MULTIPLE and len(multiple_answer) >= 1))):
            
            return False 

        k = 0 
        while k < len(multiple_answer):

            if multiple_answer[k].strip() == "A":
                new_answer_options[0][1] = True
            elif multiple_answer[k].strip() == "B":
                new_answer_options[1][1] = True
            elif multiple_answer[k].strip() == "C":
                new_answer_options[2][1] = True
            elif multiple_answer[k].strip() == "D":
                new_answer_options[3][1] = True
            k += 1
        f = 0
        while f < len(new_answer_options):
            new_answer_options[f]: tuple = tuple(new_answer_options[f])
            f += 1
        opts: list = new_answer_options
        self.answer_options = opts
        return True

    def get_answer_option_descriptions(self):
        """
        Returns formatted string listing each answer description on a new line.
        Example:
        A. Answer description
        B. Answer description
        C. Answer description
        D. Answer description
        """
        str_out: str = "" # create a string that list each answer description

        if self.qtype == Question.END or self.qtype == Question.SHORT:
            return str_out
            
        all_answer: list = self.answer_options
        i = 0 # the index of all_answer
        while i < len(all_answer):
            str_out += all_answer[i][0]
            
            if i != len(all_answer) - 1:
                str_out += "\n"
            i += 1
        return str_out

    def mark_response(self, response):
        """
        Check if response matches the expected answer
        Parameter:
            response: str, response provided by candidate
        Returns:
            marks: int|float, marks awarded for the response.
        """
        if self.qtype == Question.END:
            return None
        elif self.qtype == Question.SHORT or self.qtype == Question.SINGLE:
            if response == self.correct_answer:
                return self.marks
            else:
                return 0
        elif self.qtype == Question.MULTIPLE:
            correct_answer: str = self.correct_answer
            list_of_correct_answer: list = correct_answer.split(",")
            i = 0
            while i < len(list_of_correct_answer):
                list_of_correct_answer[i] = list_of_correct_answer[i].strip()
                i += 1

            list_of_responses = response.split(",")
            list_of_responses.sort()
            new_response: list = []
            new_response.append(list_of_responses[0].strip())
            i = 1
            while i < len(list_of_responses):
                list_of_responses[i] = list_of_responses[i].strip()
                if list_of_responses[i] != list_of_responses[i - 1].strip():
                    new_response.append(list_of_responses[i])
                i += 1
            i = 0
            total_marks = self.marks
            correct_answer = 0
            while i < len(new_response):
                j = 0
                while j < len(list_of_correct_answer):
                    if new_response[i] == list_of_correct_answer[j]:
                        correct_answer += 1
                        break
                    j += 1
                i += 1
            marks: float = total_marks * (correct_answer / len(list_of_correct_answer))
            return marks
        
        
        
        pass

    def preview_question(self, i=0, show=True):
        """
        Returns formatted string showing details of question.
        Parameters:
            i: int, placeholder for question number, DEFAULT = 0
            show: bool, True to show Expected Answers, DEFAULT = TRUE
        """
        question: int = i # the question number
        if i == 0:
            question = "X"

        # Formatted string showing details of question.
        formatted_string: str = None

        marks = self.marks
        answer: str = "Answer"
        if self.qtype == Question.END:
            formatted_string = "-End-"
            return formatted_string
            

        if self.qtype == Question.MULTIPLE:
            answer = "Answers"

        formatted_string = f"Question {question} - {self.qtype.capitalize()} {answer}[{marks}]\n"\
                         + f"{self.description}\n"\
                         + f"{self.get_answer_option_descriptions()}"

        if self.qtype != Question.SHORT:
            formatted_string += "\n"
        
                         
        if show:
           formatted_string += f"Expected Answer: {self.correct_answer}"

        return formatted_string

    @classmethod
    def generate_order(cls):
        """
        Returns a list of 4 integers between 0 and 3 inclusive to determine order.

        Sample usage:
        >>> generate_order()
            [3,1,0,2]
        """
        list_of_random_number: list = [] # a list of 4 integers between 0 and 3
        random_first_number: int = random.randint(0, 3)
        list_of_random_number.append(random_first_number)

        random_second_number: int = random.randint(0, 3)
        while True:
            if random_second_number != random_first_number:

                list_of_random_number.append(random_second_number)
                break
            else:
                random_second_number = random.randint(0, 3)

        random_third_number: int = random.randint(0, 3)
        while True:
            if (random_third_number != random_first_number
                and random_third_number != random_second_number):

                list_of_random_number.append(random_third_number)
                break
            else:
                random_third_number = random.randint(0, 3)

        random_fourth_number: int = random.randint(0, 3)
        while True:
            if (random_fourth_number != random_first_number
                and random_fourth_number != random_second_number
                and random_fourth_number != random_third_number):

                list_of_random_number.append(random_fourth_number)
                break
            else:
                random_fourth_number = random.randint(0, 3)
        return list_of_random_number
    def copy_question(self):
        """
        copying the exam object
        """
        # create a new object that will be the same of the exam object
        new_question = Question(self.qtype)
        new_question.set_description(self.description)
        new_question.set_correct_answer(self.correct_answer)
        new_question.answer_options = self.answer_options
        new_question.set_marks(self.marks)

        return new_question



    def shuffle_answers(self):
        """
        Updates answer options with shuffled elements.
        Must call generate_order only once.
        """
        # check the question type
        if (self.qtype == Question.SINGLE
            or self.qtype == Question.MULTIPLE):

            #a list before being shuffled
            list_with_order: list = self.answer_options

            k = 0 # i Use left and right arrow keys to adjust the split region size
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
ndex of list_with_order

            # create a list after being shuffled
            new_list_without_order: list = []
            order = self.generate_order()
            while k < len(list_with_order):
                new_list_without_order.append(list_with_order[order[k]])
                k += 1
            i = 0
            true_order: list = ["A", "B", "C", "D"]
            ls = []
            while i < len(new_list_without_order):
                change_to_list: list = list(new_list_without_order[i])
                ls.append(change_to_list)
                i += 1
            j = 0
            ls2 = []
            while j < len(ls):
                change = ls[j][0].split(".")
                change[0] = true_order[j]
                ls2.append(change[0] + "." + change[1])
                j += 1

            k = 0
            while k < len(ls):
                ls[k][0] = ls2[k]
                k += 1
            m = 0
            while m < len(ls):
                ls[m] = tuple(ls[m])
                m += 1
            self.answer_options = ls
            v = 0
            str_out = ""
            list_of_answer =[]
            while v < len(ls):
                if ls[v][1] == True:
                    list_of_answer = ls[v][0].split(".")
                    str_out += list_of_answer[0] + ", "
                v += 1
            
            self.set_answer_options(ls)
            self.set_correct_answer(str_out[0 : len(str_out) - 2])
            return(self.answer_options)

    def __str__(self):
        '''
        You are free to change this, this is here for your convenience.
        When you print a question, it'll print this string.
        '''
        return f'''Question {self.__hash__()}:
        Type: {self.qtype}
        Description: {self.description}
        Possible Answers: {self.get_answer_option_descriptions()}
        Correct answer: {self.correct_answer}
        Marks: {self.marks}
        '''

def main():
    # DECLARE QUESTION 2:
    question_2 = Question("multiple")
    # set attribute for question 2
    # set type for question 2
    question_2.set_type("multiple")
    # declare a string variable, which is the description of question 2
    description_2: str = "Which of following brands is not primarily known for producing sneakers?"
    # set description for question 2
    question_2.set_description(description_2)
    # declare a string variable, which is the answer of question 2
    answer_2: str = "A, C"
    # set correct answer for question 2
    question_2.set_correct_answer(answer_2)

    # declare an integer variable, which is the mark of question 2
    marks_2: int = 3
    # set marks for question 2
    question_2.set_marks(marks_2)

    # declare a list, which each element in list is a tuple with two elements.
    # the first element is the answer option and the second one is a boolean
    # with default variable is False.
    answer_options_2: list = [("A. Apple", False), ("B. Nike", False), ("C. Samsung", False), ("D. Adidas", False)]
    # set answer options for question
    question_2.set_answer_options(answer_options_2)
    

    print(question_2.mark_response("C, C"))

if __name__ == "__main__":
    main()

