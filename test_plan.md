# Test Case Designs
Complete the given tables with details of your test case design for each question type.
State the values to initalize appropriate `Question` objects required for the test case.

* Question 1 is derived from the first question in practice quiz 7 for MATH1064.
Question 1:
- Type of question: "single".
- Description: "Mance Rayder is buying Wildfire, which will cost him 20 Gold Dragons. 
He has gold coins worth 1 Gold Dragon each, and platinum coins worth 5 Gold Dragons each. 
How many different ways can Mance pay for his Wildfire with gold and platinum coins?"
- Answer options: "A. 2", "B. 5", "C. 4", "D. 3"
- Correct answer is "B"
- Marks: 1

Question 2:
- Type of question: "multiple".
- Description: "Which of the following brands is not primarily known for producing sneakers?"
- Answer options: "A. Apple", "B. Nike", "C. Samsung", "D. Adidas"
- Correct answer is "A, C"
- Marks: 3

Question 3:
- Type of question: "short".
- Description: "The abbreviation for "High Distinction" is "
- Correct answer is "HD"
- Marks: 2

Column descriptions:
* Test ID - Test case identification number
* Description - Type of testcase and brief explanation of test case details
* Inputs - Arguments into the method
* Expected Output - Return values of the method
* Status - pass/fail


Table 1: Summary of test cases for method `mark_response` for question type `short`

| Test ID |             Description              | Inputs | Expected Output | Status |
| ------- | -------------------------------------| ------ | --------------- | ------ |
|   1     |  Positive: Correct answer            |  "HD"  |       2         |   pass |
|   2     |  Negative: Incorrect answer          |  "D"   |       0         |   pass |
|   3     |  Negative: Incorrect answer          |  "C"   |       0         |   pass |
|   4     |  Negative: Incorrect answer          |  "hd"  |       0         |   pass |
Table 2: Summary of test cases for method `mark_response` for question type `single`

| Test ID |            Description               | Inputs | Expected Output | Status |
| ------- | -------------------------------------| ------ | --------------- | ------ |
|   5     | Postive: Correct answer              |  "B"   |       1         |  pass  |
|   6     | Negative: Incorrect answer           |  "A"   |       0         |  pass  |
|   7     | Negative: Incorrect answer           |  "C"   |       0         |  pass  |
|   8     | Negative: Incorrect answer           | "D, B" |       0         |  pass  |
|   9     | Negative: Invalid answer             |"hello" |       0         |  pass  |
|   10    | Negative: Empty string               |  ""    |       0         |  pass  |


Table 3: Summary of test cases for method `mark_response` for question type `multiple`

| Test ID |                     Description                       |    Inputs         | Expected Output | Status |
| ------- | ------------------------------------------------------| ------------------| --------------- | ------ |
|   11    | Positive: Enter every options of question             | "A, B, C, D"      |  3              | pass   |
|   12    | Positive: All correct answers                         | "A, C"            |  3              | pass   |
|   13    | Positive: Enter three options while 2 options are True| "A, C, B"         |  3              | pass   |
|   14    | Positive: Have some correct answers                   | "A, D"            |  1.5            | pass   |
|   15    | Positive: Have some correct answers                   | "A, B"            |  1.5            | pass   |
|   16    | Positive: Some lowercase options                      | "A, c"            |  1.5            | pass   |
|   17    | Negative: Invalid answer                              | "a, c"            |  0              | pass   |
|   18    | Negative: Invalid answer                              |"hello"            |  0              | pass   |
|   19    | Edge: Same answer                                     |"C, C"             |  1.5            | pass   |
|   20    | Negative: Empty string                                |""                 |  0              | pass   |  


