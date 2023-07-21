class funString():
    def __init__(self, string = ""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self):
        return len(self.string)

    def changeSize(self):
        change = lambda n: chr(n-32) if n > 90 else chr(n+32)
        return ''.join(change(ord(i)) for i in self.string)

    def reverse(self):
        return self.string[::-1]

    def deleteSame(self):
        l = []
        for i in self.string:
            if i not in l:
                l.append(i)
        
        return ''.join(l)


string, mode = input('Enter String and Number of Function : ').split()
res = funString(string)
command = res.size, res.changeSize, res.reverse, res.deleteSame
print(command[int(mode) - 1]())