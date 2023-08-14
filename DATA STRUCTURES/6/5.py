string, *chars = input('Enter list[str]: ').split("'")[1::2]
lenght = len(chars)

def segment(index=0, text=string):
    if index >= lenght:
        return text == ''
    
    new_text = text.replace(chars[index], '')
    index += 1
    return segment(index, new_text) or segment(index, text)

print('text: str =', repr(string))
print('lang: list[str] =', chars)
print('segment(text, lang) ->', segment())