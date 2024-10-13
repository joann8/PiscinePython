from array2D import slice_me

family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

print("\n____Listes vides ou limites weird____")
slice_me([], 1, 3)
slice_me(family, 1, -5)
slice_me(family, 3, 2)

print("\n____Erreurs____")
slice_me(3, 3, 3)
slice_me(None, 1, 3)
slice_me(family, None, 3)
