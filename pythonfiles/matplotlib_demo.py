# coding="utf-8"
#
import matplotlib
from matplotlib import pyplot as plt
import random
#
# plt.figure(figsize=(20, 6), dpi=90)
# x = range(2, 26, 2)
# y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
# plt.plot(x, y)
# xtick_label=[i/2 for i in range(4,49)]
# plt.xticks(xtick_label)
# plt.yticks(range(min(y),max(y)+1))
# # plt.
# plt.savefig("./pic1.png")
# plt.show()
#
# # --------------------------------------------------------------------------------------------
# import matplotlib
# from matplotlib import pyplot as plt
# import random
# ##########################改变字体为中文
from matplotlib import rc

font = {'family': 'MicroSoft YaHei',
        'weight': 'bold',
        'size': 15}
matplotlib.rc("font", **font)
#######################################
# x = range(0, 120)
# y = [random.randint(20, 35) for i in range(120)]
# y2=[random.randint(20, 30) for i in range(60)]
# y2+=[random.randint(30, 35) for i in range(60)]
#
# plt.figure(figsize=(20, 4), dpi=90)
#
# plt.plot(x, y,label="南阳",color="r",linestyle="--")
# plt.plot(x,y2,label="郑州")
#
# _xtick_labels = ["10点{}分".format(i) for i in range(60)]
# _xtick_labels += ["11点{}分".format(i) for i in range(60)]
# plt.xticks(list(x)[::10], _xtick_labels[::10], rotation=270)
#
# plt.xlabel("时间")
# plt.ylabel("温度")
# plt.title("10-12点温度变化")
#
# plt.grid()
# plt.legend()#显示图例
# plt.show()

#
# # 散点图
# y_3 = [random.randint(10, 20) for i in range(31)]
# y_10 = [random.randint(15, 25) for i in range(31)]
# x = range(1, 32)
# x1 = range(50, 81)
# plt.scatter(x, y_3)
# plt.scatter(x1, y_10)
# plt.show()
#
# # 条形图
# plt.figure(figsize=(20,8),dpi=90)
# x = ["战狼", "速度与激情8", "西游伏魔", "变形金刚5", "摔跤吧爸爸", "加勒比海盗", "盗梦空间", "荒野猎人", "泰囧"]
# y = [51.7, 27.6, 20.3, 18.3, 24.5, 15.8, 29.3, 10.9, 7.8]
# plt.bar(x,y,width=0.3)
# plt.xticks(range(len(x)),x,rotation=45)
# plt.xlabel("电影名")
# plt.ylabel('票房')
# plt.title("内地票房前九")
# plt.show()


# # 垂直多条形图
# plt.figure(figsize=(20, 8), dpi=90)
# x = ["战狼", "速度与激情8", "西游伏魔", "变形金刚5", "摔跤吧爸爸", "加勒比海盗", "盗梦空间", "荒野猎人", "泰囧"]
# y_14 = [21.7, 17.6, 10.3, 8.3, 14.5, 15.8, 19.3, 10.9, 7.8]
# y_15 = [12, 13, 3, 4, 13, 3, 7, 8, 3]
# y_16 = [9, 3, 4, 2.3, 3.4, 5, 3, 1, 2.3]
#
# format=0.3
# x_14=list(range(len(x)))
# x_15=[i+format for i in range(len(x))]
# x_16=[i+2*format for i in range(len(x))]
#
# plt.barh(x, y_14, height=0.3,label="九月14日")
# plt.barh(x_15, y_15, height=0.3,label="九月15日")
# plt.barh(x_16, y_16, height=0.3,label="九月16日")
#
# plt.legend()
# plt.ylabel("电影名")
# plt.xlabel('票房')
# plt.yticks(x_15,x)
# plt.title("内地票房前九")
# plt.show()

# #直方图
# plt.figure(figsize=(20,8),dpi=90)
# x=[random.randint(78,150) for i in range(250)]
# d=3#组距
# bar_width=((max(x)-min(x))//d)
# print(bar_width)
# plt.hist(x,bar_width)
#
# plt.xticks(range(min(x),max(x)+d,d))
# plt.grid()
# plt.show()


plt.figure(figsize=(20, 8), dpi=90)
interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width=[5,5,5,5,5,5,5,5,5,15,30,60]
quantity=[836,2737,3723,3926,3596,1438,3723,642,824,613,215,57]

plt.bar(range(12),quantity,width=1)

_x=[i-0.5 for i in range(13)]
interval+=[150]
plt.xticks(_x,interval)
plt.show()



