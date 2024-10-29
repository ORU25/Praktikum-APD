import os

current_dir = os.path.dirname(os.path.realpath(__file__))

path = os.path.join(current_dir, 'data\data.txt')

with open(path, 'w') as file:
    file.write('yuyun,24,wanita\n') 
    file.write('budi,24,pria\n') 

# try:
    with open(path, 'r') as file:
        data = file.read()
        print(data)

# except FileNotFoundError:
#     print('File tidak ditemukan')
