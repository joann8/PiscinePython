from load_image import ft_load
from pimp_image import ft_invert, ft_grey, ft_blue, ft_green, ft_red

array = ft_load("landscape.jpg")
# array = ft_load("../ex05")

ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)

print(ft_invert.__doc__)
