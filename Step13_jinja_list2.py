# Step13_jinja2_list.py

# 게시글 목록이 담긴 리스트
from jinja2 import Template


posts:list = [
    {"id":1, "writer":"작성자1", "title":"제목1"},
    {"id":2, "writer":"작성자2", "title":"제목2"},
    {"id":3, "writer":"작성자3", "title":"제목3"}
]

'''
    위의 posts에 담긴 데이터를 이용해서 아래와 같이 출력되도록

    글목록 입니다
    - 글번호: 1 작성자: 작성자1 제목: 제목1
    - 글번호: 2 작성자: 작성자2 제목: 제목2
    - 글번호: 3 작성자: 작성자3 제목: 제목3
'''

my_template = '''
    글목록 입니다
    {% for data in datas %}
    - 글번호: {{ data.id }} 작성자: {{ data.writer }} 제목: {{ data.title }}
    {% endfor %}
'''

temp: Template = Template(my_template)
result = temp.render(datas=posts)
print(result)