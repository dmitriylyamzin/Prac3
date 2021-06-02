import random

def reverse(b, a):
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    x = 0
    y = 0
    q = 0
    r = 0
    while b!=0:
        q = a//b
        r = a%b
        x = x2 - q*x1
        y = y2 - q*y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    return y2

def SimplePow (a, k, n):
    #b = a**k % n
    k = bin(k)
    b = 1
    k=k[2:]
    if k != '0':
        A = a
        if int(k[-1]) == 1:
            b = a
        for i in range (1, len(str(k))):
            A = A*A % n
            if int(k[len(str(k)) - i - 1]) == 1:
                b = (A*b) % n
    return b

def FermaTest (n):
    if n % 2 == 0:
        return False
    else:
        for i in range (1000):
            a = random.randint(2, n - 1)
            r = SimplePow (a, n - 1, n)
            if r != 1:
                return False
        return True

def RSA_Alice_1 ():
    p = ''
    for i in range (random.randint(30,200)):
        p += str(random.randint(0,9))
    p_len = len(p)
    p = int(p)
    while (not FermaTest(p)):
        p+=1
    q = ''
    for i in range (p_len - 1):
        q += str(random.randint(0,9))
    q = int(q)
    while (not FermaTest(q)):
        q+=1   
    n = p*q
    fn = (p-1)*(q-1)
    e= random.randint(1, 1000000000000)
    while (not FermaTest(e)):
        e+=1     
    d = reverse (e, fn)
    return [e, n, d]

def RSA_Bob (e, n, m):
    c = []
    result = ''
    for i in range (len(m)):
        c += [SimplePow (int (m[i])%n, e, n)]
        result += alphabet[c[i]%101]
    return result

def RSA_Alice_2 (c, d, n, alphabet):
    m = []
    result = ''
    for i in range (len(c)):
        m += [SimplePow (int (c[i])%n, d, n)]
        result += alphabet[m[i]%101]
    
    
    return result

alphabet= "`~!@\"№#$;%:^?&*()_-+{}[]\|/'.,<>1234567890abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
line = input("Введите открытый текст или шифртекст и через пробел укажите длину блоков, на которые надо разбивать введённую строку при шифровании/расшифровании:\n").lower()
text = line.split()[0]
length = int(line.split()[1])
letters = []
for i in text:
    letters.append(str(alphabet.find(i)))
blocks = letters
if length > 1:
    blocks = []
    current_length = 0
    current_block = 0
    for w in letters:
        if current_length < length:
            current_block += int(w)
            current_length +=1
        else:
            current_block += int(w)
            current_block %= 101
            current_length = 0
            blocks.append(current_block)
            current_block = 0
            
text = blocks
key_string = input ("Введите ключевую пару - значения e, n и d, разделённые одним пробелом. Если вы хотите сгенерировать ключевую пару, введите 1:\n")
key = key_string.split()
if key_string == "1":
    key = RSA_Alice_1()
e = int(key[0])
n = int(key[1])
d = int(key[2])
print("e: ", e)
print("n: ", n)
print("d: ", d)
action_type = input("Выберите операцию, которую вы хотите осуществить, нажав на соответствующую цифру на клавиатуре:\n 1. Зашифрование\n 2. Расшифрование\n")
choose_flag = 0
while choose_flag == 0:
    if action_type == "1":
            print (RSA_Bob (e, n, text))
            choose_flag = 1
    elif action_type == "2":
            print (RSA_Alice_2 (text, d, n, alphabet))
            choose_flag = 1
    else:
            action_type = input("Вы должны ввести цифру от 1 до 2 и ничего более:\n 1. Зашифрование\n 2. Расшифрование\n")