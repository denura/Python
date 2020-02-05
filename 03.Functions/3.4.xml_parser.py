"""4. На вход функции передается строка с xml документом (тэги без аттрибутов, корневой элемент
только один).
   Нужно выполнить следующее преобразование и вывести максимальную вложенность.
   Пример:
        a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
        foo(a) ->
        {
            'name': 'root',
            'children': [
                {'name': 'element1', 'children': []},
                {'name': 'element2', 'children': []},
                {
                    'name': 'element3',
                    'children': [
                        {'name': 'element4', 'children': []}
                    ]
                }
            ]
        }, 2
      в данном случае у element4 тэга вложенность/глубина 2
      """

import xml.dom.minidom
import xml.etree.cElementTree
XML_FILE = "my_xml.xml"

def xml_parser(xml_string):
    """"выполнить следующее преобразование и вывести максимальную вложенность."""
    doc = xml.dom.minidom.parse(XML_FILE)
    tree = xml.etree.cElementTree.ElementTree(file=XML_FILE)
    root = tree.getroot()
    print("name:", root.tag)

    for child_of_root in root:
        print (child_of_root.tag)


xml_string = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
xml_parser(xml_string)
