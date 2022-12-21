def create_an_empty_list():
    return []

def create_a_list():
    return [1, 2, 3, 4]

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
    l.pop()
    return l

def remove_element_from_start_of_list(l):
    l.remove(l[0])
    return l

def retrieve_first_element_from_list(l):
    return l[0]

def retrieve_element_from_index(l, index):
    return l[index]

def retrieve_last_element_from_list(l):
    return l[len(l) - 1]

# Module list_crud.py contains a function "create_an_empty_list()" that creates and returns an empty list. F 
# Module list_crud.py contains a function "create_a_list()" that creates and returns a list of length 4.
# Module list_crud.py contains a function "add_element_to_end_of_list" that adds an element to the end of a list.
# Module list_crud.py contains a function "add_element_to_start_of_list" that adds an element to the start of a list.
# Module list_crud.py contains a function "remove_element_from_end_of_list()" that removes an element from the end of a list.
# Module list_crud.py contains a function "remove_element_from_start_of_list()" that removes an element from the start of a list.
# Module list_crud.py contains a function "retrieve_first_element_from_list()" that retrieves the first element from a list.
# Module list_crud.py contains a function "retrieve_element_from_index()" that takes a list and an index as arguments and returns the list's element at that index.
# Module list_crud.py contains a function "retrieve_last_element_from_list()" that retrieves the last element from a list.