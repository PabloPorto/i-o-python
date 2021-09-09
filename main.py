import converting_csv_to_contact

try:
    # contacts = converting_csv_to_contact.csv_to_contact('dados/contatos.csv')
    # converting_csv_to_contact.contacts_to_pickle(contacts, 'dados/serialized_contacts.p')

    # contacts = converting_csv_to_contact.pickle_to_contacts('dados/serialized_contacts.p')

    # converting_csv_to_contact.contacts_to_json(contacts, 'dados/contacts_as_json.json')

    contacts = converting_csv_to_contact.json_to_contacts('dados/contacts_as_json.json')

    for contact in contacts:
        print(f'{contact.id} - {contact.nome} - {contact.email}')

except FileNotFoundError:
    print('You probably made a mistake writing the path of the file to be openned')
except PermissionError:
    print('You are not allowed to write in this file')
