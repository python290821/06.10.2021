
number_of_countries = 5 #170
sum_yes = 0
sum_no = 0
sum_avoid = 0
sum_veto = 0

yes_code = 1
no_code = 2
avoid_code = 3
veto_code = 4

index = 1
while True:
    vote = int(input('please enter your vote'))
    if vote == yes_code:
        sum_yes += 1
    elif vote == no_code:
        sum_no += 1
    elif vote == avoid_code:
        sum_avoid += 1
    elif vote == veto_code:
        print('veto by country number', index)
        break
    else:
        print('illegal vote')
        continue
    index += 1
    if index == 171:
        break

if index == 171:
    print('============================================')
    print('yes results:', sum_yes)
    print('no results:', sum_no)
    print('avoid results:', sum_avoid)


