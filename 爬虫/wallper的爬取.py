import requests
import os
from lxml import etree

#proxies={
 #   "http":"http://118.190.244.234:3128"}
#  if __name__ == "__main__":
#  url = 'http://pic.netbian.com/4kdongman'
#  headers = {
#      'User-Agent':
#      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
#  }
#  page_text = requests.get(url=url, headers=headers).text
#
#  tree = etree.HTML(page_text)
#  li_list = tree.xpath('//div[@class="slist"]/ul/li/a@href')
#  if not os.path.exists('./picLibs'):
#      os.mkdir('./picLibs')
#  for li in li_list:
#      img_src = 'http://pic.netbian.com' + li
#      img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
#      img_name = img_name.encode('iso-8859-1').decode('gbk')
#      img_data = requests.get(url=img_src, headers=headers).content
#      img_path = 'picLibs/' + img_name
#      with open(img_path, 'wb') as fp:
#          fp.write(img_data)
#  print(img_name, '成功')


def get_picture(pages):
   # path = "自然"
    #os.mkdir("自然")
    for page in range(51, pages):
        print('++++++++++++++=正在抓取第{}页++++++'.format(page))
        url = "http://pic.netbian.com/4kdongman/index_{}.html".format(
            str(page))
        #print(url)
        headers = {
            'User-Agent':
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
        }
        resp = requests.get(url=url, headers=headers)
        print(resp)
        html = etree.HTML(resp.text)
        href = html.xpath('//div[@class="slist"]/ul/li/a/@href')
        print(href)
        for i in href:
            url = 'http://pic.netbian.com' + i
            resp = requests.get(url=url, headers=headers)
            html = etree.HTML(resp.text)
            src = html.xpath('//div[@class="photo-pic"]/a/img/@src')
            #print(src)
            for li in src:
                res = 'http://pic.netbian.com/' + li
                pic_name = res.split('/')[-1]
                pic_data = requests.get(res).content
                #print(pic_name)
                pic_i = '../动漫/' + pic_name
                with open(pic_i, 'wb') as f:
                    print('正在下载', pic_name)
                    f.write(pic_data)


if __name__ == "__main__":
    pages = int(input("请输入爬取的页数:"))
    get_picture(pages)
