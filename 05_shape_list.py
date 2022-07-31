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



# initalise shape list

shape_choice = ["Circle", "Square", "Rectangle", "Triangle", "Parallelogram"]

dimension_value = []
area_list = []
peri_list = []

result_list = [dimension_value, area_list, peri_list]

# data frame dictionary
apc_data_dict = {
    "Shape": shape_choice,
    "Dimensions": dimension_value,
    "Area": area_list,
    "Perimeter": peri_list
}

test_data = [
    [[5, "Dimensions"], [31.42, "Perimeter"]],
    [[4, "Dimensions"], [16, "Area"]],
    [[2, 7, "Dimensions"], [14, "Area"]],
    [[5, 9, 13, "Dimensions"], [29, "Perimeter"]],
    [[5, 8, "Dimensions"], [26, "Perimeter"]]
]

