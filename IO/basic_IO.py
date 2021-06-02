
print("Hello World")


# 이게 주석이구만
print("Mary\"s cosmetics")
print('hi')
print("abc", 1)     # abc 1    -> no Java


# printf, .format()
# 근데 이상한게 뒤가 5일때는 반올림 안되고 6부터 됨         
n = 5
f = 3.141592
print("%d + %.2f" %(n,f))   # 5 + 3.14   -> System.out.printf("%d, %.2f", n, f);  
n1 = 3
print('{0}/{1}={2:0.2f}'.format(n, n1, n/n1))   # 5/3=1.67   


# input
a = input('first: ')
b = input('second: ')
print('합:', int(a)+int(b))
print('합: ', int(input('a: ')) + int(input('b: ')))


# 골때리는거
print("ab" * 4)     # 이게 됨.. 각각 변수에 넣은뒤 *연산해도 됨
a = "a"             # 근데 각각 input으로 입력받으면 연산 안됨.
b = 2               # (can't multiply sequence by non-int of type 'str')
print(a * b)
