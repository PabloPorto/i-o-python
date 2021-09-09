contact_number_one = '15,luana,luana@email.com.br\n'
contact_number_two = '16,jessica,jessica@email.com.br\n'

with open('dados/contatos-written.csv', encoding='latin_1', mode='w') as file_contacts_one:
    file_contacts_one.write(contact_number_one)

with open('dados/contatos-written.csv', encoding='latin_1', mode='a') as file_contacts_two:
    file_contacts_two.write(contact_number_two)

#there is a lot of ways to deal with concurrency in python.