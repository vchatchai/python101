vec = [-4, -2, 0, 2, 4]

result = [x*2 for x in vec]
print("x * 2", result)

result = [x for x in vec if x >= 0]
print("if x >  0", result)

result = [abs(x) for x in vec]
print("abs(x)",result)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
result = [weapon.strip() for weapon in freshfruit]
print("freshfruit", result)

result = [(x, x**2) for x in range(6)]
print("power",result)

vec = [[1,2,3], [4,5,6], [7,8,9]]
result = [num for elem in vec for num in elem]
print('list in list', result)


from math import pi 
result = [str(round(pi, i)) for i in range(1,6)]
print('math :', result)