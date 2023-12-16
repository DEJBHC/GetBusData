import requests
from bs4 import BeautifulSoup

#url = 'https://nanchang.8684.cn/list1'
#to = url.find('/list')
#print(url[0:to])

# 获取指定分类下所有公交线路
# 比如获取以数字1开头的所有线路
def obtain_lines(url):
    objects = []
    # 获得 url 的前缀(即剔除 /listX 部分 )
    prefix = url[0:url.find('/list')]
    response = requests.get(url)
    bs = BeautifulSoup(response.text,'html.parser')
    # 选择 <div class="list clearfix"> 内部的直接子元素
    links = bs.select('div.list.clearfix > a')
    for link in links:
        href = link['href']
        title = link['title']
        text = link.text
        object = { 'url': f'{prefix}{href}', 'full_name': title, 'short_name': text }
        objects.append(object)
    return objects

# 获得南昌市以数字1为开头的所有公交线路
lines = obtain_lines('https://nanchang.8684.cn/list1')
print(lines)