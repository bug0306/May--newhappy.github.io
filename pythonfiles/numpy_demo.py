import numpy as np
import random

# 数组的生成
# t1 = np.array([23, 34, 32])
# print(t1)
# print(type(t1))
# t2 = np.array(range(10))
# print(t2)
# print(type(t2))
# t3 = np.arange(10)
# print(t3)
# print(type(t3))
# print(t3.dtype)
# t4 = np.array([1, 3, 4, 0, 0, 0, 43], dtype=bool)
# print(t4)
# print(type(t4))
# print(t4.dtype)
# t6 = t4.astype("int")修改类型
# print(t6)
# t7=np.array([random.random() for i in range(10)])
# print(t7)
# t8=np.around(t7,3)
# print(t8)

# # 数组的形状
# a1 = np.arange(12)
# print(a1.shape)
# a2 = np.arange(24)
# a3 = a2.reshape((2, 3, 4))
# print(a2)
# print(a3)
# 数组的计算
# a4 = np.array([[0, 2, 2, 7, 5, 4, 6, 8],
#                [1, 1, 34, 23, 45, 3, 21, 34],
#                [2, 3, 43, 45, 46, 46, 76, 12]])
# # a5=a4+8
# # a6=np.arange(24).reshape((3,8))
# # # print(a5)
# # # print(a6)
# # # print(a6+a4)
# # a7=np.array([0,1,2,3,4,5,6,7])
# # print(a4-a7)
# # print(a4.T)
# # print(a4.transpose())
# # print(a4[1:3])
# # print("*" * 100)
# # print(a4[[0, 2]])
# # print("*" * 100)
# # print(a4[:, 0:2])
# # print("*"*100)
# # print(a4[:,2:])
# # print("*"*100)
# # print(a4[1:3, 3:7])
# # # 选取不相邻的点(0,2)(1,4)(2,6)
# # print(a4[[0, 1, 2], [2, 4, 6]])
# # # ##****************************************重点
# # a5 = np.where(a4 < 8, 4, 34)
# # print(a5)
# # a6=a4.clip(8,20)
# # print(a6)
# a4[a4 < 8] = 0
# print(a4)
# a5=a4.astype("float")#改为浮点类型
# a5[1, 6] = np.nan
# print(a5)
# print(np.count_nonzero(a5))#非0个数
# print(a5!=a5)
# print(np.count_nonzero(a5!=a5))#nan不和任何数值相等
# print(np.sum(a5))
# print(np.sum(a4))#整体相加
# print(np.sum(a5,axis=0))#同一列相加
# print(np.sum(a4,axis=1))#同一行相加
# 求和：t.sum(axis=None)
# 均值：t.mean(a,axis=None)  受离群点的影响较大
# 中值：np.median(t,axis=None)
# 最大值：t.max(axis=None)
# 最小值：t.min(axis=None)
# 极值：np.ptp(t,axis=None) 即最大值和最小值只差
# 标准差：t.std(axis=None)
# 默认返回多维数组的全部的统计结果,如果指定axis则返回一个当前轴上的结果
# 建立一个4×2的矩阵c, c.shape[1]为第一维的长度，c.shape[0]为第二维的长度。
# >> > c = array([[1, 1], [1, 2], [1, 3], [1, 4]])
# >> > c.shape
# (4, 2)
# >> > c.shape[0]
# 4
# >> > c.shape[1]
# 2
#
# def find_ndarray(a1):
#     for i in range(a1.shape[1]):
#         temp_col = a1[:, i]
#         nan_num = np.count_nonzero(temp_col != temp_col)
#         if nan_num != 0:
#             temp_not_nan_col = temp_col[temp_col == temp_col]  # 当前一列中不为nan的array
#             # 选中当前为nan的值，把不为nan的均值赋给她
#             temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()
#     return a1
#
#
# if __name__ == '__main__':
#     a1 = np.arange(12).reshape((3, 4)).astype("float")
#     a1[1, 2:] = np.nan
#     print(a1)
#     a1 = find_ndarray(a1)
#     print(a1)
#数组的拼接
a1=[random.random() for i in range(12)]
a1=np.random.randint(5,10,12).reshape((3,4))
a2=np.arange(12).reshape((3,4))
print(np.vstack((a1,a2)))# vertically垂直
print(np.hstack((a1,a2)))# horizontally水平
# 获取最大值最小值的位置
#   np.argmax(t,axis=0)
#   np.argmin(t,axis=1)
# 创建一个全0的数组: np.zeros((3,4))
# 创建一个全1的数组:np.ones((3,4))
# 创建一个对角线为1的正方形数组(方阵)：np.eye(3)


