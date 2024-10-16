# import math

# angka = 49
# print(math.sqrt(angka))

import pandas as pd

data = {'Nama': ['Andi', 'Budi', 'Cici'],
        'Umur': [25, 30, 22],
        'Kota': ['Jakarta', 'Surabaya', 'Bandung']}

df = pd.DataFrame(data)
print(df)