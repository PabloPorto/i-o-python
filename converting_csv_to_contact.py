import csv, pickle, json
from contato import Contato

def csv_to_contact(path, encoding='latin_1'):
    contacts = []

    with open(path,encoding=encoding) as file:
        reader = csv.reader(file)

        for line in reader:
            #unpacking python, it will follow the order of the parameters coming from line.
            id, name, email = line

            contact = Contato(id, name, email)
            contacts.append(contact)


    return contacts

def contacts_to_pickle(contacts, path):

    with open(path, mode='wb') as file:
        pickle.dump(contacts, file)

def pickle_to_contacts(path):

    with open(path, mode='rb') as file:
        contacts =  pickle.load(file)

    return contacts

def contacts_to_json(contacts, path):
    with open(path, mode='w') as file:
        json.dump(contacts, file, default=_contact_to_json)

def _contact_to_json(contact):
    return contact.__dict__

def json_to_contacts (path):
    contacts = []

    with open(path) as file:
        contacts_json = json.load(file)

        for contact in contacts_json:
            c = Contato(id = contact['id'], nome = contact['nome'], email = contact['email'] )
            # it could be like (unpacking):
            # c = Contato(**contact)
            contacts.append(c)
    
    return contacts