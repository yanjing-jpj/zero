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

class Frame2(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title = "价值重量比非递增排序",pos=(100,100),size=(400,900))
        #创建面板
        firstPan = wx.Panel(self)
        #数据处理
        for i in range(len(weight)):
            rate=weight[i]/value[i]
            ratio.append(rate)
            for i in range(len(weight)):
                for j in range(len(value)):
                    if i==j:
                          for k in range(len(ratio)):
                              if j==k:
                                  t=[weight[i],value[j],ratio[k]]
                                  packbag.append(t)
        message=sorted(packbag,key=lambda x:x[2],reverse=True)
        #for i in range(len(message)):
        #    print("---")
        title = wx.StaticText(firstPan,label="价值重量比非递增排序",pos=(140,20))
        title = wx.StaticText(firstPan,label="重量        价值         价值重量之比",pos=(120,40))
        
        count=60
        
        for i in range(len(message)):
            date = wx.StaticText(firstPan,label="%8d      %8d        %8f"%(message[i][0],message[i][1],message[i][2]),pos=(95,count))
            #date = wx.StaticText(firstPan,label="%d"%message[i],pos=(0,count))
            count=count+20
#动态规划
class Frame3(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title = "动态规划最优解",pos=(100,100),size=(400,900))
        #算法
        c=10149
        value1=[]
        value1 = [[0 for j in range(c + 1)] for i in range(31)]
        for i in range(1, 31):
            for j in range(1, c + 1):
                if j<weight[i-1]:
                    value1[i][j]=value1[i-1][j]
                else:
                    value1[i][j]=max(value1[i-1][j],value1[i-1][j-weight[i-1]]+value[i-1])
                        # 背包总容量够放当前物体，取最大价值
        x=[0 for i in range(30)]
        j=c
        for i in range(30,0,-1):
            if value1[i][j]>value1[i-1][j]:
                x[i - 1]=1
                j -= weight[i-1]
        #创建面板
        firstPan = wx.Panel(self)
        title = wx.StaticText(firstPan,label="最优解",pos=(140,20))
        title = wx.StaticText(firstPan,label="最大价值为: %d"%value1[30][c],pos=(70,40))
        title = wx.StaticText(firstPan,label="背包中所装物品为：",pos=(70,60))
        count=80
        for i in range(30):
            if x[i]:
                title = wx.StaticText(firstPan,label="第 %d 个   "%(i+1),pos=(70,count))
                count = count+20
max_last = 0
#遗传算法
class Frame4(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title = "动态规划最优解",pos=(100,100),size=(900,900))
        #创建面板
        firstPan = wx.Panel(self)
        
        #算法
        # 记录上一代的最大值
       
        # 随机精选出四个个体
        # 用来初始化整个种群
        chromosomes_state1 = '100100100100100100100100100100'
        chromosomes_state2 = '101010101010101010101010101010'
        chromosomes_state3 = '010101010101010101010101010101'
        chromosomes_state4 = '101011101011101011101011101011'
        chromosomes_states = [chromosomes_state1, chromosomes_state2, chromosomes_state3, chromosomes_state4]

        union=[ [a,b] for a,b in zip(weight,value)]
        figure=list(range(1,31))
        x =dict(zip(figure,union))
        FINISH_LIMT = 0             # 定义终止界限
             
        # 重量界限
        WEIGHT_LIMIT = 10149
             
        # 染色体长度
        CHROMOSOME_SIZE =6
             
        # 精选次数
        SELECT_NUMBER = 4
             
        # 记录上一代和上上一代的适应函数的差
        diff_last = 10000
            # 计算种群的适应度
            # 将所有存入包中大的物品的重要的和作为当前种群的适应度
        def fitness(chromosomes_states):
            fitnesses = []
            for chromosomes_state in chromosomes_states:
                value_sum = 0
                weight_sum = 0
                # enumerate将数据对象组合为索引序列，同时列出数据下标和数据
                for i,v in enumerate(chromosomes_state):
                    if int(v)==1:
                        weight_sum += x[i+1][0]
                        value_sum += x[i + 1][1]
                fitnesses.append([value_sum,weight_sum])
            return fitnesses
            
            # 当这次的差异值和上次的差异值都小于终止界限
            # 就可以认为适应度函数这时候已经开始收敛了
            # 可以认为当前的种群已经达到最优的一代
        def is_finished(fitnesses):
            global max_last
            global diff_last
            max_current = 0
            # 获得当前的适应度函数的最大值
            for v in fitnesses:
                if v[1]>max_current:
                    max_current = v[1]
            diff = max_current - max_last
            # 判断差异值，来决定是否已经到达了最优的种群
            if diff<FINISH_LIMT and diff_last < FINISH_LIMT:
                return True
            else:
                    # 对最大值和和差异值进行更新
                diff_last = diff
                max_last = max_current
                return False
             
             
            # 精选下一代
            # 先淘汰掉不能适应环境的，即淘汰重量大于80的
            # 随机从上一代能适应环境的种群个体中选出几个个体进行下一代的繁衍
            # 记录下精选个体的位置(同一个个体可能被选多次)，因此slelect_index中可能有两个值是相同的
        def filter(chromosomes_states,fitnesses):
            index = len(fitnesses) - 1
            while index >= 0:
                index -= 1
                if fitnesses[index][1] > WEIGHT_LIMIT:
                    chromosomes_states.pop(index)
                    fitnesses.pop(index)
            select_index = [0] * len(chromosomes_states)
                # 开始进行精选
            for i in range(SELECT_NUMBER):
                j = chromosomes_states.index(random.choice(chromosomes_states))
                select_index[j] += 1
            return select_index
             
             
            # 产生下一代
            # 从精选的四个个体里面依次取一个个体，再从能适应环境的个体中随机的取一个个体
            # 交配产生新的下一代
        def crossover(chromosomes_states,select_index):
            chromosomes_states_new = []
            tmp = chromosomes_states[:]
            index = len(chromosomes_states) - 1
            while index >= 0:
                index -= 1
                chromosomes_state = tmp.pop(index)
                for i in range(select_index[index]):
                    chromosomes_state_x =random.choice(chromosomes_states)
                        # 随机产生基因序列的交配位置
                    pos = random.choice(range(1,CHROMOSOME_SIZE-1))
                    chromosomes_states_new.append(chromosomes_state[:pos]+chromosomes_state_x[pos:])
            return chromosomes_states_new
             
             
         
            # 让种群最多繁衍100代
        n = 100
        cloum = 40
        title = wx.StaticText(firstPan,label="当前种群的适应度",pos=(140,20))
        
        while n>0:
            n -= 1
                # 计算当前第100-i代种群的适应度
            row = 0
            fitnesses = fitness(chromosomes_states)
            for i in fitnesses:
                title = wx.StaticText(firstPan,label="[%d, %d]    "%(i[0],i[1]),pos=(row,cloum))
                row = row+100
                #print(i, end=' ')
            
            cloum=cloum+40
                # 利用相关条件判断当前的这一代是否能达到结束遗传的条件
            if is_finished(fitnesses):
                break
                # 精选
            select_index = filter(chromosomes_states,fitnesses)
                # 产生下一代
            chromosomes_states = crossover(chromosomes_states,select_index)
        count=40   
        title = wx.StaticText(firstPan,label="背包最大价值对应序列为",pos=(540,20))
        for i in chromosomes_states:
            title = wx.StaticText(firstPan,label="%s"%i,pos=(500,count))
            count = count+20           

        
if __name__=='__main__':
    app = wx.App()
    frame = Frame1(parent=None,id=1)
    frame.Show()
    app.MainLoop()
    conn=sqlite3.connect('data.db')
    cursor = conn.cursor()

    #cursor.execute('create table bag(weight int(10),value int(10))')#创建表
    
    for i in range(0,len(weight)):
        cursor.execute('INSERT INTO bag(weight,value) values ("%d","%d")' %(weight[i], value[i]))#插入数据
        conn.commit()
    
    #cursor.execute('delete from bag')
    cursor.execute('select *from bag')
    result=cursor.fetchall()
    print("数据库中背包的重量和价值为：")
    for i in result:
        print(i)
    cursor.close()
    conn.close()
