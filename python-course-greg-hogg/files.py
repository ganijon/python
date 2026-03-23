print('# Let\'s write to a new file')
with open('newfile.txt', 'w') as f:
    f.write('Hi!')

print('# Then print() to a file')
with open('newfile.txt', 'w', encoding='utf-8') as f:
    print('overwrite file', file=f)
    print('use print() to a file!', file=f)
    pi = 3.14
    print(f'print a value to file: {pi}', file=f, flush=True)
    print(f'print a value to stdout: {pi}')

print('# Now, append some text to a file')
name="Python"
with open('file.txt', 'a') as f:
    f.write(f'\nHello, {name}!')
    
print('# Then, just read all of it')    
with open('file.txt', 'r') as f:
    print(f.read())

print('# Try read all lines, but print by line')    
with open('file.txt', 'r') as f:
    for line in f.readlines():
        print(line.rstrip())
        
print('# Try read line by line')    
with open('file.txt', 'r') as f:
    for line in f:
        print(line.rstrip())

print('# Finally, read from one file by line & write to another file with line numbers')    
with open('file.txt', 'r') as f1:
    with open('copy.txt', 'r+') as f2:
        for i, line in enumerate(f1):
            print(i, line.rstrip())
            print(i, line.rstrip(), file=f2)
        f2.seek(0)
        print(f2.read())

