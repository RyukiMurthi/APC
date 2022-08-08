import pandas

# initalise shape list

all_shapes = ['circle', 'square', 'rectangle', 'triangle', 'parallelogram']

dimension_value = []
area_list = []
peri_list = []

result_list = [dimension_value, area_list, peri_list]

#lists to store summary data
summary_headings = ['Shape', 'Dimensions', 'Area', 'Perimeter']
summary_data = []

all_shapes = ["square", "rectangle"]
dimension_value = [0, 0]
area_list = [0, 0]
peri_list = [0, 0]

# data frame dictionary
apc_data_dict = {
    'Shape': all_shapes,
    'Dimensions': dimension_value,
    'Area': area_list,
    'Perimeter': peri_list
}

# test_data = [
#     [[5, 'Dimensions'], [31.42, 'Perimeter']],
#     [[4, 'Dimensions'], [16, 'Area']],
#     [[2, 7, 'Dimensions'], [14, 'Area']],
#     [[5, 9, 13, 'Dimensions'], [29, 'Perimeter']],
#     [[5, 8, 'Dimensions'], [26, 'Perimeter']]
# ]

# count = 0
# for user_data in test_data:
    
#     # assume no value has been entered
#     for item in result_list:
#         item.append (0)

#     # get results (hard coded for easy testing)
#     result = test_data [count]
#     count += 1


# print details
shape_frame = pandas.DataFrame (apc_data_dict)
shape_frame = shape_frame.set_index ('Shape')
print (shape_frame)