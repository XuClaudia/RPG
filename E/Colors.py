from colorama import init, Fore, Back, Style

# Initialiseer colorama 
init(autoreset=True)
#------------ Ascii art kleur toewijzen-------------
class Color:
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL
#------------- Tekst kleur toewijzen ------------------
class TextPrinter:
    def __init__(self):
        self.colors = Color()
    
    def print_red(self, text):
        print(self.colors.RED + text)
    
    def print_green(self, text):
        print(self.colors.GREEN + text)
    
    def print_yellow(self, text):
        print(self.colors.YELLOW + text)
    
    def print_blue(self, text):
        print(self.colors.BLUE + text)
    
    def print_with_color(self, text, color_name):
        color_map = {
            "red": self.colors.RED,
            "green": self.colors.GREEN,
            "yellow": self.colors.YELLOW,
            "blue": self.colors.BLUE,
            "magenta": self.colors.MAGENTA,
            "cyan": self.colors.CYAN,
            "white": self.colors.WHITE
        }
        
        color = color_map.get(color_name.lower(), self.colors.WHITE) #KLeur geven en anders wit
        print(color + text) #tekst in de bijbehorende kleur printen

