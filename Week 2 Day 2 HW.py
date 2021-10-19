def fullName (first_name,last_name):
    full_name = []
    for i in range(len(first_name)):
        name = first_name[i] + " "  + last_name[i]
        full_name.append(name)
    return(full_name)
print(fullName(['John', 'Evan', 'Jordan', 'Max'],['Smith', 'Smith', 'Williams', 'Bell']))

def listLessThan10(list_1):
    return [x for x in list_1 if x < 10]
print(listLessThan10([1,11,14,5,8,9]))

def listCombiSort(list_1,list_2):
    new_list = list_1 + list_2
    new_list.sort()
    return(new_list)
print(listCombiSort([1,2,3,4,5,6],[3,4,5,6,7,8,10]))