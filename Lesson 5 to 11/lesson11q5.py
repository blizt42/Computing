import random as ran

def rolling():
    x = ran.randint(1,6)
    y = ran.randint(1,6)
    return x+y

expected = { 2:1/36, 3:1/18, 4:1/12, 5:1/9, 6: 5/36,\
                 7:1/6, 8:5/36, 9:1/9, 10:1/12, 11:1/18, 12: 1/36}
simulated ={} 
for i in range(1000):
    totalOf2Dice = rolling()
    if totalOf2Dice not in simulated:
        simulated[totalOf2Dice] = 1
    else:
        simulated[totalOf2Dice] = simulated[totalOf2Dice] + 1
print('{0:^5}{1:^20}{2:^20}'.format('Total','Simulated Percent','Expected percent'))
for total in sorted(simulated):
      print('{0:^5}{1:^20.2f}{2:^20.2f}'.format(total,simulated[total]/1000*100,\
                                          expected[total]*100))
#print(simulated)
