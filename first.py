import wx
#import images

class ShapedFrame(wx.Frame):
    def __init__(self):
	wx.Frame.__init__(self,None,-1,"!!!!",pos=(360,360),style=wx.FRAME_SHAPED|wx.SIMPLE_BORDER|wx.FRAME_NO_TASKBAR)

	self.hasShape = False
	self.bmp = wx.Image('/home/z0x55aa/logo.gif', type=wx.BITMAP_TYPE_GIF).ConvertToBitmap()
	#self.bmp.SetAlphaData(100)
	#self.bmp.SetMask(wx.Mask(self.bmp,wx.BLACK))

	self.SetClientSize((self.bmp.GetWidth(),self.bmp.GetHeight()))

	dc = wx.ClientDC(self)
	dc.DrawBitmap(self.bmp,0,0,True)
	self.SetWindowShape()
	self.timer = wx.Timer(self,)
	self.Bind(wx.EVT_TIMER,self.OnExit,self.timer)
	self.Bind(wx.EVT_PAINT,self.OnPaint)
	self.Bind(wx.EVT_WINDOW_CREATE,self.SetWindowShape)

    def SetWindowShape(self,evt=None):
	r = wx.RegionFromBitmap(self.bmp)
	self.hasShape = self.SetShape(r)


    def OnPaint(self,evt):
	dc = wx.PaintDC(self)
	dc.DrawBitmap(self.bmp,0,0,True)

    def OnExit(self,evt):
	self.Close()


if __name__=='__main__':
    app = wx.PySimpleApp()
    a = ShapedFrame()
    a.Show()
    a.timer.Start(1000,True)
    app.MainLoop()






