

from math import pi


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

def circle ():
    # ask for shape type
    get_shape = string_check ("What shape?: ", valid_shapes, "Please enter a valid shape")
    
    # return shape choice
    if get_shape == "circle":
        print ("You have chosen circle")

    # ask for dimension type
    dimension_choice = string_check ("Area / Perimeter?: ", valid_dimensions, "Please enter either area or perimeter")

    # return chosen dimension
    print ("You have chosen {}".format (dimension_choice))

    # get dimension value
    if get_shape == "circle":
        circle_value = float (input ("Radius: "))

    # return circle value
    print ("Your radius is {}".format (circle_value))

    # calculate circle dimension
    circ_area = pi*circle_value*circle_value
    if dimension_choice == "area":
        print ("Area = {}".format (circ_area))
    
    circ_peri = (2*pi)*circle_value
    if dimension_choice == "perimeter":
        print ("Perimeter = {}".format (circ_peri))
   






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

# get dimension type
# valid dimensions hold list of the dimensions
# valid options include <full name and first letter>
valid_dimensions = [
    ["area", "a"],
    ["perimeter", "p"]
    ]

# loop six times to make testing quicker
for item in range (0, 6):
    
    # ask for shape type
    get_shape = string_check ("What shape?: ", valid_shapes, "Please enter a valid shape")
    
    # return shape choice
    if get_shape != valid_shapes and get_shape != "":
        print ("You have chosen {}".format (get_shape))

    # ask for dimension type
    dimension_choice = string_check ("Area / Perimeter?: ", valid_dimensions, "Please enter either area or perimeter")

    # return chosen dimension
    print ("You have chosen {}".format (dimension_choice))

    # get dimension value for each shape
    if get_shape == "circle":
        shape_value = float (input ("Radius: "))

    # return shape value
    print ("You radius is {}".format (shape_value))
   

    # calculate the chosen dimensions of the shape
    area_circ = pi*shape_value*shape_value
    if dimension_choice == "area":
        print ("Area = {}".format (area_circ))

    peri_circ = (2*pi)*shape_value
    if dimension_choice == "perimeter":
        print ("Perimeter = {}".format (peri_circ))



