#qns 6a
def main():
    rat_1_weight = 1
    rat_1_rate = eval(input("what is the rate of weight gain by rat1 weekly?:"))
    week_count = 0
    while rat_1_weight < 1.25:
        rat_1_weight = rat_1_weight + rat_1_weight*(rat_1_rate/100)
        week_count += 1
        print(rat_1_weight)
    print(week_count)
main()
#qns 6b
def main2():
    rat_1_weight = 1
    rat_2_weight = 1
    rat_1_rate = eval(input("what is the rate of weight gain by rat1 weekly?:"))
    rat_2_rate = eval(input("what is the rate of weight gain by rat2 weekly?:"))
    week_count = 0
    while rat_1_rate <= rat_2_rate:
        print('Rat 1 should gain weight faster than rat 2. \nEnter rates again')
        rat_1_rate = eval(input("what is the rate of weight gain by rat1 weekly?:"))
        rat_2_rate = eval(input("what is the rate of weight gain by rat2 weekly?:"))
              
    while rat_1_weight <  1.1*rat_2_weight:
        rat_1_weight = rat_1_weight + rat_1_weight*(rat_1_rate/100)
        rat_2_weight = rat_2_weight + rat_2_weight*(rat_2_rate/100)
        week_count += 1
        print(rat_1_weight, rat_2_weight)
    print(week_count)
main2()
