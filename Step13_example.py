# Step13_example.py

from jinja2 import Template


info:dict = {
    "num":1,
    "name":"김구라",
    "body":{
        "height":180,
        "weight":80
    },
    "hobby":["피아노", "당구", "프로그래밍"]
}

'''
    번호: 1
    이름: 김구라
    키: 180 cm
    몸무게: 80 kg
    취미: 피아노 당구 프로그래밍
'''

my_template = '''
    번호: {{ num }}
    이름: {{ name }}
    키: {{ body.height }}
    몸무게: {{ body.weight }}
    취미:
    {% for data in hobby %}
        - {{ data }}
    {% endfor %}
'''

temp:Template = Template(my_template)
result = temp.render(info)

print(result)