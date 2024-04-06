import urllib.request
from lxml import etree
def create_request(page):
    url ='https://aspx.sc.chinaz.com/query.aspx?keyword=%E7%BE%8E%E5%A5%B3&issale=&classID=11&navindex=0&page='+str(page)
    headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
    request = urllib.request.Request(url=url,headers=headers)
    return request
def get_content(request):
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')

def down_load(content):
    tree = etree.HTML(content)
    name_list=tree.xpath('//*[@id="ulcontent"]/div//img/@alt')
    src_list=tree.xpath('//*[@id="ulcontent"]/div//img/@data-src')
    for i in range(len(src_list)):
        name=name_list[i]
        src=src_list[i]
        url = "https:"+src.replace("\\", "/")
        urllib.request.urlretrieve(url=url,filename=name+'.jpg')
start_page=int(input("Enter the start page:"))
end_page=int(input("Enter the end page:"))
for page in range(start_page,end_page+1):
    request=create_request(page)
    content=get_content(request)
    down_load(content)


