import math

w = 8
h = 12

ggcd = math.gcd(8,12)

answer = w*h - ((w/ggcd+h/ggcd)-1)*ggcd

print(int(answer))