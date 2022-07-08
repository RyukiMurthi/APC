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



shape = string_check("What shape do you want? ", ["square", "circle", "rectangle", "triangle", "parallelogram"], "Please enter a valid shape (square / circle / rectangle / triangle / parallelogram")
print("you chose", shape)