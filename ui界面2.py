import wx
import matplotlib.pyplot as plt
import time
import random
import sqlite3
weight=[]
value=[]
ratio=[]
packbag=[]
message=[]
def read():
    fname = 'data.txt'
    with open(fname, 'r') as f:
        s = [i.split(',') for i in f.readlines()]
    number=30
    for i in range(len(s)):
        for j in range(len(s[i])):
            if(i==0):
                weight.append(int(s[i][j]))
            else:
                value.append(int(s[i][j]))

class Frame1(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title = "D{0-1} KP",pos=(100,100),size=(400,300))
        #创建面板
        firstPan = wx.Panel(self)
        #创建文本框和输入框
        title = wx.StaticText(firstPan,label="请选择要进行的操作",pos=(150,20))
        theFirst = wx.StaticText(firstPan,label="1,散点图",pos=(30,40))
        theSecond = wx.StaticText(firstPan,label="2,价值重量比非递增排序",pos=(30,60))
        theThird = wx.StaticText(firstPan,label="3,动态规划算法--最优解",pos=(30,80))
        theFour = wx.StaticText(firstPan,label="4,遗传算法",pos=(30,100))
        choice = wx.StaticText(firstPan,label="选择",pos=(30,120))
        self.choice_text = wx.TextCtrl(firstPan,pos=(80,120),size=(235,25),style=wx.TE_LEFT)
        #创建“确定”“取消”按钮
        but_yes = wx.Button(firstPan,label="确定",pos=(100,150))
        but_no = wx.Button(firstPan,label="取消",pos=(220,150))
        #给按钮绑定事件
        but_yes.Bind(wx.EVT_BUTTON,self.OnclickBut_yes)
        but_no.Bind(wx.EVT_BUTTON,self.OnclickBut_no)

    def OnclickBut_yes(self,event):
        message = ""
        self.choice = self.choice_text.GetValue()
        if self.choice == "":
            message = "请输入您的选择"
            wx.MessageBox(message)
        else:
            read()
            if self.choice == "1":
                plt.scatter(weight,value)
                plt.xlabel("weight")		#x轴标签
                plt.ylabel("value")		#y轴标签
                plt.tick_params(axis='both')	#x,y轴都有刻度
                plt.savefig('3.2.png')		#保存图片，一定要在show之前保存图片，否则保存的图片就为空白
                plt.show()
            elif self.choice == "2":
                app = wx.App()
                frame2 = Frame2(parent=None,id=1)
                frame2.Show()
                app.MainLoop
            elif self.choice == "3":
                app = wx.App()
                frame3 = Frame3(parent=None,id=1)
                frame3.Show()
                app.MainLoop()
            elif self.choice == "4":
                app = wx.App()
                frame4 = Frame4(parent=None,id=1)
                frame4.Show()
                app.MainLoop()
    def OnclickBut_no(self,event):
        self.choice_text.SetValue("")

        
if __name__=='__main__':
    app = wx.App()
    frame = Frame1(parent=None,id=1)
    frame.Show()
    app.MainLoop()