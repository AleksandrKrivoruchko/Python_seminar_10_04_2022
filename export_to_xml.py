import pandas as pd
import xml.etree.ElementTree as ET
import csv


def to_xml(file_name='contacts.csv'):
    with open(file_name, newline='') as f:
        csv_f = csv.reader(f, delimiter=';')
        data = []
        for row in csv_f:
            row.pop(len(row) - 1)
            data.append(row)
    return data[0:]


def convert_row(data):
    for row in data:
        # fam, name, phone, info = row
        xml = '<xml>\n'
        xml += '    <Last_name units = "%s">{}</Last_name>\n' \
            .format(row[0])
        xml += '    <Name units = "%s">{}</Name>\n' \
            .format(row[1])
        xml += '    <Phone_number units = "%s">{}</Phone_number>\n' \
            .format(row[2])
        xml += '    <Info units = "%s">{}</Info>\n' \
            .format(row[3])
        xml += '</xml>'
        with open('data.xml', 'w') as page:
            page.write(xml)
    return """<Фамилия="%s">
    <Имя>%s</Имя>
    <Номер телефона>%s</Номер телефона>
    <Описание>%s</Описание>
    </Фамилия>""" % (row[0], row[1], row[2], row[3])


data = to_xml()
convert_row(data)
# data = ET.Element('data')
print('\n'.join([convert_row(row) for row in data[1:]]))

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
