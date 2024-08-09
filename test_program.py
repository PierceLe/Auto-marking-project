'''
Name: Pierce Le - SID: 530328265
This is my test program for mark_response
There are totally 20 test cases for mark_response
- 4 test cases for short answer(test case 1, 2, 3, 4) with one positive test 
case and four negative test cases
- 6 test cases for single answer (test case 5, 6, 7, 8, 9, 10) with one positve
test case and 5 negative test cases
- 10 test cases for mutiple answer (test case from 11 to 20) with six positive
test case, one edge case and three negative test cases

- From line 15 and 16, I import module question and time
- From line 19 to 53, I create question_1 object with single type
- From line 56 to 80, I create question_2 object with multiple type
- From line 83 to 100, I create question_3 object with short type
- From line 105 to 322, I create test cases from test_plan.md

To create test case, I have to declare some variables.
+  responses: type is string, each test case have different responses 
and it take from inputs in test_plan.md
+  expected_marks: int | float, that take from Expected Output in test_plan.md
+ actual_marks: int | float, which is what mark_response return
+ if expected_marks == actual_marks, I will print pass that test case, if not,
I will raise an assertation error by using assert, then print to terminal 
expected_output is expected_marks and Got is
what actual_marks to see the difference.

- From line to , I create a function call delay. This function will use 
in main loop to make a delay after checking test case for each type of questions. 
For example, when you run this file, terminal will print "loading...". 
Then, after 1.5 seconds, it will print every test cases for short answer. 
If it pass every test case for short answer, terminal will continue to use 
function delay again. After that it will print every test cases for single answer. 
The reason why I create delay function is I want to create a time to read 
each line in terminal, instead of printing every thing immediately. 
The second reason is I want to make my test_program.py more interesting

- In main, I will call every testcase then if every test case
from 1 - 4 return True, I also print that pass every 
test case for short answer, others line also similar like short answer.
If I pass every 20 test cases, I will print that pass every test cases

- If you want to check only one test case, you can comment others.

'''
# import modules
import question
import time
'''
Declare 3 different questions.
The first question have the type is "single"
The second question have the type is "multiple"
The third question have the type is "short"
'''

# DECLARE QUESTION 1:
question_1 = question.Question("single")
# set attribute for question 1
# set type for question 1
question_1.set_type("single")
# declare a string variable, which is the description of question 1
description_1: str = ('Mance Rayder is buying Wildfire, which will cost '
                      'him 20 Gold Dragons. He has gold coins worth 1 '
                      'Gold Dragon each, and platinum coins worth 5 '
                      'Gold Dragons each. How many different ways can '
                      'Mance pay for his Wildfire with gold and platinum coins?')
# set description for question 1
question_1.set_description(description_1)

# declare a string variable, which is the answer of question 1
answer_1: str = "B"
# set correct answer for question 1
question_1.set_correct_answer(answer_1)

# declare an integer variable, which is the mark of question 1
marks_1: int = 1
# set marks for question 1
question_1.set_marks(marks_1)

# declare a list, which each element in list is a tuple with two elements.
# the first element is the answer option and the second one is a boolean
# with default variable is False.
answer_options_1: list = [("A. 2", False), ("B. 5", False), ("C. 4", False), ("D. 3", False)]
# set answer options for question
question_1.set_answer_options(answer_options_1)

# DECLARE QUESTION 2:
question_2 = question.Question("multiple")
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

# DECLARE QUESTION 3:
question_3 = question.Question("short")
# set attribute for question 3
# set type for question 3
question_3.set_type("short")
# declare a string variable, which is the description of question 3
description_3: str = 'The abbreviation for "High Distinction " is '
# set description for question 3
question_3.set_description(description_3)
# declare a string variable, which is the answer of question 3
answer_3: str = "HD"
# set correct answer for question 3
question_3.set_correct_answer(answer_3)

# declare an integer variable, which is the mark of question 3
marks_3: int = 2
# set marks for question 3
question_3.set_marks(marks_3)


# TEST CASE FOR MARK RESPONSE
# test case 1, 2, 3, 4 for short question(question 3)
# type question: short, positive test case, correct answer
# get full marks for question 3 with 2/2
def test_case_1():
    responses: str = "HD"
    expected_marks: int = 2
    actual_marks: int = question_3.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 1")
    return True


# test case 2
# type question: short, negative test case, wrong answer
# get no points for question 3 0/2
def test_case_2():
    responses: str = "D"
    expected_marks: int = 0
    actual_marks: int = question_3.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 2")
    return True


# test case 3:
# type question: short, negative test case, wrong answer
# get no points for question 3 0/2
def test_case_3():
    responses: str = "C"
    expected_marks: int = 0
    actual_marks: int = question_3.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 3")
    return True


# test case 4:
# type question: short, negative test case, wrong answer
# get no points for question 3 0/2
def test_case_4():
    responses: str = "hd"
    expected_marks: int = 0
    actual_marks: int = question_3.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 4")
    return True


# test case 5, 6, 7, 8, 9, 10 for single question(question 1)
# test case 5
# type question: single, positive test case, correct answer
# get all points for question 1 1/1
def test_case_5():
    responses: str = "B"
    expected_marks: int = 1
    actual_marks: int = question_1.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 5")
    return True
# test case 6, 7, 8, 9, 10
# type question: single, negative test case, wrong answer
# get no points for question 1 0/1
def test_case_6():
    responses: str =  "A"
    expected_marks: int = 0
    actual_marks: int = question_1.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 6")
    return True

def test_case_7():
    responses: str = "C"
    expected_marks: int = 0
    actual_marks: int = question_1.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 7")
    return True


def test_case_8():
    responses: str = "D, B"
    expected_marks: int = 0
    actual_marks: int = question_1.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 8")
    return True

def test_case_9():
    responses: str = "hello"
    expected_marks: int = 0
    actual_marks: int = question_1.mark_response(responses)
    assert expected_marks == actual_marks, ('Return value from \'mark_response\' was incorrect.'
                                            f'\nExpected: {expected_marks}\nGot: {actual_marks}\n')
    print("Pass test case 9")
    return True



def test_case_10():
    responses: str = ""
    expected_marks: int = 0
    actual_marks: int = question_1.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 10")
    return True

# test case 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 for multiple question(question 2)
# test case 11, 12, 13, 14, 15, 16 for positive test cases, type of question is multiple
# type question: multiple, positive test case, correct answer
# get all points for question 2 3/3
def test_case_11():
    responses: str = "A, B, C, D"
    expected_marks = 3.0
    actual_marks: int = question_2.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 11")
    return True
# type question: multiple, positive test case, correct answer
# get all points for question 2 3/3
def test_case_12():
    responses: str = "A, C"
    expected_marks = 3.0
    actual_marks: int = question_2.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 12")
    return True
# type question: multiple, positive test case, correct answer
# get all points for question 2 3/3
def test_case_13():
    responses: str = "A, C, B"
    expected_marks = 3.0
    actual_marks: int = question_2.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 13")
    return True
# type question: multiple, positive test case, correct answer
# get partial points for question 2 1.5/3
def test_case_14():
    responses: str = "A, D"
    expected_marks = 1.5
    actual_marks: int = question_2.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 14")
    return True
# type question: multiple, positive test case, correct answer
# get partial points for question 2 1.5/3
def test_case_15():
    responses: str = "A, B"
    expected_marks = 1.5
    actual_marks: int = question_2.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 15")
    return True
# type question: multiple, positive test case, correct answer
# get partial points for question 1 1.5/3
def test_case_16():
    responses: str = "A, c"
    expected_marks = 1.5
    actual_marks: int = question_2.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 16")
    return True
# test case 17, 18, 19, 20 for positive test cases, type of question is multiple
# type question: multiple, negative test case, wrong answer
def test_case_17():
    responses: str = "a, c"
    expected_marks = 0
    actual_marks: int = question_2.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 17")
    return True
# type question: multiple, negative test case, wrong answer

def test_case_18():
    responses: str = "hello"
    expected_marks = 0
    actual_marks: int = question_2.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 18")
    return True
# type question: multiple, negative test case, wrong answer

def test_case_19():
    responses: str = "C, C"
    expected_marks = 1.5
    actual_marks: int = question_2.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 19")
    return True

def test_case_20():
    responses: str = ""
    expected_marks = 0
    actual_marks: int = question_2.mark_response(responses)
    assert expected_marks == actual_marks, ("Return value from 'mark_response' was incorrect."
                                            f"\nExpected: {expected_marks}\nGot: {actual_marks}\n")
    print("Pass test case 20")
    return True


def delay():
    print("loading", end="", flush=True)
    i = 0
    while i < 3:
        print(".", end="", flush=True)
        time.sleep(0.5)
        i += 1
    print()
    return

def main():
    delay()
    test1 = test_case_1()
    test2 = test_case_2()
    test3 = test_case_3()
    test4 = test_case_4()
    if test1 and test2 and test3 and test4:
        print("PASS ALL SHORT TEST CASES")
        delay()
    test5 = test_case_5()
    test6 = test_case_6()
    test7 = test_case_7()
    test8 = test_case_8()
    test9 = test_case_9()
    test10 = test_case_10()
    if test5 and test6 and test7 and test8 and test9 and test10:
        print("PASS ALL SINGLE TEST CASES")
        delay()
    test11 = test_case_11()
    test12 = test_case_12()
    test13 = test_case_13()
    test14 = test_case_14()
    test15 = test_case_15()
    test16 = test_case_16()
    test17 = test_case_17()
    test18 = test_case_18()
    test19 = test_case_19()
    test20 = test_case_20()
    if test11 and test12 and test13 and test14 and test16 and test17 and test18 and test19 and test20:
        print("PASS ALL MULTIPLE TEST CASES")
        delay()
    if ((test1 and test2 and test3 and test4) and 
        (test5 and test6 and test7 and test8 and test9 and test10) and
        (test11 and test12 and test13 and test14 and test16 and test17 and test18 and test19 and test20)):
        print("PASS ALL TEST CASES")



if __name__ == "__main__":
    main()
