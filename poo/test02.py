import random
from datetime import datetime


x = str(random.random())
y = x
print(y.replace(".", ""))


def generate_numbers():
    x = str(random.random())
    nome_file = x + str(datetime.now())[:11].replace("-", "")
    name_data = str(nome_file.replace(".", ""))
    print(name_data[-9:])
    return name_data

# 20211011
generate_numbers()
# print(data[:11].replace("-", ""))