name = ["huy", "nhan", "gia", "nhung", "rosy"]
age = [20, 19, 31, 23, 21]
list_of_person = {}

def createdictionary():
    for i in range(len(name)):
        list_of_person[name[i]] = age[i]
    print(list_of_person)