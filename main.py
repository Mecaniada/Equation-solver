#Write a Python program
# which solve the equation:

from sympy import symbols, solve, Eq

# ax+by=c
# dx+ey=f

print("This program will solve a 2nd degree equation that looks like this:\n\t ax + by = c\n\t dx + ey = f")
num_s = input('Enter value for a, b, c, d, e and f: ').split()
if len(num_s) < 6:
    print('You must enter all the neccesary numbers according to the equation.')
    quit()
values = list(map(int, num_s))
numbers = ['a', 'b', 'c', 'd', 'e', 'f']
num_dic = dict(zip(numbers, values))
solutions = {"Value for x":[], "Value for y":[]}
# print(num_dic) ## VERIFY ##
for k, v in num_dic.items():
    print(k + ' = ' + str(v))
# for ax + by = c
y = symbols('y')
x = (num_dic['c'] - num_dic['b'] * y)/num_dic['a']
# for dx+ey=f
#print('X is: ', x)
y = (num_dic['f'] - num_dic['d'] * x)/num_dic['e']
#print('Y is: ', y)
eq1 = Eq(x + y)
solve_eq1 = solve(eq1, 0)
#print(solve_eq1)
solved_Y = solve(solve_eq1)
#print('Solved y: ', solved_Y)

for key, value in solved_Y.items():
    y = int(value)
    solutions["Value for y"].append(y)
    x = (num_dic['c'] - num_dic['b'] * y) / num_dic['a']
    solutions["Value for x"].append(x)

print("x =", solutions["Value for x"])
print("y =", solutions["Value for y"])

### TAKE THE VALUES FROM A LIST INSIDE A DICTIONARY ###
for x1 in solutions["Value for x"]:
    print('x =', x1)
for y1 in solutions["Value for y"]:
    print('y =', y1)