ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Liste classique []
# Mofication en accedant directement a la valeur cherchee
ft_list[1] = "World!"

# Tuple (): sorte de Liste mais avec un ordre immuable
# Pour le modifier: Tuple --> Liste --> Tuple
list_temp = list(ft_tuple)
list_temp[1] = "France!"
ft_tuple = tuple(list_temp)

# Set {}: valeurs uniques non ordonnees
# Les operations suivantes fonctionnent mais ne garantissent pas l'ordre d'affichage
# ft_set.remove("tutu!")
# ft_set.add("Paris!")
ft_set = "{'Hello', 'Paris!'}"

# Dictionnaire { : }: Assemblage de clef / valeur
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
