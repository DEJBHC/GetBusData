import requests
from bs4 import BeautifulSoup

def obtain_list(city):
    list = []
    url = f'https://{city}.8684.cn'
    response = requests.get(url)
    bs = BeautifulSoup(response.text,'html.parser')
    # 使用CSS选择器获取页面上的元素
    results = bs.select('div.bus-layer div.list')
    for element in results:
        # 获取当前元素前一个兄弟节点
        prev = element.previous_sibling
        # 取得 prev 元素内部的文本信息
        text = prev.text
        # 判断字符串是否是以"以"字为前缀
        if text.startswith('以'):
            # 获取 element 内部所有 a 元素
            links = element.select('a')
            for link in links:
                # 获取超链接
                suffix = link['href']
                # 将完整的查询地址添加到列表中
                list.append(f'{url}{suffix}')
    return list

city_list = ['nanchang', 'beijing']

list = obtain_list(city_list[0])
print(list)

list = obtain_list(city_list[1])
print(list)