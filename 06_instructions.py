

def string_check (question, options, error):
    valid = False
    while not valid:
        response = input (question).lower()
        for var_list in options:
            # if the answer is in one of the lists, return the full statement
            if response in var_list:

                # get full name of answer
                chosen = var_list[0].lower()
                is_valid = "yes"
                break

            # if the chosen option is not valid, set is_valid to no
            else:
                is_valid = "no"

        # if the answer is invalid ask question again
        if is_valid == "yes":
            return chosen
        else:
            print (error)

def instructions (yes_no):
    show_error = "Please enter either yes or no"
    show_help = "Would you like to read the instructions?: "
    show_help = string_check (show_help, yes_no, show_error)

    if show_help == "yes":
        print ()
        print ()
        print ("*** Area / Perimeter Calculator instructions ***")
        print ()
        print ("This program will calculate either the area or perimeter of a shape \n"
                "depending on your inputs")
        print ()
        print ("This program will ask you for...")
        print ("- your desired unit to work with (Valid units are cm, m, and km)")
        print ("- your desired shape (Valid shapes are circle, square, rectangle, triangle and parallelogram)")
        print ("- dimensions of the shape")
        print ()
        print ("Once you have finished calculating your shapes, \n"
                "please enter the exit code 'xxx'. \n"
                "This will allow you to see an overview of all \n"
                "the dimensions and results that has been calculated")
        print ()

        return ""


# *** MAIN ROUTINE ***

# valid options for instructions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# ask user if they want to read the intrsuctions
instructions (yes_no)