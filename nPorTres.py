import os
os.system('cls')

n = int(input("Suministre valor de n: "))

nn = int('{}{}'.format(n,n))
nnn = int('%s%s%s' % (n,n,n))

total = n + nn + nnn

print(total)