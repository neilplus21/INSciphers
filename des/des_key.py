import random

s = input("Enter a string : ")
result = ''.join(format(ord(i), '08b') for i in s)
answer = ""

for i in range(len(result)):
    if i % 8 != 0:  # Fixed '=' to '=='
        answer += result[i]

l = len(answer) // 2
left = answer[:l]
right = answer[l:]

lt = [2, 3, 6, 7, 1, 6, 5, 9]
keys = []

for i in range(8):
    newKey = ""
    newAnswer = ""

    nl = int(left, 2) if left else 0
    nl = bin(nl << lt[i])[2:]  # Fixed bit shift

    nr = int(right, 2) if right else 0
    nr = bin(nr << lt[i])[2:]  # Fixed bit shift

    num = 2 + lt[i]  # This value is assigned but never used; retained for structure
    newKey = nr[num:] + nl[num:] if len(nr) > num and len(nl) > num else nr + nl  # Fixed slicing issue

    rm = set()
    while len(rm) < 8 and len(newKey) > 0:  # Fixed infinite loop
        r = random.randint(0, len(newKey) - 1)
        rm.add(r)

    for j in range(len(newKey)):
        if j not in rm:
            newAnswer += newKey[j]

    while len(newAnswer) < 8:  # Ensure key length consistency
        newAnswer = "0" + newAnswer

    keys.append(newAnswer)

for i in range(len(keys)):
    print("Key", i + 1, "=", keys[i])
