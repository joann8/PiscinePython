ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#Mon code

ft_list[1] = "World!"

list_temp = list(ft_tuple)
list_temp[1]= "France!"
ft_tuple = tuple(list_temp)

#ft_set.remove("tutu!")
#ft_set.add("Paris!")
ft_set="{'Hello', 'Paris!'}"

ft_dict["Hello"] = "42Paris!"

#end mon code

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)