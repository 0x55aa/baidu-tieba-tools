#-*- coding:utf-8 -*-
import wx
import webbrowser
import baidu_list
import baidu_del
import first

#标题
sampleList=[]
#url
URLList=[]


class Frame(wx.Frame):
    def __init__(self,parent):
	wx.Frame.__init__(self,parent,title="虹子湖专用删帖小助手(beta)---by 0x55aa（坏小孩/mg）",pos=(360,360),size=(500,500),style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX))
	self.panel = wx.Panel(self)

	self.sizer00 = wx.BoxSizer(wx.VERTICAL)

	self.u = ''
	self.if_login=''
	#登录
	self.userLabel = wx.StaticText(self.panel,-1,"帐号：")
	self.uservalue = wx.TextCtrl(self.panel,-1,"haha")
	self.pwdLabel = wx.StaticText(self.panel,-1,"密码：")
	self.pwdvalue = wx.TextCtrl(self.panel,-1,"123456",style=wx.TE_PASSWORD)
	self.userButton = wx.Button(self.panel,label="登录",pos=(10,10))
	
	#事件监听
	self.Bind(wx.EVT_BUTTON,self.user_login,self.userButton)

	self.box=wx.StaticBox(self.panel,-1,"登录")
	self.sizer = wx.StaticBoxSizer(self.box,wx.HORIZONTAL)
	self.sizer.AddMany([self.userLabel,self.uservalue,self.pwdLabel,self.pwdvalue,self.userButton,])

	self.sizer00.Add(self.sizer,0,wx.ALL,10)
	self.panel.SetSizer(self.sizer00)


	#列表和删除
	#这两句调用baidu_list进行列表的生成
	self.t=baidu_list.Tieba_list()
	self.sampleList,self.URLList = self.t.get_subject_list()

	self.clb = wx.CheckListBox(self.panel,-1,size=(320,360),choices=self.sampleList,style=wx.LB_MULTIPLE)
	for i in range(2,len(self.sampleList)):
		self.clb.Check(i,)
	
	self.delButton = wx.Button(self.panel,label="删除")
	self.refreshButton = wx.Button(self.panel,label="刷新")
	self.aboutButton = wx.Button(self.panel,label="关于")
	self.blogButton = wx.Button(self.panel,label="My Blog")
	#事件监听
	self.Bind(wx.EVT_BUTTON,self.del_list,self.delButton)
	self.Bind(wx.EVT_BUTTON,self.refresh_list,self.refreshButton)
	self.Bind(wx.EVT_BUTTON,self.about_this,self.aboutButton)
	self.Bind(wx.EVT_BUTTON,self.myblog,self.blogButton)
	#按钮横向排列
	sizerbt = wx.BoxSizer(wx.HORIZONTAL)
	sizerbt.Add(self.delButton,0,wx.ALL,10)
	sizerbt.Add(self.refreshButton,0,wx.ALL,10)
	sizerbt.Add(self.aboutButton,0,wx.ALL,10)
	sizerbt.Add(self.blogButton,0,wx.ALL,10)

	self.sizer00.Add(self.clb,0,wx.ALL,10)
	self.sizer00.Add(sizerbt,0,wx.ALL,10)


	#状态显示
	self.stLabel = wx.TextCtrl(self.panel,-1,'\n******虹子湖吧******\n\n',pos=(333,81),size=(156,360),style=wx.TE_READONLY|wx.TE_MULTILINE)
	self.stLabel.AppendText("---by 0x55aa（坏小孩/mg）\n")

    #用户登录函数
    def user_login(self,event):
	username = self.uservalue.GetValue()
	self.stLabel.AppendText(u"正在登录 %s ...\n" % username)
	password = self.pwdvalue.GetValue()
	self.u = baidu_del.BaiduUser(username, password)
	self.login = self.u.login()
	self.if_login = self.u.is_login()
	#判断登录是否成功
	if self.if_login:
	    self.userLabel.Hide()
	    self.uservalue.Hide()
	    self.pwdLabel.Hide()
	    self.pwdvalue.Hide()
	    self.userButton.Hide()
	    self.stLabel.AppendText(u"登录成功！.........\n")
	    self.sucessLabel = wx.StaticText(self.panel,-1,u"欢迎您的使用 %s ..." % username)
	    self.sizer.Add(self.sucessLabel,0,wx.ALL,2)
	    self.sizer.Layout()
	else:
	    self.stLabel.AppendText(u"..%s......\n" % self.login)
    #点击删除按钮，删除帖子
    def del_list(self,event):
	if self.if_login:
	    TIEBA_URL="http://tieba.baidu.com"

	    #获取选择的列表，返回一个元组
	    select_list = self.clb.GetChecked()
	    for i in range(len(select_list)):
		#print select_list[i],'...'
		del_url = TIEBA_URL + self.URLList[select_list[i]]
		#print self.sampleList[select_list[i]]
		is_del = self.u.delete_tiezi(del_url)
		if is_del:
		    print u"..删除帖子成功！(%s)..." % self.sampleList[select_list[i]][0:5]
		else:
		    print u"..删除帖子失败！..."
	else:
	    self.stLabel.AppendText(u".oh~no!请先登录！.........\n")
	    
    #点击刷新按钮，刷新帖子
    """self.clb.Set(sampleList)"""
    def refresh_list(self,event):
	self.t=baidu_list.Tieba_list()
	self.sampleList,self.URLList = self.t.get_subject_list()

	self.clb.Set(self.sampleList)
	"""
	for i in range(2,len(self.sampleList)):
		self.clb.Check(i,)
	"""
	self.stLabel.AppendText(u"..刷新成功！.........\n")

    #关于
    def about_this(self,event):
	dlg = wx.MessageDialog(self.panel,"感谢银月l夏尔吧的支持,本工具仅用于学习交流~\n《If I Die Young》\n\n\t\t\t---by 0x55aa（坏小孩/mg）\n","关于haha~",wx.OK,)
	dlg.ShowModal()
    #blog
    def myblog(self,event):
	webbrowser.open("http://0x55aa.sinaapp.com/")

class App(wx.App):

    def OnInit(self):
	self.frame = Frame(parent=None,title="bare",style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX))
	self.frame.Show()
	self.SetTopWindow(self.frame)
	return True

if __name__=='__main__':

    #app=App()
    app = wx.PySimpleApp()
    a = first.ShapedFrame()
    a.Show()
    a.timer.Start(6000,True)

    def hahah(evt):
	frame.Show()

    frame = Frame(parent=None)
    #这里不知道怎么实现，用了两个定时事件
    timer1 = wx.Timer(frame,)
    frame.Bind(wx.EVT_TIMER,hahah,timer1)
    timer1.Start(5000,True)

    app.MainLoop()
