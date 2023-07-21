def odd_even(type, data, mode):
    if type == 'L':
        data = data.split(' ')
        
    data = data[mode == 'Even'::2]
    print(data if type == 'S' else list(data))
    
print("*** Odd Even ***")
odd_even(*input('Enter Input : ').split(','))