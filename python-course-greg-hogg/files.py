print('---write to a new file----')
with open('newfile.txt', 'w') as f:
    f.write('Hi!')

print('---print() to a file----')
with open('newfile.txt', 'w', encoding='utf-8') as f:
    print('overwrite file', file=f)
    print('use print() to a file!', file=f)
    pi = 3.14
    print(f'print a value to file: {pi}', file=f, flush=True)
    print(f'print a value to stdout: {pi}')
    
name="Python"
with open('file.txt', 'a') as f:
    f.write(f'\nHello, {name}!')
    
print('----read all file----')    
with open('file.txt', 'r') as f:
    print(f.read())

print('----read all lines----')    
with open('file.txt', 'r') as f:
    for line in f.readlines():
        print(line.rstrip())
        
print('----read line by line----')    
with open('file.txt', 'r') as f:
    for line in f:
        print(line.rstrip())

print('----read & write line by line----')    
with open('file.txt', 'r') as f1:
    with open('copy.txt', 'r+') as f2:
        for i, line in enumerate(f1):
            print(i, line.rstrip())
            print(i, line.rstrip(), file=f2)
        f2.seek(0)
        print(f2.read())

