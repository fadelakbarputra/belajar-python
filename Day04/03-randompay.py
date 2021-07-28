import random
from typing import Literal
name_string = input("Nama-nama yang akan membayar (pisah dg koma): ")
name_string = name_string.split(", ")

will_pay = name_string[random.randint(0, len(name_string)-1)]
print(will_pay)

