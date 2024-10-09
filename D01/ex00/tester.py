from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

# tests listes vides
bmi_empty = give_bmi([], [])
print(bmi_empty, type(bmi_empty))
print(apply_limit(bmi_empty, 3))

# tests erreurs apply
apply_limit(bmi, "hello")
bmi.append("hello")
apply_limit(bmi, 26)

# tests erreurs bmi
height2 = [2.71, 1.15, 'lol', 2.58, 2.72]
weight2 = [165.3, 38.4, 1, "random", 165.4]
give_bmi(height2, weight2)

height3 = [2.71, 1.15]
weight3 = [165.3]
give_bmi(height3, weight3)

# test erreur poid
weight4 = [165.3, 0]
give_bmi(height3, weight4)
