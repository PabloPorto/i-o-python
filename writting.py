file_contacts = open('dados/contatos-written.csv', encoding='latin_1', mode='w+')

contacts = ['11,Pablo,pabl0@email.com.br\n',
            '12,Lucas,lucas@email.com.br\n',
            '13,Rildete,rildete@email.com.br\n']

for contact in contacts:
    file_contacts.write(contact)

file_contacts.flush()
file_contacts.write('14,Melissa,melissa@email.com.br\n'.upper())
file_contacts.seek(0)

for line in file_contacts:
    print(line, end='')