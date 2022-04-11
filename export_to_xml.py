def export_to_xml(path):
    with open('contacts.xml', 'w') as xml:
        bd.write(f'{info};')
        

        for info in path:
            bd.write(f'{info};')
        bd.write('\n')
