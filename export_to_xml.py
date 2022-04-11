# import pandas as pd
# import xml.etree.ElementTree as ET
import csv


def csv_to_data(file_name='contacts.csv'):
    with open(file_name, newline='') as f:
        csv_f = csv.reader(f, delimiter=';')
        data = []
        for row in csv_f:
            data.append(row)
    return data


def export_to_xml(data=csv_to_data()):
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<contacts>\n'
    for row in data:
        xml += '    <contact>\n'
        xml += '        <Last_name>{}</Last_name>\n' \
            .format(row[0])
        xml += '        <Name>{}</Name>\n' \
            .format(row[1])
        xml += '        <Phone_number>{}</Phone_number>\n' \
            .format(row[2])
        xml += '        <Info>{}</Info>\n' \
            .format(row[3])
        xml += '    </contact>\n'
    xml += '</contacts>'
    with open('contacts.xml', 'w') as page:
        page.write(xml)
    return data

# contacts = csv_to_data()
# print(contacts)
# export_to_xml(contacts)

# data = ET.Element('data')
# print('\n'.join([export_to_xml(row) for row in data[1:]]))

# <?xml version="1.0"?>
# <Company>
#   <Employee>
#       <FirstName>Tanmay</FirstName>
#       <LastName>Patil</LastName>
#       <ContactNo>1234567890</ContactNo>
#       <Email>tanmaypatil@xyz.com</Email>
#       <Address>
#            <City>Bangalore</City>
#            <State>Karnataka</State>
#            <Zip>560212</Zip>
#       </Address>
#   </Employee>
# </Company>
