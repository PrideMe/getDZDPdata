import requests
from bs4 import BeautifulSoup
import time
headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Accept-Encoding": "gzip, deflate, sdch", "Accept-Language": "zh-CN,zh;q=0.8","Cache-Control": "max-age=0",
           "Connection": "keep-alive", "Host": "www.dianping.com", "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36"}
url = "http://www.dianping.com/search/category/3/10/g110p"
for page_number in range(1,51):
    myurl = '%s%s' %(url,page_number)
    print(myurl)
    request = requests.post(myurl, headers=headers)
    soup = BeautifulSoup(request.text, "html.parser")
    # print(soup.title.get_text())
    for txt in soup.find_all('div', {'class': 'txt'}):
        for title in txt.find_all('div', {'class': 'tit'}):
            # 解决bug，标题不够长时
            print(title.find_all('a')[0]['title'])
        for comment in txt.find_all('div', {'class': 'comment'}):
            print(comment.find_all('span')[0]['title'].replace(' ', '').replace('\n', '').replace('\t', ''))
            print(comment.find_all('a')[0].find_all('b')[0].get_text(), '条评论')
            for comment_consume in comment.find_all('a',{'class':'mean-price'}):
                a = comment_consume.find_all("b")
                print('消费',''.join(str(a)).replace('</b>]','').replace('[<b>',''))
    if(page_number!=50):
        print('下一页：', soup.find_all('div', {'class': 'page'})[0].find_all('a', {'class': 'next'})[0]['href'][22:29].replace('?',''))
    print('========================')
    time.sleep(2)