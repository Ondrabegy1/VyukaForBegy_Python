#Program pro zpracování textu. Zpracuje počet řádků, počet vět a průměrnou délku slova.

import re
import requests

# Stáhnutí textu z URL
url = "https://www.gutenberg.org/cache/epub/2267/pg2267.txt"
response = requests.get(url)
text = response.text

# Počet řádků
pocet_radku = len(re.findall(r'\n', text)) + 1
print(f'Počet řádků: {pocet_radku}')

# Počet vět
pocet_vet = len(re.split(r'[.!?]', text))
print(f'Počet vět: {pocet_vet}')

# Průměrná délka slova
slova = re.findall(r'\b\w+\b', text)
prumer_delky_slova = sum(len(slovo) for slovo in slova) / len(slova)
print(f'Průměrná délka slova: {prumer_delky_slova:.2f}')