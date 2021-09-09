try:
    with open('dados/contatos.csv', encoding='latin_1') as file_contacts:

        for line in file_contacts:
            print(line, end='');

except FileNotFoundError:
    print('You probably made a mistake writing the path of the file to be openned')
except PermissionError:
    print('You are not allowed to write in this file')
finally:
    file_contacts.close()