from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

'''
# tests listes vides
print("\n____Test listes vides____")
bmi_empty = give_bmi([], [])
print(bmi_empty, type(bmi_empty))
print(apply_limit(bmi_empty, 3))

# tests erreurs apply
print("\n____Test Erreurs apply limit____")
apply_limit(bmi, "hello")
bmi.append("hello")
apply_limit(bmi, 26)

# tests erreurs bmi
print("\n____Test Erreurs gibve bmi____")
height2 = [2.71, 1.15, 'lol', 2.58, 2.72]
weight2 = [165.3, 38.4, 1, "random", 165.4]
give_bmi(height2, weight2)

height3 = [2.71, 1.15]
weight3 = [165.3]
give_bmi(height3, weight3)

weight4 = [165.3, 0]
give_bmi(height3, weight4)

height5 = [-2.71, 1]
weight5 = [165.3, 38]
give_bmi(height5, weight5)

print("\n____Test Erreurs None____")
give_bmi(None, None)
apply_limit(None, 3)
give_bmi([1], {2})
apply_limit({2}, 3)
'''
