print("*** Fun with countdown ***")
num_list = input("Enter List : ").split()
num_list = list(map(int, num_list))

count_down_list = []
temp_list = []
last = num_list[0]

if last == 1:
    print('0.add [1]')
    count_down_list.append([1])

for i in range(1, len(num_list)):
    now = num_list[i]
    print(i, now, '->', end=' ')
    
    if last - now == 1:
        if now == 1:
            print('1.add')
            temp_list.append(last)
            temp_list.append(now)
            count_down_list.append(list(temp_list))
            temp_list.clear()

        else:
            print('2.append')
            temp_list.append(last)
    else:
        temp_list.clear()
        if now == 1:
            print('3.add [1]')
            count_down_list.append([1])
        
    last = now

print([len(count_down_list), count_down_list])