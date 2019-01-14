이번에느 튜플 자료형에 대해 알아보도록 하자.

튜플은 리스트와 매우 비슷하며 다른점은 리스트는 값을 수정할 수 있지만, 튜플은 값이 고정된다.

자바 프로그래밍을 공부한 사람은 알겠지만 final 변수와 비슷한 느낌이라고 할 수 있다.

그럼 튜플을 선언해보자.

>>> tuple_test = (1, 2, 3)
>>> tuple_test_2 = ('Hello' ,'World', 'Hello, World!)
>>> tuple_test
(1, 2, 3)
>>> tuple_test_2
('Hello', 'World', 'Hello, World!)

다시 말하지만 튜플의 값은 수정할 수 없다. 튜플의 요소값을 수정하려 하면 오류가 발생한다.

>>> del tuple_test[0]
TypeError: 'tuple' object does not support item assignment


- 튜플의 인덱싱, 슬라이싱
튜플의 인덱싱과 슬라이싱은 리스트이 인덱싱, 슬라이싱과 매우 흡사하다. 그래도 한번은 실습해보는것이 좋으므로 해보도록 하자.

>>> test = (1, 2, 3)
>>> test[0]
1
>>> test[2]
3

문자도 해보자

>>> test = (1, 2, 'Hello', 'World')
>>> test[2]
'Hello'
>>> test[3]
'World'


- 슬라이싱
>>> test = (1, 2, 3, 4)
>>> test[1:]
(2, 3, 4)

>>> test = (1:3)
(2, 3)



- 튜플의 연산

- 튜플 더하기

>>> tuple_1 = (1, 2, 3)
>>> tuple_2 = (4, 5, 6)
>>> tuple_1 + tuple_2         # tuple_1, tuple_2 두개의 튜플을 더한다.
(1, 2, 3, 4, 5, 6)

- 튜플 곱하기

>>> tuple_1 = (1, 2, 3)
>>> tuple_2 * 2
(1, 2, 3, 1, 2, 3)

- 튜플의 길이를 구해보자

>>> tuple_test = (1, 2, 3, 4)
>>> len(tuple_test)             # tuple_test 이름의 튜플의 길이를 반환해라
4
