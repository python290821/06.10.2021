
num = int(input('please enter a number'))
#den = int(input('please enter a number'))

# 1
while True:
    den = int(input('please enter a number'))
    if den != 0:
        break

# 2 -- same as 1
den = int(input('please enter a number'))
while den == 0:
    den = int(input('please enter a number'))


print(num / den)
