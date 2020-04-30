import pyfiglet
from termcolor import colored

permitted_colours = ("grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white")


def print_art(text, text_colour):
    ascii_art = pyfiglet.figlet_format(text)
    if text_colour in permitted_colours:
        colored_ascii = colored(ascii_art, text_colour)
    else:
        print("Colour not valid, will use magenta")
        colored_ascii = colored(ascii_art, "magenta")

    print(colored_ascii)


msg = input("What would you like to print?")
colour = input("What colour?").lower()
print_art(msg, colour)
