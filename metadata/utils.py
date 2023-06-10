def tagset_desc(string):
    pairs = string.split(", ")

    # Initialize empty lists
    list_1 = []
    list_2 = []

    # Extract names and values and append to respective lists
    for pair in pairs:
        name, value = pair.split(" - ")
        list_1.append(name.strip())
        list_2.append(value.strip())
    
    list_1 = ' , '.join(list_1)
    return list_1

def tagset_val(str):
    pairs = str.split(", ")

    # Initialize empty lists
    list_1 = []
    list_2 = []

    # Extract names and values and append to respective lists
    for pair in pairs:
        name, value = pair.split(" - ")
        list_1.append(name.strip())
        list_2.append(value.strip())
    
    list_2 = ' , '.join(list_2)
    return list_2
