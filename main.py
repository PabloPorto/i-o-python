import converting_csv_to_contact

try:
    contacts = converting_csv_to_contact.csv_to_contact('dados/contatos.csv')

    for contact in contacts:
        print(f'{contact.id} - {contact.nome} - {contact.email}')

except FileNotFoundError:
    print('You probably made a mistake writing the path of the file to be openned')
except PermissionError:
    print('You are not allowed to write in this file')
