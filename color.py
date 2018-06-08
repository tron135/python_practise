from pyfiglet  import figlet_format
from termcolor import colored
valid_colors = ("red", "blue", "yellow", "blue", "magenta", "cyan")

msg = input("What would you like to print ?")
color = input("What color ??")
if color not in valid_colors:
	color = "yellow"

s = pyfiglet.figlet_format(msg)
t = colored(s, color = color)
print(t)