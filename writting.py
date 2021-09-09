file_contacts = open('dados/contatos-written.csv', encoding='latin_1', mode='a')

contacts = [ '11,Pablo,pabl0@email.com.br\n',
            '12,Lucas,lucas@email.com.br\n',
            '13,Rildete,rildete@email.com.br\n']

for contact in contacts:
    file_contacts.write(contact)

file_contacts.flush()

input("dear user, please press <enter> in your keaboard to terminate the execution.")