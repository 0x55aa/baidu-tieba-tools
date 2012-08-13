#-*- coding:utf-8 -*-
import cookielib, urllib2
import HTMLParser



class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
	HTMLParser.HTMLParser.__init__(self)
	self.aaa=False
	self.ttt=False
	#self.text=""
	#self.text2=""
	#标题
	self.sampleList=[]
	#url
	self.URLList=[]
     
    def handle_starttag(self, tag, attrs):
	# 这里重新定义了处理开始标签的函数
	if tag == 'td':
	# 判断标签<a>的属性
	    for(varviable,value) in attrs:
		if varviable=="class" and (value=="thread_title"):
		    self.ttt=True
	if tag == 'a' and self.ttt==True:
	    for(varviable,value) in attrs:
		if varviable=="href":
		    self.aaa=True
		    #self.text2=value
		    #print self.text2
		    self.URLList.append(value)
		    #print self.sampleList
    def handle_data(self,data):
	if self.aaa == True :
	    #self.text = data
	    #print self.text.decode('gbk')
	    self.sampleList.append(data.decode('gbk'))
	    #print data.decode('gbk')
    def handle_endtag(self,tag):
	if tag == 'a':
	    self.aaa=False
	if tag == 'td':
	    self.ttt=False

class Tieba_list:
    tieba_url = 'http://tieba.baidu.com'
    tieba_name = '银月l夏尔'
    def __init__(self):
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        urllib2.install_opener(opener)
    def get_subject_list(self, tieba_name = '银月l夏尔'):
        try:
            html = urllib2.urlopen(self.tieba_url + '/' + tieba_name).read()
	    my = MyParser()
	    my.feed(html)
	    if my.sampleList==[] or my.URLList==[]:
	 	#print 00
		return False
	    else:
		#print my.sampleList
		return my.sampleList,my.URLList

        except urllib2.URLError:
            print('connection error')
    def run(self):
        self.get_subject_list(self.tieba_name)


if __name__ == '__main__':
    t = Tieba_list()
    print('*' * 10 + t.tieba_name + '吧' + '*' * 10 + '\n\n')
    t.get_subject_list()

