#
#quad_zahl = []
#for k in range(1, 11):
#    if k%2 == 0:
#        quad_zahl.append(k)
#    else:
#        quad_zahl.append(k**2)
#        
#print(quad_zahl)
#

#quad_zahl = [k if k%2 == 0 else k**2 for k in range(1,11)]


sn = []
x = 0
n = 10
r = 0.5
a = 1
for k in range(0,n):
    x += a*r**k
    sn.append(x)
    
    
print(sn)