import matplotlib.pyplot as plt


sn = []
x = 0
n = 10
r = 0.5
a = 1
for k in range(0,n):
    x += a*r**k
    sn.append(x)
    
print(sn)

plt.plot(sn)