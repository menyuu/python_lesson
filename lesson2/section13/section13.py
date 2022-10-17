# XML と Json

"""
XML
<?xml version='1.0' encoding='utf-8'?>
<root>
    <employee>
        <employ>
            <id>111</id>
            <name>Mike</name>
        </employ>
        <employ>
            <id>222</id>
            <name>Nancy</name>
        </employ>
    </employee>
</root>

Json
{
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
}

"""
import xml.etree.ElementTree as ET

root = ET.Element('root')
tree = ET.ElementTree(element=root)

employee = ET.SubElement(root, 'employee')

employ = ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '111'
employ_id = ET.SubElement(employ, 'name')
employ_id.text = 'Mike'

employ = ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '222'
employ_id = ET.SubElement(employ, 'name')
employ_id.text = 'Nancy'

# XML の書き込み
tree.write('test.xml', encoding='utf-8', xml_declaration=True)

# XML の読み込み
tree = ET.ElementTree(file='test.xml')
root = tree.getroot()

for employee in root:
    for employ in employee:
        for person in employ:
            print(person.tag, person.text)


import json

j = {
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
    }

print(j)
print('########################################')
# Json のデータフォーマットはダブルクォート
# ファイルへの書き込みなしで Python上だけで回す場合は s がつく
j = json.dumps(j)
print(json.loads(j))

# ファイルへの書き込み
with open('test.json', 'w') as f:
    json.dump(j, f)
print('########################################')
with open('test.json', 'r') as f:
    print(json.load(f))