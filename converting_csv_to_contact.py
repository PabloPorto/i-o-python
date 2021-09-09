import csv
from contato import Contato

def csv_to_contact(caminho, encoding='latin_1'):
    contacts = []

    with open(caminho,encoding=encoding) as file:
        reader = csv.reader(file)

        for line in reader:
            #unpacking python, it will follow the order of the parameters coming from line.
            id, name, email = line

            contact = Contato(id, name, email)
            contacts.append(contact)


    return contacts