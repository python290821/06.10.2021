
_class = 0
# outer loop
while _class < 3:
    _class += 1
    print('class', _class)

    # inner loop
    i = 0
    _sum = 0
    while i < 5:
        i += 1
        grade = int(input('please enter grade'))
        if grade < 0:
            break # goes to line 17
        if grade == 0:
            i -= 1
            continue # goes to line 11
        _sum += grade
    _avg = _sum / 5
    print('for class', _class, ' average is', _avg)
