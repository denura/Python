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


def xml_parser(xml_string):
    """"выполнить следующее преобразование и вывести максимальную вложенность."""
    print(xml_string.split("<"))

xml_string = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
xml_parser(xml_string)
