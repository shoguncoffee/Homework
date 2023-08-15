money, data = input('Enter Input (Money, Product) : ').split('/')
money = int(money)
price = list(map(int, data.split()))
m = len(price)

def pantip(index=-1, *product):
    index += 1
    
    if index <= m:
        s = sum(product)
        
        if s == money:
            print(*product)
            return 1
            
        elif s < money and index < m:
            return pantip(index, *product, price[index]) + pantip(index, *product)
    
    return 0

print(f'Krisada can purchase Product: {price} with: {money} Baht | {pantip()} Pattern')