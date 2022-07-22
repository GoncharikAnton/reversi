size = 8

lst = [x+1 for x in range(size)]
table = []
for i in range(size):
    rowList = []
    for j in range(size):
        rowList.append(0)
    table.append(rowList)



for i in range(size):
    if i == 0:
        print('     ', end='')
    print(f'{i + 1}' + ' | ', end='')
print('\n')

for index, lst in enumerate(table):
    print(f' {index + 1} |' + '   |' * size)
    print('---+' * (size + 1))



