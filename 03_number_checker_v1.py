def num_check (question):
    error = "Please enter a number more than 0"
    
    valid = False
    while not valid:
        
        #ask user for number and check if it is valid
        try:
            response = float(input (question))

            if response <= 0:
                print (error)
            else:
                return response

        except ValueError:
            print (error)


# loop six times to make testing quicker
for item in range (0, 6):
    number_choice = num_check("Size of your dimension: ")

