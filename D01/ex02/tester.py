from load_image import ft_load

print(ft_load("landscape.jpg"))

# tests erreurs
ft_load("landscape.jpgff")
ft_load("load_image.py")
ft_load(None)
ft_load([])
