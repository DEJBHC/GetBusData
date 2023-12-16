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

def obtain_desc(line):
    response = requests.get(line['url'])
    bs = BeautifulSoup(response.text,'html.parser')
    list = bs.select('.bus-desc>li')
    desc = []
    for li in list:
        desc.append(li.text)
    line['desc'] = desc
    return line

# 定义 main 函数
def main():
    city_list = ['nanchang']
    for city in city_list:
        list = obtain_list(city)
        for e in list:
            lines = obtain_lines(e)
            for d in lines:
                obtain_desc(d)
            print(lines)
        print('- - - - - - - - - - - - - -')

# 将main函数放在if __name__ == "__main__" 语句中,
# 是为了防止在作为模块被导入时main函数被执行
if __name__ == "__main__":
    # 调用 main 函数
    main()