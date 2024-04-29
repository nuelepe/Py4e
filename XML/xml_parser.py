import xml.etree.ElementTree as ET


input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count: ', len(lst))
for tag in lst:
    print('Name', tag.find('name').text)
    print('ID', tag.find('id').text)
    print('Attribute', tag.get("x"))

