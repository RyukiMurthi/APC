
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

    return [shape_choice, rect_l, rect_w]

def triangle_area ():
    # calculate triangle dimension
    # area
    triangle_area = float (0.5*tri_b*tri_h)
    if shape_choice == "triangle" and dimension_choice == "area":
        print()
        print ("Area = {}".format (triangle_area))
        print()

    return [shape_choice, tri_h, tri_b]

def triangle_peri():
    # calculate parallelogram dimension
    # perimeter
    triangle_peri = float (tri_1+tri_2+tri_3)
    if shape_choice == "triangle" and dimension_choice == "perimeter":
        print()
        print ("Perimeter = {}".format (triangle_peri))
        print()

    return [shape_choice, tri_1, tri_2, tri_3]

def parallelogram_area ():
    # calculate parallelogram dimension
    # area
    para_area = float (para_b*para_h)
    if shape_choice == "parallelogram" and dimension_choice == "area":
        print()
        print ("Area = {}".format (para_area))
        print()

    return [shape_choice, para_b, para_h]

def parallelogram_peri ():
    # calculate parallelogram dimension 
    # perimeter
    para_peri = float ((para_1+para_2)*2)
    if shape_choice == "parallelogram" and dimension_choice == "perimeter":
        print()
        print ("Perimeter = {}".format (para_peri))
        print()

    return [shape_choice, para_1, para_2]






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

#lists to store summary data
summary_headings = ['Shape', 'Dimensions', 'Area', 'Perimeter']
summary_data = []

# intialise list
shape_list = []
dimension_value = []
area_list = []
peri_list = []

# data frame dictionary
apc_data_dict = {
    'Shape': shape_list,
    'Dimensions': dimension_value,
    'Area': area_list,
    'Perimeter': peri_list
}



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

    # add shape to list
    shape_list.append (shape_choice)

    # ask for dimension type
    dimension_choice = string_check ("Area / Perimeter?: ", valid_dimensions, "Please enter either area or perimeter")

    # return chosen dimension
    print ("You have chosen {}".format (dimension_choice))
        


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

        # add dimensions to list
        dimension_value.append (rect_l)
        dimension_value.append (rect_w)

    # *** get triangle ***
    if shape_choice == "triangle" and dimension_choice == "area":
        tri_b = float (num_check ("Base: "))
        tri_h = float (num_check ("Height: "))

        # return triangle value
        print ("Your base is {}".format (tri_b))
        print ("Your height is {}".format (tri_h))

        # calculate triangle
        calc_tri_a = triangle_area ()

        # add dimensions to list
        dimension_value.append (tri_b)
        dimension_value.append (tri_h)

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
        
        # add dimensions to list
        dimension_value.append (tri_1)
        dimension_value.append (tri_2)
        dimension_value.append (tri_3)
    
    # *** get parallelogram ***
    if shape_choice == "parallelogram" and dimension_choice == "area":
        para_b = float (num_check ("Base: "))
        para_h = float (num_check ("Height: "))

        # return parallelogram value
        print ("Your base is {}".format (para_b))
        print ("Your height is {}".format (para_h))

        # calculate parallelogram
        calc_para_a = parallelogram_area ()

        # add dimensions to list
        dimension_value.append (para_b)
        dimension_value.append (para_h)
    
    if shape_choice == "parallelogram" and dimension_choice == "perimeter":
        para_1 = float (num_check ("Side 1: "))
        para_2 = float (num_check ("Side 2: "))

        # return parallelogram value
        print ("Side 1 is {}".format (para_1))
        print ("Side 2 is {}".format (para_2))

        # calculate paralleogram
        calc_para_p = parallelogram_peri ()

        # add dimensions to list
        dimension_value.append (para_1)
        dimension_value.append (para_2)

    print('Shape',shape_list)
    print('Dimensions', dimension_value)
    print('Area', area_list)
    print('Perimeter', peri_list)

# print details
shape_frame = pandas.DataFrame (apc_data_dict)
shape_frame = shape_frame.set_index ('Shape')
print (shape_frame)