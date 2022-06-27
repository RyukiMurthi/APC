

def string_check (question, options, error):
    valid = False
    while not valid:
        response = input (question).lower()
        for var_list in options:
            # if the shape is in one of the lists, return the full statement
            if response in var_list:

                # get full name of shape and put it
                # in title case
                chosen = var_list[0].title()
                is_valid = "yes"
                break
            
            # if the chosen option is not valid, set is_valid to no
            else:
                is_valid = "no"

        # if the shape is invalid ask question again
        if is_valid == "yes":
            return chosen
        else:
            print (error)
            return ""

def num_check (question):
    error = "Please enter a number more than 0"
    
    valid = False
    while not valid:
        
        # ask user for number and check if it is valid
        try:
            response = float(input (question))

            if response <= 0:
                print (error)
            else:
                return response

        except ValueError:
            print (error)

def area_perimeter (question):
    
    valid = False
    while not valid:

        # ask for dimension type and put response in lowercase
        response = input (question).lower()

        if response == "a" or response == "area":
            return "area"
        elif response == "p" or response == "perimeter":
            return "perimeter"
        
        else:
            print ("Please enter either area / perimeter...\n")

def dimensions (shape_choice, ap_choice):

    # ask for dimensions
    if shape_choice == "circle":
        question == "Radius: "
    elif shape_choice == "square":
        question = "Length: "
    elif shape_choice == "rectangle":
        question == "Length and Width: "
    elif shape_choice == "triangle" and ap_choice == "area":
        question == "Base length and height: "
    elif shape_choice == "triangle" and ap_choice == "perimeter":
        question == "Side legth: "
    elif shape_choice == "parallelogram" and ap_choice == "area":
        question == "Base length and height: "
    elif shape_choice == "parallelogram" and ap_choice == "perimeter":
        question == "Side length 1 & 2: "

    get_dimensions = float (input(question))
    return get_dimensions



# *** main routine ***

# get shape name
# valid shapes hold list of all shapes
# valid options include <full name and first letter>
valid_shapes = [
    ["circle", "c"],
    ["square", "s"],
    ["rectangle", "r"],
    ["triangle", "t"],
    ["parallelogram", "p"]
    ]

# loop six times to make testing quicker
for item in range (0, 6):
    # check if shape is valid
    get_shape = string_check ("What shape?: ", valid_shapes, "Please enter a valid shape")
    
    # return chosen shape
    if get_shape != valid_shapes and get_shape != "":
        print ("You have chosen {}".format (get_shape))

    # ask for dimension type
    dimension_choice = area_perimeter ("Area / Perimeter?: ")

    # return chosen dimension
    print ("You have chosen {}".format (dimension_choice))

    # get dimensions



    # return dimension description

