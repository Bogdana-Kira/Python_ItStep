from colorama import init, Fore, Back, Style

# Ініціалізація бібліотеки
init()

# Виведення тексту з кольоровим форматуванням
print(Fore.RED + 'Цей текст має червоний колір' + Fore.RESET)
print(Back.GREEN + 'Цей текст має зелений фон' + Back.RESET)
print(Style.BRIGHT + 'Цей текст написаний яскраво' + Style.RESET_ALL)
