# 存储人口数据（单位：百万）
a = 5.08  # 2004年
b = 5.33  # 2014年
c = 5.55  # 2024年

# 计算变化量
d = b - a  # 2004到2014的变化
e = c - b  # 2014到2024的变化

# 比较变化量
if d > e:
    print("2004-2014年的增长更快")
else:
    print("2014-2024年的增长更快")

# 回答老师的问题：人口增长是在加速还是减速？
# Answer: Population growth is decelerating (减速), because d (0.25) is larger than e (0.22).
X = True
Y = False
W = X or Y
print(W)

# Truth table for W (X or Y):
# X=True,  Y=True  => W=True
# X=True,  Y=False => W=True
# X=False, Y=True  => W=True
# X=False, Y=False => W=False