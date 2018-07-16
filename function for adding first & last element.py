def find_elements(my_list):
    new_list = []
    first_element = my_list[0]
    last_element = my_list[-1]
    new_list.append(first_element)
    new_list.append(last_element)
    return new_list


print(find_elements([1, 2, 3, 4, 5, 6,7,8]))
