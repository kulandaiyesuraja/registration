import os,sys


def register():
    userlen = 20
    temp = input('Enter username')
    len(temp)
    temp = temp.encode()
    with open('database.txt/database.txt', 'ab+') as f:
        size = os.path.getsize('database.txt/database.txt')
        n = int(size/28)
        position = 0
        for i in range(n):
            f.seek(position)
            str = f.read(20)
            if temp in str:
                print('Username already exist')
                return
            position = position+28
        username = temp
    print('Enter password')
    print('Password must contain one uppercase and special character and must be 8 character')
    u = 0
    s = 0
    a = input()
    for i in range(0, len(a)):
        if a[i].isupper():
            a = u+1
        elif a[i] == '@' or a[i] == '$':
            s = s+1
    try:
        if u != 0 and s != 0 and len(a) <= 8:
            password = a
            password = password.encode()
        else:
            raise Exception('Invalid Password')
    except Exception as e:
        print('Password must contain one uppercase and special character and must be 8 character')
        exit()
    with open('database.txt/database.txt', 'a+b') as f:
        f.write(username + password)

        def login():
            pass
        userlen = 20
        user = input('Enter username')
        user = user + ((userlen-len(temp)) * '')
        user = user.encode()
        password = input('Enter password')
        password = password.encode()
        userinfo = user + password
        size = os.path.getsize('database.txt/database.txt')
        n = int(size/28)
    with open('database.txt/database.txt', 'rb') as f:
        position = 0
        for i in range(n):
            f.seek(position)
            str = f.read(28)
        if userinfo in str:
            print('Login successful')
            exit()
        position += 28
    print('Username and password does not match')
    return


def login():
    pass

while 1:
    print('Register\n2 . Login\n Exit')
    print('Enter your choice')
    c = int(input())
    if c == 1:
        register()
    elif c == 2:
        login()
    elif c == 3:
        exit()
    else:
        print('Invalid choice')
