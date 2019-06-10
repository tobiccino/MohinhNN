import math
print("Hello! Đây là bài toán hỗ trợ cho việc tính toán với những hệ thống sử dụng mô hình hàng đợi")

# Một tiệm rửa xe có 1 nhân viên làm việc, mỗi
# ngày làm việc 8 giờ, mỗi giờ rửa TB được 6 xe,
# lương là 15.000đ/giờ. Mỗi giờ TB có khoản 4 xe
# vào để rửa. Giả sử chi phí chờ đợi của 1 khách
# là 20.000đ/giờ
# 1. Hãy tính toán các thông số của hệ thống và
# tổng chi phí một ngày?
# 2. Tính xác suất để có hơn 1, 2, 3 xe trong tiệm


lamda = input("Nhập giá trị của Lambda :" )
lamda = int(lamda)
muy = input("Nhập giá trị của Muy :" )
muy = int(muy)
sohangdoi = input("Nhập số hàng đợi của hệ thống :" )
time_lamviec = input("Nhập thời gian làm việc 1 ngày của nhân viên :" )
time_lamviec = int(time_lamviec)
luong_nv = input("Nhập lương của nhân viên"+"("+"$/t"+"):" )
luong_nv = int(luong_nv)
wait_price = input("Nhập chi phí chờ đợi của khách hàng - $/t :" )
wait_price = int(wait_price)


Ls = lamda /(muy-lamda)
Ws = 1/(muy-lamda)
Lq = lamda*lamda/(muy*(muy-lamda))
Wq = lamda/(muy*(muy-lamda))
rho = lamda/muy
Po = 1 - lamda/muy
n = input("Nhập n là số xe ít nhất có trong hệ thống :" )
n = int(n)
k = 3
PN = []
Pn_k = math.pow(rho,4)
i = 0
while i < n :
    Pi = (1-rho)*math.pow(rho,i)
    PN.append(Pi)
    i+=1
PI = 0
for item in PN :
    PI = PI + item
print("xác suất để có ít nhất "+str(n)+" xe trong hệ thống là : " , 1 - PI)
print("Số xe trung bình trong hệ thống : Ls = ", Ls)
So_xe_1_ngay = lamda * time_lamviec
print("Thời gian trung bình 1 xe trong hệ thống : Ws = ", Ws)
print("Số xe trung bình trong hàng đợi : Lq= ", Lq)
print("Thời gian chờ đợi trung bình trong hệ thống : Wq = ", Wq)
print("Số xe trung bình đến trong 1 ngày : ",So_xe_1_ngay)
time_wait_1_ngay = Wq * So_xe_1_ngay
print("Thời gian chờ đợi trung bình 1 ngày : ", time_wait_1_ngay)
chi_phi_wait = wait_price * time_wait_1_ngay
print("Chi phí chờ đợi trung bình 1 ngày :" ,chi_phi_wait)
luong_nv_1_ngay = time_lamviec * luong_nv
Cost = chi_phi_wait + luong_nv_1_ngay
print("Tổng chi phí trong 1 ngày là : ",Cost)