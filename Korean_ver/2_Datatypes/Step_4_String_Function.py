이번에는 문자열 자료형에서 사용하는 함수를 공부해보자.

- 문자열에서 문자의 위치 알려주기 (find)

>>> A = "Hello, World!"
>>> A.find('H')          # H가 처음나온 위치를 반환해준다.
0
>>> A.find('q')          # q가 처음나온 위치를 반환해야 하는데 없으므로 -1 을 반환한다.
-1


- 문자열에서 문자의 위치 알려주기 - 2 (index)

>>> A = "Hello, World!"
>>> A.index('H')
0
>>> A.index('q')
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    A.index('q')
ValueError: substring not found

find 함수와 다른건 find함수에서는 찾을 수 없으면 -1을 반환하지만 index 함수는 에러를 발생시킨다.
그럼 find 함수와 index 함수중 아무거나 사용해도 되나 라는 질의가 있을 수 있는데
경우에 따라 다르며 find 함수를 사용해서 못찾는 문자는 -1를 반환하고 그 -1의 값을 다른 변수에 저장하여 다시 재활용 할 수 있기 때문이다.

- 문자열에서 문자의 개수 세기 (count)

>>> A = "Hello, World!"
>>> A.count('l')
3

- 문자열 삽입 (join)
>>> ','.join('hello')
'h,e,l,l,o'

- 대소문자 변환 (upper, lower)

>>> A = 'hello, world!'
>>> A.upper()             # 소문자를 대문자로
HELLO, WORLD!

>>> A = 'HELLO, WORLD!'
>>> A.lower()             # 대문자를 소문자로
hello, world!


- 문자 지우기 (lstrip, rstrip, strip)

>>> A = ' Hello '
>>> A.lstrip()            # 왼쪽 공백 제거
'Hello '

>>> A = ' Hello '
>>> A.rstrip()            # 오른쪽 공백 제거
' Hello'

>>> A = ' Hello '
>>> A.strip()             # 양쪽 공백 제거
'Hello'

>>> A = 'PPPPPHELLOPPPPP'
>>> A.lstrip('P')         # 왼쪽의 P를 모두 제거
HELLOPPPPP

>>> A = 'PPPPPHELLOPPPPP'
>>> A.rstrip('P')         # 오른쪽의 P를 모두 제거
PPPPPHELLO

>>> A = 'PPPPPHELLOPPPPP'
>>> A.strip('P')          # 양쪽의 P를 모두 제거
HELLO


- 문자열 변경 (replace)

>>> A = "Hello, World!"
>>> A.replace('World', 'Python')
Hello, Python!


- 문자열 나누기 (split)
>>> A = "Hello, World!".split()        # 공백을 기준으로 문자열을 나눔
>>> print(A)
['Hello,', 'World!']

>>> A = "Hello, World!".split(',')     # , 을 기준으로 문자열을 나눔
>>> print(A)
['Hello', ' World!']
