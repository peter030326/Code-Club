print('정수 N을 입력하면 N번째 소수를 출력하는 프로그램입니다')
n = input('N을 입력하세요 :')
prime_numbers = []
x = 1
while True:
    x += 1
    for y in range(2, x):
        if x % y == 0:
            break
        else:
            prime_numbers.append(x)
            if len(prime_numbers) == n:
                print(x)
                break
# https://wikidocs.net/60
# https://www.youtube.com/watch?v=V9bTS16hCS0&list=PLGPF8gvWLYyrkF85itdBHaOLSVbtdzBww&index=7
