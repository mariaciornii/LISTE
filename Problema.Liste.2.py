with open("input.txt",'r') as f:
    x=list(eval(f.readline()))
print("lista 1:",x)
y=sorted(x)
print("lista 2:",y)
y.sort(reverse=True)
print("lista 3:",y)
print('Lungimea =', len(y))
print('Max =', max(y))
print('Min =', min(y))
x.extend([111])
print("lista 4:",x)
x[1]=222
print("lista 5:",x)