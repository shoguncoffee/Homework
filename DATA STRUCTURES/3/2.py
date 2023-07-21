data = [
    tuple(item.split()) for item in input('Enter Input : ').split(',')
]
seq = enumerate(data)
next(seq)

for i, (this_weight, _) in seq:
    print('-', this_weight)
    print(data[i-1::-1])
    for weight, sound in data[i-1::-1]:
        
        if weight < this_weight:
            data.remove((weight, sound))
            print(sound)
            
        else: break