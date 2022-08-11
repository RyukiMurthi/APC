
from cmath import rect
import pandas
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
    # calculate circle dimension
    # area and perimeter
    circ_area = float (pi*circle_value*circle_value)
    circ_peri = float ((2*pi)*circle_value)
    if shape_choice == "circle":
        print()
        print ("Area = {}".format (circ_area))
        print() 
        print ("Perimeter = {}".format (circ_peri))
        print()

        # add results to list
        area_list.append (circ_area)
        peri_list.append (circ_peri)

    return [shape_choice, circle_value]
   
def square ():
    # calculate square dimension
    # area and perimeter
    square_area = float (square_value*square_value)
    square_peri = float (4*square_value)
    if shape_choice == "square":
        print()
        print ("Area = {}".format (square_area))
        print()
        print ("Perimeter = {}".format (square_peri))
        print ()

        # add results to list
        area_list.append (square_area)
        peri_list.append (square_peri)

    return [shape_choice, square_value]

def rectangle ():
    # calculate rectangle dimension
    # area and perimeter
    rectangle_area = float (rect_l*rect_w)
    rectangle_peri = float ((rect_l+rect_w)*2)
    if shape_choice == "rectangle":
        print()
        print ("Area = {}".format (rectangle_area))
        print()
        print ("Perimeter = {}".format (rectangle_peri))
        print()

        # add results to list
        area_list.append (rectangle_area)
        peri_list.append (rectangle_peri)

    return [shape_choice, rect_l, rect_w]

def triangle_area ():
    # calculate triangle dimension
    # area
    triangle_area = float (0.5*tri_b*tri_h)
    if shape_choice == "triangle" and dimension_choice == "area":
        print()
        print ("Area = {}".format (triangle_area))
        print()

        # set perimeter to "n/a"
        triangle_peri = "n/a"

        # add area to list
        area_list.append (triangle_area)
        peri_list.append (triangle_peri)

    return [shape_choice, tri_h, tri_b]

def triangle_peri():
    # calculate parallelogram dimension
    # perimeter
    triangle_peri = float (tri_1+tri_2+tri_3)
    if shape_choice == "triangle" and dimension_choice == "perimeter":
        print()
        print ("Perimeter = {}".format (triangle_peri))
        print()

        # set area to "n/a"
        triangle_area = "n/a"

        # add perimeter to list
        peri_list.append (triangle_peri)
        area_list.append (triangle_area)

    return [shape_choice, tri_1, tri_2, tri_3]

def parallelogram_area ():
    # calculate parallelogram dimension
    # area
    para_area = float (para_b*para_h)
    if shape_choice == "parallelogram" and dimension_choice == "area":
        print()
        print ("Area = {}".format (para_area))
        print()

        # set perimeter to "n/a"
        para_peri = "n/a"

        # add area to list
        area_list.append (para_area)
        peri_list.append (para_peri)

    return [shape_choice, para_b, para_h]

def parallelogram_peri ():
    # calculate parallelogram dimension 
    # perimeter
    para_peri = float ((para_1+para_2)*2)
    if shape_choice == "parallelogram" and dimension_choice == "perimeter":
        print()
        print ("Perimeter = {}".format (para_peri))
        print()
        
        # set area to "n/a"
        para_area = "n/a" 

        # add perimeter to list
        peri_list.append (para_peri)
        area_list.append(para_area)

    return [shape_choice, para_1, para_2]

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


# get shape name
# valid shape hold list of all shape
# valid options include <full name and first letter>
valid_shapes = [
    ["circle", "c"],
    ["square", "s"],
    ["rectangle", "r"],
    ["triangle", "t"],
    ["parallelogram", "p"],
    ]

# get dimension type
# valid dimensions hold list of the dimensions
# valid options include <full name and first letter>
valid_dimensions = [
    ["area", "a"],
    ["perimeter", "p"]
    ]

# get units
# valid units hold list of the units
# valid options include <full name and first letter>

valid_units = [
    ["centimeter", "CM", "cm", "c"],
    ["meter", "M", "m"],
    ["kilometer", "KM", "kilo", "km", "k"],
    ["xxx"]
]



#lists to store summary data
summary_headings = ['Shape', 'Dimensions', 'Area', 'Perimeter']
summary_data = []

# intialise list
shape_list = []
dimension_value = []
area_list = []
peri_list = []
unit_list = []

# data frame dictionary
apc_data_dict = {
    'Shape': shape_list,
    'Dimensions': dimension_value,
    'Area': area_list,
    'Perimeter': peri_list,
    'Units': unit_list
}



# ask user if they want to read the intrsuctions
instructions (yes_no)

# loop to get shape information
unit_choice = ""
while unit_choice != "xxx":

    # ask for unit
    unit_choice = string_check ("What unit: ", valid_units, "Please enter a valid unit")

    # return unit choice
    if unit_choice != "xxx":
        print ("you have chosen {}".format (unit_choice))
        print ()

    if unit_choice == "xxx":
        print ("EXIT")
        break

    # add unit to list
    unit_list.append (unit_choice)

    # ask for shape type
    shape_choice = string_check ("What shape?: ", valid_shapes, "Please enter a valid shape")

    # return shape choice
    print ("You have chosen {}".format (shape_choice))
    print()

    # add shape to list
    shape_list.append (shape_choice)

    # ask for dimension type
    dimension_choice = string_check ("Area / Perimeter?: ", valid_dimensions, "Please enter either area or perimeter")

    # return chosen dimension
    print ("You have chosen {}".format (dimension_choice))
    print ()

        


    # *** GET VALUES AND RESULTS ***

    # *** get circle ***
    if shape_choice == "circle":
        circle_value = float (num_check ("Radius: "))

        # return circle value
        print ("Your radius is {}".format (circle_value))

        # calculate circle
        calc_circle = circle()

        # add dimensions to list
        dimension_value.append (circle_value)

    # *** get square ***
    if shape_choice == "square":
        square_value = float (num_check ("Length: "))

        # return square value
        print ("Your length is {}".format (square_value))

        # calculate square
        calc_square = square ()

        # add dimensions to list
        dimension_value.append (square_value)


    # *** get rectangle ***
    if shape_choice == "rectangle":
        rect_l = float (num_check ("Length: "))
        rect_w = float (num_check ("Width: "))

        # return rectangle value
        print ("Your length is {}".format (rect_l))
        print ("Your width is {}".format (rect_w))

        # calculate rectangle
        calc_rectangle = rectangle ()

        # reduce argument to 1
        rect_value = rect_l, rect_w

        # add dimensions to list
        dimension_value.append (rect_value)

    # *** get triangle ***
    if shape_choice == "triangle" and dimension_choice == "area":
        tri_b = float (num_check ("Base: "))
        tri_h = float (num_check ("Height: "))

        # return triangle value
        print ("Your base is {}".format (tri_b))
        print ("Your height is {}".format (tri_h))

        # calculate triangle
        calc_tri_a = triangle_area ()

        # reduce argument to 1
        tri_value_a = tri_b, tri_h

        # add dimensions to list
        dimension_value.append (tri_value_a)
   

    if shape_choice == "triangle" and dimension_choice == "perimeter":
        tri_1 = float (num_check ("Side length 1: "))
        tri_2 = float (num_check ("Side length 2: "))
        tri_3 = float (num_check ("Side length 3: "))

        # return triangle value
        print ("Side length 1 is {}".format (tri_1))
        print ("Side length 2 is {}".format (tri_2))
        print ("Side length 3 is {}".format (tri_3))

        # calculate triangle
        calc_tri_p = triangle_peri ()

        # reduce argument to 1
        tri_value_p = tri_1, tri_2, tri_3
        
        # add dimensions to list
        dimension_value.append (tri_value_p)

    
    # *** get parallelogram ***
    if shape_choice == "parallelogram" and dimension_choice == "area":
        para_b = float (num_check ("Base: "))
        para_h = float (num_check ("Height: "))

        # return parallelogram value
        print ("Your base is {}".format (para_b))
        print ("Your height is {}".format (para_h))

        # calculate parallelogram
        calc_para_a = parallelogram_area ()

        # reduce argument to 1
        para_value_a = para_b, para_h

        # add dimensions to list
        dimension_value.append (para_value_a)

    
    if shape_choice == "parallelogram" and dimension_choice == "perimeter":
        para_1 = float (num_check ("Side 1: "))
        para_2 = float (num_check ("Side 2: "))

        # return parallelogram value
        print ("Side 1 is {}".format (para_1))
        print ("Side 2 is {}".format (para_2))

        # calculate paralleogram
        calc_para_p = parallelogram_peri ()

        # reduce argument to 1
        para_value_p = para_1, para_2

        # add dimensions to list
        dimension_value.append (para_value_p)



# print details
shape_frame = pandas.DataFrame (apc_data_dict)
shape_frame = shape_frame.set_index ('Shape')
print (shape_frame)
print ()