import requests
from bs4 import BeautifulSoup

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
    line =  {
        'url': 'https://ganzhou.8684.cn/x_30df69c6', 
        'full_name': '赣州于都12路公交车路线', 
        'short_name': '于都12路'
    }
    print(line)
    obtain_desc(line)
    print(line)

if __name__ == "__main__":
    main()