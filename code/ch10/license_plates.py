from itertools import product
from string import ascii_uppercase as alphabet

license_plates = (
    f'{letters} {number:03}'
    for letters in (
        "".join(chars)
        for chars in product(alphabet, repeat=3)
    )
    if letters != ('G', 'O', 'V')
    for number in range(1_000)
)

# testing = [
#     print(i, j)
#     for i in range(5)
#     for j in range(10)
# ]

