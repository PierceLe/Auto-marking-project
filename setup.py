'''
Functions to setup the exam questions and candidate list for the exam.
'''
# please do not change or add another import
import question
import candidate
import io


def extract_questions(fobj: io.TextIOWrapper)->list:
    """
    Parses fobj to extract details of each question found in the file.
    General procedure to extract question.
    1. Extract the following
        - type
        - question details (description)
        - possible answers (if any)
        - expected answer
        - marks
        (you shouldn't need to perform error handling on these details,
        this is handled in the next step) .
    2. You'll need to convert the possible answers (if any) to a list of tuples (see 
       "Section 1. Setup the exam - Question" for more details). All flags can be False.
    3. Create a question object and call the instance methods to set the
       attributes. This will handle the error handling.
    4. Repeat Steps 1-3 for the next question until there are no more questions.
    5. You will need to create an end question as well.
    6. Create the list for all your questions and return it.

    Parameter:
        fobj: open file object in read mode
    Returns:
        result: list of Question objects.
    """
    all_questions = []
    all_lines: list = []
    all_lines = fobj.readlines()

    each_question = []
    i = 0
    while i < len(all_lines):
        line_stripped = all_lines[i].strip("\n")
        if line_stripped != "":
            each_question.append(line_stripped)
        if all_lines[i].startswith("Marks"):
            all_questions.append(convert_to_question(each_question))
            each_question = []

        i += 1
    # create end question
    ends = question.Question("end")
    all_questions.append(ends)
    return all_questions

def convert_to_question(list_of_question: list):
    '''
    this function will convert a question in string to a question object
    and will return it.
    '''
    # set type of question
    type_of_question = list_of_question[0].split("-")
    type_of_question = type_of_question[1].strip().lower()
    questions = question.Question(type_of_question)
    type_of_questions_valid: bool = questions.set_type(type_of_question)
    if not type_of_question:
        return questions
    elif type_of_question:

        # split the description and possible answser to 2 different lists
        i = 1
        description: str = ""
        possible_answer = []
        control_type_question = False
        while i < len(list_of_question):
            if list_of_question[i].startswith("Possible"):
                break
            elif list_of_question[i].startswith("Expected"):
                control_type_question = True
                break
            description += f"{list_of_question[i]}" + "\n"
            i += 1
        i += 1
        while i < len(list_of_question):
            if control_type_question:
                possible_answer = []
                break
            elif list_of_question[i].startswith("Expected"):
                break
            possible_answer.append(list_of_question[i])
            i += 1
        
        # set description for questions
        questions.set_description(description[0 : len(description) - 1])


        correct_answer: str = ""
        correct_answer = list_of_question[len(list_of_question) - 2]
        correct_answer = correct_answer.split(":")
        correct_answer = correct_answer[1].strip()
        # set correct answer for questions
        questions.set_correct_answer(correct_answer)

        # set answer options for questions
        i = 0
        default_boolean = False
        answer_options: tuple = ()
        opt: list =[]
        while i < len(possible_answer):
            answer_options = (possible_answer[i], default_boolean)
            opt.append(answer_options)
            i += 1
        
        questions.set_answer_options(opt)


            


        marks: str = ""
        marks = list_of_question[len(list_of_question) - 1]
        marks = marks.split(":")
        marks = marks[1].strip()
        marks = int(marks)

        # set marks for questions
        questions.set_marks(marks)

        return questions

def sort(to_sort: list, order: int=0)->list:
    """
    Sorts to_sort depending on settings of order.

    Parameters:
        to_sort: list, list to be sorted.
        order: int, 0 - no sort, 1 - ascending, 2 - descending
    Returns
        result: list, sorted results.

    Sample usage:
    >>> to_sort = [(1.50, "orange"), (1.02, "apples"), (10.40, "strawberries")]
    >>> print("Sort 0:", sort(to_sort, 0))
    Sort 0: [(1.5, 'orange'), (1.02, 'apples'), (10.4, 'strawberries')]
    >>> print("Sort 1:", sort(to_sort, 1))
    Sort 1: [(1.02, 'apples'), (1.5, 'orange'), (10.4, 'strawberries')]
    >>> print("Sort 2:", sort(to_sort, 2))
    Sort 2: [(10.4, 'strawberries'), (1.5, 'orange'), (1.02, 'apples')]
    >>> to_sort = [ "oranges", "apples", "strawberries"]
    >>> print("Sort 0:", sort(to_sort, 0))
    Sort 0: ['oranges', 'apples', 'strawberries']
    >>> print("Sort 1:", sort(to_sort, 1))
    Sort 1: ['apples', 'oranges', 'strawberries']
    >>> print("Sort 2:", sort(to_sort, 2))
    Sort 2: ['strawberries', 'oranges', 'apples']
    """
    if not isinstance(to_sort, list):
        return []
    elif order > 2 or order <= 0:
        return to_sort
    elif order == 1:
        if isinstance(to_sort[0], str):
            length: int = len(to_sort)
            list_after_sort = []
            while True:
                i = 0
                store_index_i: int
                max_of_list = to_sort[0]
                while i < len(to_sort):
                    if to_sort[i] >= max_of_list:
                        max_of_list = to_sort[i]
                        store_index_i = i
                    i += 1
                list_after_sort.append(to_sort[store_index_i])
                to_sort.remove(to_sort[store_index_i])
                if len(list_after_sort) == length:
                    break
            return list_after_sort
        else:
            length: int = len(to_sort)
            list_after_sort = []
            while True:
                i = 0
                store_index_i: int
                min_of_list = to_sort[0][0]
                while i < len(to_sort):
                    if to_sort[i][0] <= min_of_list:
                        min_of_list = to_sort[i][0]
                        store_index_i = i
                    i += 1
                list_after_sort.append(to_sort[store_index_i])
                to_sort.remove(to_sort[store_index_i])
                if len(list_after_sort) == length:
                    break
            return(list_after_sort)

    elif order == 2:
        if isinstance(to_sort[0], str):
            length: int = len(to_sort)
            list_after_sort = []
            while True:
                i = 0
                store_index_i: int
                max_of_list = to_sort[0]
                while i < len(to_sort):
                    if to_sort[i] >= max_of_list:
                        max_of_list = to_sort[i]
                        store_index_i = i
                    i += 1
                list_after_sort.append(to_sort[store_index_i])
                to_sort.remove(to_sort[store_index_i])
                if len(list_after_sort) == length:
                    break
            list_after_sorting = []
            i = len(list_after_sort) - 1
            while i >= 0:
                list_after_sorting.append(list_after_sort[i])
                i -= 1
            return(list_after_sorting)
        else:
            length: int = len(to_sort)
            list_after_sort = []
            while True:
                i = 0
                store_index_i: int
                min_of_list = to_sort[0][0]
                while i < len(to_sort):
                    if to_sort[i][0] <= min_of_list:
                        min_of_list = to_sort[i][0]
                        store_index_i = i
                    i += 1
                list_after_sort.append(to_sort[store_index_i])
                to_sort.remove(to_sort[store_index_i])
                if len(list_after_sort) == length:
                    break
            list_after_sorting = []
            i = len(list_after_sort) - 1
            while i >= 0:
                list_after_sorting.append(list_after_sort[i])
                i -= 1
            return(list_after_sorting)

        
        
                
            
        
    

def extract_students(fobj: io.TextIOWrapper)->list:
    """
    Parses fobj to extract details of each student found in the file.

    Parameter:
        fobj: open file object in read mode
    Returns:
        result: list of Candidate objects sorted in ascending order
    """
    try:
        all_lines = fobj.readlines()
    except:
        return []
    if all_lines == []:
        return []
    all_lines = all_lines[1 : ]
    i = 0
    while i < len(all_lines):
        all_lines[i] = all_lines[i].strip()
        i += 1
    list_of_students = []
    # Check if the last element is an empty string,
    # then take them to extra time equal 0

    i = 0
    while i < len(all_lines):
        information_of_students = []
        information_of_students = all_lines[i].split(",")
        if information_of_students[2] == "":
            information_of_students[2] = 0
        list_of_students.append(information_of_students)
        i += 1
    # change to the ascending order
    list_with_order: list = sort(list_of_students, 1)
    # now we have the list with ascending order.
    # then take each element in the list to create Candidate object
    i = 0
    list_of_candidate: list = []
    while i < len(list_with_order):
        students = candidate.Candidate(list_with_order[i][0], list_with_order[i][1], int(list_with_order[i][2]))
        list_of_candidate.append(students)
        i += 1
    return list_of_candidate




def main():
    extract_students(open("/home/info1110_test_1/students.csv"))

main()
