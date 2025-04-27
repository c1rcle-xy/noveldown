import requests
from bs4 import BeautifulSoup
import re
def character_download(website, timeout=10):
 website = input("Enter the website: ")
 response = requests.get(website, verify=False) #盗版小说网站ssl很多都不全，遂关ssl校验
 if response.status_code == 200: #200验证
    sc = response.text
    soup = BeautifulSoup(sc, 'html.parser') #bs解析HTML
    p_content = soup.find('div', class_='content', id='chaptercontent') #局限性是否过大?有待改进
    p_title = soup.find('title') 
    if p_title and p_title.string:
        # 清理文件名，去除非法字符
        file_name = re.sub(r'[\\/*?:"<>|]', '', p_title.string.strip()) + ".txt"
        try:
            with open(file_name, mode="w", encoding="UTF-8") as file:
                if p_content and p_content.text:
                    file.write(p_content.text)
                    print("下载成功")
                else:
                    print("无法找到内容")
        except Exception as e:
            print(f"错误: {e}")
    else:
        print("无法找到标题")
 else:
    print("此章节下载出错")