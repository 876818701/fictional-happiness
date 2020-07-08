from selenium import webdriver

# 创建 WebDriver 实例对象，指明使用Edge浏览器驱动
wd = webdriver.Edge(r'D:\Dev\Python 3.8.3\Scripts\msedgedriver.exe')

# WebDriver 实例对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.imdb.com/title/tt2442560/reviews?ref_=tt_urv')



from time import sleep
for i in range(1,26):
    lm = wd.find_element_by_id('load-more-trigger')
    lm.click()
    sleep(10)

tc = wd.find_elements_by_css_selector('#main > section > div.lister > div.lister-list  div > div.lister-item-content > a , #main > section > div.lister > div.lister-list div.lister-item-content div.content div.text' )
# 取出列表中的每个 WebElement对象，打印出其text属性的值
# text属性就是该 WebElement对象对应的元素在网页中的文本内容

f = open('.\Peaky Blinders.txt','w',encoding='utf-8')
for i in tc:
   
        print(i.text,file=f)
f.close()    
pass
