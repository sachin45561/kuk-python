h = "hello"

word = "Python"
for ch in word:
    print(ch)

word = "Python"
for index, ch in enumerate(word):
    print(index, ch)


print(h.capitalize())  # Output: Hello
print(h.upper())       # Output: HELLO
print(h.lower())       # Output: helloprint(h.title())       # Output: Hello
print(h.swapcase())    # Output: HELLO          
print(h.center(20, '*'))  # Output: *******hello********
print(h.ljust(20, '-'))   # Output: hello---------------
print(h.rjust(20, '+'))   # Output: +++++++++++++++hello
print(h.strip('h'))      # Output: ello
print(h.replace('l', 'x'))  # Output: hexxo 
print(h.split('e'))     # Output: ['h', 'llo']
print(h.find('l'))     # Output: 2  
print(h.index('e'))    # Output: 1
print(h.isalpha())     # Output: True
print(h.isdigit())     # Output: False
print(h.islower())     # Output: True
print(h.isupper())     # Output: False  
print(h.startswith('he'))  # Output: True
print(h.endswith('lo'))    # Output: True   
print(h.count('l'))    # Output: 2      
print(h.zfill(10))     # Output: 00000hello
print(h.encode())      # Output: b'hello'   
print(h.format())      # Output: hello
print(h.format_map({'h': 'H', 'e': 'E', 'l': 'L', 'o': 'O'}))  # Output: hello
print(h.isnumeric())   # Output: False      
print(h.isprintable()) # Output: True
print(h.partition('e')) # Output: ('h', 'e', 'llo')     
print(h.rpartition('l')) # Output: ('he', 'l', 'lo')
print(h.splitlines())  # Output: ['hello']  
print(h.translate(str.maketrans('hel', '123')))  # Output: 123lo
print(h.zfill(15))     # Output: 00000000000hello

print(h.removeprefix('he'))  # Output: llo
print(h.removesuffix('lo'))   # Output: hel 
print(h.isidentifier())  # Output: True
print(h.casefold())     # Output: hello
print(h.expandtabs())  # Output: hello
print(h.isascii())     # Output: True
print(h.rfind('l'))    # Output: 3
print(h.rindex('o'))   # Output: 4
print(h.isalnum())     # Output: True
print(h.join(['H', 'E', 'L', 'L', 'O']))  # Output: HhelloEhelloLhelloLhelloO
print(h.count('lo'))    # Output: 1 
print(h.encode('utf-8'))  # Output: b'hello'
print(h.expandtabs(4))  # Output: hello
print(h.translate(str.maketrans('', '', 'aeiou')))  # Output: hll

