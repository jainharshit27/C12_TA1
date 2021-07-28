a_list = [0, "2nd entry", True, 0]
print(a_list[0])
print(a_list)
a_list.append("hello")
print(a_list)
a_list.insert(2, "hello")
print(a_list)
print(type(a_list))


a_tuple = (0, "2nd entry", True, 0)
print(a_tuple[0])
print(type(a_tuple))


a_dictionary = {"number": 0, "string": "2nd entry", "boolean":True}
print(a_dictionary["string"])
print(a_dictionary.keys())
print(a_dictionary.values())
print(type(a_dictionary))