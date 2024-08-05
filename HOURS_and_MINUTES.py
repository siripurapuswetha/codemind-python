import math
x=int(input())
minu=x/60
sec=x%60
r=math.floor(minu)
print("{} Hour(s) {} Minute(s)".format(r,sec))