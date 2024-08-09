'''
Interface of the exam
'''
import sys
import setup
import program_two
import program_one
def main(args):
    commandline: tuple = program_one.parse_cmd_args(args)
    if commandline != None:
        list_of_candidates = program_two.main(args)
        if list_of_candidates != 1:
            # declare the attempt of invalid sid
            attempt: int = 0
            checking_name: int = 0
            response: bool = True
            signal:bool = False
            continuing: bool = True
            trying = False
            index_of_candidate = 0
            while True:
                if response:
                    enter_sid: str = input("Enter your student identification number (SID) to start exam: ")
                elif not response:
                    try_again: str = input("Do you want to try again [Y|N]? ")
                    if try_again.lower() == "y":
                        if attempt == 3:
                            print("Contact exam administrator.")
                            return
                        enter_sid: str = input("Enter your student identification number (SID) to start exam: ")
                    elif try_again.lower() == "n":
                        if attempt == 3:
                            print("Contact exam administrator.")
                            return None
                        return None
                    else:
                        print("Response must be [Y|N].")
                        continuing = False
                        signal = False
                        trying = True
                        continue

                if continuing:
                    # check the valid of enter_sid and the exist of sid.
                    if not enter_sid.isnumeric():
                        print("Invalid SID.")
                        attempt += 1
                        signal = False
                        response = True
                    elif len(enter_sid) != 9:
                        print("Invalid SID.")
                        attempt += 1
                        signal = False
                        response = True
                    elif int(enter_sid) <= 0:
                        print("Invalid SID.")
                        attempt += 1
                        signal = False
                        response = True
                    #check the exist of sid
                    else:
                        i = 0
                        exist: bool = False
                        while i < len(list_of_candidates):
                            if list_of_candidates[i].sid == enter_sid:
                                exist = True
                                index_of_candidate = i
                                break
                            i += 1
                        if exist == False:
                            print("Candidate number not found for exam.")
                            response = False
                            signal = True
                            attempt += 1
                        elif exist == True:
                            print("Verifying candidate details...")
                            while True:
                                if checking_name == 3:
                                    print("Contact exam administrator to verify documents.")
                                    return
                                name = input("Enter your full name as given during registration of exam: ")
                                if name.lower() != list_of_candidates[index_of_candidate].name.lower():
                                    checking_name += 1
                                    if checking_name < 3:
                                        print("Name does not match records.")
                                elif name.lower() == list_of_candidates[index_of_candidate].name.lower():
                                    print("Start exam....\n")
                                    list_of_candidates[index_of_candidate].do_exam(False)
                                    return 

                if attempt == 3:
                    if signal:
                        one_chance = input("Do you want to try again [Y|N]? ")
                        if one_chance.lower() == "n":
                            return None
                        elif one_chance.lower() == "y":
                            print("Contact exam administrator.")
                            return None
                        else:
                            response = False
                            print("Response must be [Y|N].")
                            trying = True
                            continue
                            
                    elif not signal:
                        print("Contact exam administrator.")
                        return None

if __name__ == "__main__":
    main(sys.argv) 
