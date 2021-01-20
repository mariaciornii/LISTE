x=[10,8,7,6,4,3,2]
print("lista 1:",x)
y=sorted(x)
print("lista 2:",y)
y.sort(reverse=True)
print("lista 3:",y)
print(len(y))
print(max(y))
print(min(y))
x.extend([111])
print("lista 4:",x)
x[1]=222
print("lista 5:",x)