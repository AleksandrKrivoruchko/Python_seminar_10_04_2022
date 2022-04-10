def save_to_csv(contact_info):
    with open('contacts.csv', 'a') as bd:
        for info in contact_info:
            bd.write(f'{info};')
        bd.write('\n')


# save_to_csv(['Глухов', 'Павел', '+7 913 927 5379', 'Ученик в GB'])
