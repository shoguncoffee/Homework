def triangle(size: int):
    border = size - 1
    ground = '.' * border + '*'
    drawing = [ground]
    
    for _ in range(border):
        ground = ground[1:] + '+'
        drawing.append(ground)

    return mirror(drawing)

def mirror(lines):
    for n, line in enumerate(lines):
        lines[n] = line + line[-2::-1]
        
    return lines

def draw(drawing):
    print(*drawing, sep='\n')

print('*** Fun with Drawing ***')
n = int(input('Enter input : '))

draw(mirror(triangle(n)))
bottom = reversed(triangle(2*n - 1))
next(bottom)
draw(bottom)