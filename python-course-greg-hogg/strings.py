name = "GG"
age = 20

s1 = f"Hello, {name}. You are {age} years old."
s2 = "Hello, {}. You are {} years old.".format(name, age)
s3 = "Hello, {name}. You are {age} years old.".format(name=name, age=age)
s4 = "1234567890"

print(s1)
print(s2)
print(s3)
print(s4)

# strings are immutable
print(s1[0]) # you can read
try:
    s1[0] = 'B'  # you can't update
    print("this won't print")
except TypeError as e:
    print(e)

#s1[0] = 'B'  # you can't update it

# iterate over string
for c in s1:
    print(c, end=' ')
    
print("\ncapitalize:", s1.capitalize())
print("casefold:", s1.casefold())
print("center(10,'.'):", s1.center(100, '.'))
print("count('a'):", s1.count("a"))
print("encode:", s1.encode())
print("endswith('.'):", s1.endswith("."))
print("expandtabs:", s1.expandtabs())
print("find('x'):", s1.find("x"))
print("index('a'):", s1.index('a'))
print("isalnum:", 'a1b2'.isalnum())
print("isalpha:", s1.isalpha())
print("isascii:", s1.isascii())
print("isdecimal:", s1.isdecimal())
print("isdigit:", s1.isdigit())
print("isidentifier:", 'class'.isidentifier())
print("islower:", s1.islower())
print("isnumeric:", s1.isnumeric())
print("isprintable:", s1.isprintable())
print("isspace:", s1.isspace())
print("istitle:", s1.istitle())
print("isupper:", s1.isupper())
print("s1.join(s2):", s1.join(s2))
print("ljust(100,'.'):", s1.ljust(100, '.'))
print("lower:", s1.lower())
print("lstrip:", s1.lstrip())
# s1.maketrans()
print("partition(' '):", s1.partition(" "))
print("replace('a','A'):", s1.replace("a", "A"))
print("rfind('a'):", s1.rfind("a"))
print("rindex(' '):", s1.rindex(" "))
print("rjust(100,'.'):", s1.rjust(100, '.'))
print("rpartition(' '):", s1.rpartition(' '))
print("rsplit:", s1.rsplit())
print("rstrip:", s1.rstrip())
print("split:", s1.split())
print("splitlines:", s1.splitlines())
print("startswith('Hello'):", s1.startswith("Hello"))
print("strip:", s1.strip())
print("swapcase:", s1.swapcase())
print("title:", s1.title())
print("translate([]):", s1.translate([]))
print("upper:", s1.upper())
print("zfill(10):", s4.zfill(20))