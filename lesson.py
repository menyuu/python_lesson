import math

num = 1
name = 'Mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok,type(is_ok))

n = '1'
new_num = int(n)
print(new_num, type(new_num))

print('Hi', 'Mike', sep=',', end='.\n')
print('Hi', 'Mike', sep=',')

print(2 + 2)

result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)

# print(help(math))

s = 'test'
print(s)
print('hello')
print("hello")
print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don't know\"")

print('hello.\nHow are you?')
print(r'C:\name\name')

print("################")
print("""\
line1
line2
line3\
""")
print("################")

print('Hi.' * 3 + 'Mike')

s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print(word[0:6:2])
print(word[:2])
print(word[2:])
word = 'j' + word[1:]
print(word[:])
n = len(word)
print(n)

s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

print('#############')
print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))

a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Name'
family = 'Family'
print(f'My name id {name} {family}. watashi ha {family} {name}')
