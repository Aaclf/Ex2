import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import time

# 贪心算法
def tanXin(m, h, v):

    data = open("data.txt", "w+")
    start = time.time()
    arr = [(i, v[i] / h[i], h[i], v[i]) for i in range(len(h))]   # 计算权重, 整合得到一个数组
    arr.sort(key = lambda x: x[1], reverse = True)   # 按照list中的权重，从大到小排序,list.sort() list排序函数
    bagVal = 0
    bagList = [0] * len(h)

    for i, w, h, v in arr:
        if w <= m:   # 1 如果能放的下宝物，那就把宝物全放进去
            m -= h
            bagVal += v
            bagList[i] = 1
        else:   # 2 如果宝物不能完全放下，考虑放入部分宝物
            bagVal += m * w
            bagList[i] = 1
            break

    end = time.time()
    print('最大价值：', bagVal)
    print('最大价值：', bagVal, file=data)
    print('解向量：', bagList)
    print('解向量：', bagList, file=data)
    return bagVal


# 动态规划算法
def bag(n, m, w, v):

    value = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if j < w[i - 1]:
                value[i][j] = value[i - 1][j]
            else:
                value[i][j] = max(value[i - 1][j], value[i - 1][j - w[i - 1]] + v[i - 1])   # 背包总容量够放当前物体，取最大价值

    return value

def dongTai(n, m, w, value):

    data = open("data.txt", "w+")
    bagList = [0] * len(w)
    x = [0 for i in range(n)]
    j = m

    # 求出解向量
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            x[i - 1] = 1
            j -= w[i - 1]
    for i in range(n):
        if x[i]:
            bagList[i] = 1

    print('最大价值为:', value[n][m])
    print('最大价值为:', value[n][m], file=data)
    print("解向量：", bagList)
    print('解向量：', bagList, file=data)
    return value[n][m]


# 回溯算法
bestV = 0
curW = 0
curV = 0
bestx = None

def huiS(i):

    global bestV, curW, curV, x, bestx

    if i >= n:
        if bestV < curV:
            bestV = curV
            bestx = x[:]
    else:
        if curW + w[i] <= m:
            x[i] = 1
            curW += w[i]
            curV += v[i]
            huiS(i + 1)
            curW -= w[i]
            curV -= v[i]
        x[i] = 0
        huiS(i + 1)


# 散点图
def sanDt(w, v):

    plt.title("value-weight", fontsize = 20)   # 图名称
    plt.xlabel("weight", fontsize = 10)
    plt.ylabel("value", fontsize = 10)
    plt.axis([0, 100, 0, 100])   # 设置x,y轴长度
    plt.scatter(w, v, s = 20)   # 将数据传入x,y轴
    plt.show()


# 排序
def paiX(w, v):

    w1 = np.array(w)
    v1 = np.array(v)
    vw = v1 * (1 / w1)
    vw = abs(np.sort(-vw))
    print("价值/重量：（递减排序）", vw)


#窗口输入
def get_click():

    entry1 = e1.get()
    entry2 = e2.get()
    return entry1, entry2


#数据选择
def data_select():

    # 用户输入，选择要读取的数据
    (a, b) = get_click()
    t = int(a)
    if t == 0:
        a = np.loadtxt("E:/测试数据/beibao0.in")
    elif t == 1:
        a = np.loadtxt("E:/测试数据/beibao1.in")
    elif t == 2:
        a = np.loadtxt("E:/测试数据/beibao2.in")
    elif t == 3:
        a = np.loadtxt("E:/测试数据/beibao3.in")
    elif t == 4:
        a = np.loadtxt("E:/测试数据/beibao4.in")
    elif t == 5:
        a = np.loadtxt("E:/测试数据/beibao5.in")
    elif t == 6:
        a = np.loadtxt("E:/测试数据/beibao6.in")
    elif t == 7:
        a = np.loadtxt("E:/测试数据/beibao7.in")
    elif t == 8:
        a = np.loadtxt("E:/测试数据/beibao8.in")
    elif t == 9:
        a = np.loadtxt("E:/测试数据/beibao9.in")
    else:
        print("输入错误！")

    return a


#算法选择
def airthmetic_Select():

    a = data_select()
    a = a.ravel()
    m = int(a[0])  # 背包容量
    n = int(a[1])  # 物品个数
    h = 2 * n + 1
    print(a[2:h])
    i = 2
    w = []   # 物品重量
    v = []   # 物品价值
    while i < 2 * n + 2:
        if i % 2 == 0:
            w.append(a[i])
        else:
            v.append(a[i])
        i = i + 1
    w = list(map(int, w))
    v = list(map(int, v))

    # 用户输入，选择执行的算法
    (a1, b1) = get_click()
    s = int(b1)
    if s == 1:
        start = time.time()
        tanXin(m, w, v)
        end = time.time()
        data = open("data.txt", "a+")
        print("运行时间", end - start, "s", file=data)
        data.close()
        print("运行时间", end - start, "s")
    elif s == 2:
        start = time.time()
        value = bag(n, m, w, v)
        dongTai(n, m, w, value)
        end = time.time()
        data = open("data.txt", "a+")
        print("运行时间", end - start, "s", file=data)
        data.close()
        print("运行时间:", end - start, "s")
    elif s == 3:
        data = open("data.txt", "w+")
        start = time.time()
        x = [False for i in range(n)]
        huiS(0)
        bestV = float(bestV)
        print("最大价值：", bestV)
        print("最大价值：", bestV, file=data)
        print("解向量：", bestx)
        print("解向量：", bestx, file=data)
        end = time.time()
        print("运行时间", end - start, "s", file=data)
        print("运行时间:", end - start, "s")
        data.close()
    else:
        print("输入错误！")

    paiX(w, v)
    sanDt(w, v)


# 主程序
if __name__ == '__main__':

    win = tk.Tk()   # 创建一个窗口
    win.title('0-1背包问题')
    win.geometry('400x200+400+100')

    label1 = tk.Label(win,text = "请输入测试数据（0~9）:", fg = "black" ,font = ("宋体",12),
                     width = 30, height= 1,justify = "left", anchor = "n")  # 在窗口输出一个文本
    label1.pack()

    e1 = tk.Variable()   # 创建文本输入框
    entry1 = tk.Entry(win, textvariable=e1)
    entry1.pack()
    e1.set(" ")

    label2 = tk.Label(win, text="请选择算法（1.贪心，2.动态规划，3.回溯）：", fg="black", font=("宋体", 12),
                      width=50, height=1, justify="left", anchor="n")
    label2.pack()

    e2 = tk.Variable()
    entry2 = tk.Entry(win, textvariable=e2)
    entry2.pack()
    e2.set(" ")

    button2 = tk.Button(win, text="确定", command=get_click).pack()   # 创建按钮
    button3 = tk.Button(win, text="结束", command=exit).pack()

    win.mainloop()

    airthmetic_Select()
