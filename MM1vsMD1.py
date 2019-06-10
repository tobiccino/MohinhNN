import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 1, 0.01)
y = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
for item in x :
    y.append(item/(1-item))
    y1.append(item*(2-item)/(2*(1-item)))
    y2.append(item*item/(1-item))
    y3.append(item*item/(2*(1-item)))
    y4.append(item/(50*(1-item)))
    y5.append(item*(2-item)/(100*(1-item)))
    y6.append(item*item/(50*(1-item)))
    y7.append(item*item/(100*(1-item)))

plt.figure(1)
axis1 = plt.subplot()
axis1.set_title(
        "Đồ thị N phụ thuộc vào ρ")
axis1.step(x, y, label='M/M/1')
axis1.step(x, y1, label='M/D/1')
axis1.set_xlabel('ρ')
axis1.set_ylabel('N - Số yêu cầu')
axis1.legend()

plt.figure(2)
axis2 = plt.subplot()
axis2.set_title(
        "Đồ thị Nq phụ thuộc vào ρ")
axis2.step(x, y2, label='M/M/1')
axis2.step(x, y3, label='M/D/1')
axis2.set_xlabel('ρ')
axis2.set_ylabel('Nq - Số yêu cầu')
axis2.legend()

plt.figure(3)
axis3 = plt.subplot()
axis3.set_title(
        "Đồ thị T phụ thuộc vào ρ")
axis3.step(x, y4, label='M/M/1')
axis3.step(x, y5, label='M/D/1')
axis3.set_xlabel('ρ')
axis3.set_ylabel('s - thời gian')
axis3.legend()

plt.figure(4)
axis4 = plt.subplot()
axis4.set_title(
        "Đồ thị Tq phụ thuộc vào ρ")
axis4.step(x, y6, label='M/M/1')
axis4.step(x, y7, label='M/D/1')
axis4.set_xlabel('ρ')
axis4.set_ylabel('s - thời gian')
axis4.legend()
plt.show()