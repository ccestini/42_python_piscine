ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# your code here
ft_list[1] = "World!"

new_tuple = list(ft_tuple)
new_tuple[1] = "UAE!"
ft_tuple = tuple(new_tuple)

ft_set.add("Abu Dhabi!")
ft_set.remove("tutu!")

ft_dict.update({"Hello": "42AbuDhabi!"})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)


"""
All 4 built-in data types in Python used to store collections of data:
List items are ordered, changeable, allow duplicate values, and items are indexed.
Tuple items are ordered, unchangeable, allow duplicate values, and items are indexed.
Set items are unordered, unchangeable, do not allow duplicate values, and unindexed.
Dictionary items are ordered, changeable, do not allow duplicates, and  items are presented in key:value pairs
"""
