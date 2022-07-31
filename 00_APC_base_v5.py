

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
    # area
    circ_area = float (pi*circle_value*circle_value)
    if shape_choice == "circle" and dimension_choice == "area":
        print()
        print ("Area = {}".format (circ_area))
        print()
    
    # perimeter
    circ_peri = float ((2*pi)*circle_value)
    if dimension_choice == "perimeter":
        print()
        print ("Perimeter = {}".format (circ_peri))
        print()
   
def square ():
    # calculate square dimension
    # area
    square_area = float (square_value*square_value)
    if shape_choice == "square" and dimension_choice == "area":
        print()
        print ("Area = {}".format (square_area))
        print()
    
    # perimeter
    square_peri = float (4*square_value)
    if shape_choice == "square" and dimension_choice == "perimeter":
        print()
        print ("Perimeter = {}".format (square_peri))

def rectangle ():
    # calculate rectangle dimension
    # area
    rectangle_area = float (rect_l*rect_w)
    if shape_choice == "rectangle" and dimension_choice == "area":
        print()
        print ("Area = {}".format (rectangle_area))
        print()
    
    # perimeter
    rectangle_peri = float ((rect_l+rect_w)*2)
    if shape_choice == "rectangle" and dimension_choice == "perimeter":
        print()
        print ("Perimeter = {}".format (rectangle_peri))
        print()

def triangle_area ():
    # calculate triangle dimension
    # area
    triangle_area = float (0.5*tri_b*tri_h)
    if shape_choice == "triangle" and dimension_choice == "area":
        print()
        print ("Area = {}".format (triangle_area))
        print()

def triangle_peri():
    # calculate parallelogram dimension
    # perimeter
    triangle_peri = float (tri_1+tri_2+tri_3)
    if shape_choice == "triangle" and dimension_choice == "perimeter":
        print()
        print ("Perimeter = {}".format (triangle_peri))
        print()

def parallelogram_area ():
    # calculate parallelogram dimension
    # area
    para_area = float (para_b*para_h)
    if shape_choice == "parallelogram" and dimension_choice == "area":
        print()
        print ("Area = {}".format (para_area))
        print()

def parallelogram_peri ():
    # calculate parallelogram dimension 
    # perimeter
    para_peri = float ((para_1+para_2)*2)
    if shape_choice == "parallelogram" and dimension_choice == "perimeter":
        print()
        print ("Perimeter = {}".format (para_peri))
        print()






# *** MAIN ROUTINE ***

# get shape name
# valid shape hold list of all shape
# valid options include <full name and first letter>
valid_shapes = [
    ["circle", "c"],
    ["square", "s"],
    ["rectangle", "r"],
    ["triangle", "t"],
    ["parallelogram", "p"],
    ["xxx"]
    ]

# get dimension type
# valid dimensions hold list of the dimensions
# valid options include <full name and first letter>
valid_dimensions = [
    ["area", "a"],
    ["perimeter", "p"]
    ]

# intialise list
shape_choice = []
dimension_value = []
area_list = []
peri_list = []



shape_choice = ""
while shape_choice != "xxx":

    # ask for shape type
    shape_choice = string_check ("What shape?: ", valid_shapes, "Please enter a valid shape")

    # return shape choice
    if shape_choice != "xxx":
        print ("You have chosen {}".format (shape_choice))

    if shape_choice == "xxx":
        print ("EXIT")
        break

    # ask for dimension type
    dimension_choice = string_check ("Area / Perimeter?: ", valid_dimensions, "Please enter either area or perimeter")

    # return chosen dimension
    print ("You have chosen {}".format (dimension_choice))
        


    # *** GET VALUES AND RESULTS ***

    # *** get circle ***
    if shape_choice == "circle":
        circle_value = float (num_check ("Radius: "))

        # dimension value
        dimension_value = circle_value

        # return circle value
        print ("Your radius is {}".format (circle_value))

        # calculate circle
        circle()

    # *** get square ***
    if shape_choice == "square":
        square_value = float (num_check ("Length: "))

        # dimension value
        dimension_value = square_value

        # return square value
        print ("Your length is {}".format (square_value))

        # calculate square
        square ()

    # *** get rectangle ***
    if shape_choice == "rectangle":
        rect_l = float (num_check ("Length: "))
        rect_w = float (num_check ("Width: "))

        # dimension value
        dimension_value = rect_l
        dimension_value = rect_w

        # return rectangle value
        print ("Your length is {}".format (rect_l))
        print ("Your width is {}".format (rect_w))

        # calculate rectangle
        rectangle ()

    # *** get triangle ***
    if shape_choice == "triangle" and dimension_choice == "area":
        tri_b = float (num_check ("Base: "))
        tri_h = float (num_check ("Height: "))

        # get dimensions
        dimension_value = tri_b
        dimension_value = tri_h

        # return triangle value
        print ("Your base is {}".format (tri_b))
        print ("Your height is {}".format (tri_h))

        # calculate triangle
        triangle_area ()

    if shape_choice == "triangle" and dimension_choice == "perimeter":
        tri_1 = float (num_check ("Side length 1: "))
        tri_2 = float (num_check ("Side length 2: "))
        tri_3 = float (num_check ("Side length 3: "))

        # get dimensions
        dimension_value = tri_1
        dimension_value = tri_2
        dimension_value = tri_3

        # return triangle value
        print ("Side length 1 is {}".format (tri_1))
        print ("Side length 2 is {}".format (tri_2))
        print ("Side length 3 is {}".format (tri_3))

        # calculate triangle
        triangle_peri ()
    
    # *** get parallelogram ***
    if shape_choice == "parallelogram" and dimension_choice == "area":
        para_b = float (num_check ("Base: "))
        para_h = float (num_check ("Height: "))

        # get dimensions
        dimension_value = para_b
        dimension_value = para_h

        # return parallelogram value
        print ("Your base is {}".format (para_b))
        print ("Your height is {}".format (para_h))

        # calculate parallelogram
        parallelogram_area ()
    
    if shape_choice == "parallelogram" and dimension_choice == "perimeter":
        para_1 = float (num_check ("Side 1: "))
        para_2 = float (num_check ("Side 2: "))

        # dimension value
        dimension_value = para_1
        dimension_value = para_2

        # return parallelogram value
        print ("Side 1 is {}".format (para_1))
        print ("Side 2 is {}".format (para_2))

        # calculate paralleogram
        parallelogram_peri ()