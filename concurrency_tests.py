file_contacts_one = open('dados/contatos-written.csv', encoding='latin_1', mode='w')
file_contacts_two = open('dados/contatos-written.csv', encoding='latin_1', mode='w')

contact_number_one = '15,luana,luana@email.com.br\n'
contact_number_two = '16,jessica,jessica@email.com.br\n'

file_contacts_one.write(contact_number_one)
file_contacts_two.write(contact_number_two)

file_contacts_two.close()
file_contacts_two.close()

#there is a lot of ways to deal with concurrency in python.