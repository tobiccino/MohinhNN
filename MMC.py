import math
print("Đây là bài toán hỗ trợ cho việc tính toán với những hệ thống sử dụng mô hình hàng đợi MMC")
import numpy as np
import matplotlib.pyplot as plt


lamda = input("Nhập giá trị của Lambda :" )
lamda = int(lamda)
print(lamda)
muy = input("Nhập giá trị của Muy :" )
muy = int(muy)
print(muy)
c = input("Nhập số kênh phục vụ của hệ thống :" )
c = int(c)
print(c)
t = input("Nhập thời gian quan sát : ")
t = int(t)


rho = lamda / (sohangdoi*muy)
A = 0
for n in range(0,c,1) :
    ngiaithua = 1
    for x in range(1,n+1,1) :
        ngiaithua = ngiaithua * x
    A = A + (1/ngiaithua) * ( math.pow(lamda/muy,n))
giaithua_c = 1
for x in range(1,c+1,1) :
    giaithua_c = giaithua_c * x
Po = float(1/(A + (1/giaithua_c) * math.pow(lamda/muy,c)*c*muy/(c*muy-lamda)))
# Po = format(Po,'.40f')
# print(Po)

Ls = Po * muy * math.pow(lamda/muy,c) /((giaithua_c/c) * math.pow(c*muy-lamda,2))  + lamda/muy
Ws = Po * muy * math.pow(lamda/muy,c) /((giaithua_c/c) * math.pow(c*muy-lamda,2))  + 1/muy
Lq = Ls - lamda/muy
Wq = Lq / lamda
k = t * lamda #so obj vao he thong
s = c * t / Ws
print("Hiệu suất của hệ thống : rho = ",rho)
print("Xác suất không có Obj nào trong hệ thống  : Po = ",format(Po,'.6f'))
print("Số Obj trung bình trong hệ thống : Ls = ",Ls)
print("Số Obj trung bình trong hàng đợi  : Lq = ",Lq)
print("Thời gian trung bình của Obj trong hàng đợi : Wq = ",Wq)
print("Thời gian trung bình của Obj trong hệ thống : Ws = ",Ws)
X = np.arange(0, c+40, 1)
Y =[]
for n in X :
    if n < c :
        giaithua_n = 1
        for x in range(1,n+1,1) :
            giaithua_n = giaithua_n * x
        Pn = (1/(giaithua_n) )* math.pow(lamda/muy,n) * Po
        Y.append(Pn)
    else :
        giaithua_c = 1
        for x in range(1,c+1,1) :
            giaithua_c = giaithua_c  * x
        Pn = (1/(giaithua_c) )* math.pow(lamda/muy,c) *math.pow(lamda/(c*muy),(n-c))* Po
        Y.append(Pn)


this_axis = plt.subplot()
this_axis.set_title(
        "Đồ thị giữa số lượng vật thể và xác suất có N vật trong hệ thống")
this_axis.step(X, Y,'-r')
this_axis.set_xlabel('Number of Objs')
this_axis.set_ylabel('Prob')
