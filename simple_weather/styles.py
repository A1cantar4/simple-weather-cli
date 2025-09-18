from colorama import Fore, Style, init

init(autoreset=True)

C_STYLED = {
    "normal": Fore.WHITE,
    "error": Fore.RED,
    "city": Fore.BLUE,
    "state": Fore.RED,
    "country": Fore.GREEN,
}

def styled(text, c_style="normal", bright=False):
    return f"{C_STYLED.get(c_style, Fore.WHITE)}{text}{Style.RESET_ALL}"



def c_normal(text): return styled(text, "normal")
def c_error(text): return styled(text, "error")
def c_city(text): return styled(text, "city")
def c_state(text): return styled(text, "state")
def c_country(text): return styled(text, "country")