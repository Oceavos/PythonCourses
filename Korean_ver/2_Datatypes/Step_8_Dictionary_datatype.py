이번에는 딕셔너리 자료형에 대해 알아보자.

먼저 딕셔너리(Dictinoary) 라는 뜻은 사전 이라는 뜻이다. 그렇다면 이 뜻을 자료형에 적용하면 어떤 형식으로 자료형이 될까

"성별" : "남자", "국적" : "대한민국"
이런 형태로 자료를 저장하는 방식을 딕셔너리 자료형 이라고 한다.

딕셔너리 자료형에서는 "Key" 와 "Value" 를 한쌍으로 갖게되는데 위 예제를 인용해서 말하자면

성별은 Key가 되고 남자는 Value 가 된다.

그럼 예제를 통해 공부해보고 딕셔너리를 만들어보자

>>> me = {'name':'Seongjin-Hong', 'Nationality':'Korea'}

Key는 name, Nationality가 되고, Value 는 Seongjin-Hong, Korea 가 된다.
Key는 무조건 문자열 혹은 문자가 오지않아도 된다.

변수가 와도 되며 숫자형이 와도 된다. 그밖에 자료형들을 Key값으로 갖게 할 수 있다.

다음 예제를 보며 익히자.

>>> test = {1: 'Hello, World!'}

>>> test_2 = {'Hello, World!', [1, 2]}

>>> test_3 = {1:2}

- 딕셔너리 쌍 추가

>>> me = {'name' : 'SeongJin-Hong'}     # me 라는 딕셔너리에 데이터 추가
>>> me['Nationality'] = 'Korea'         # me 라는 딕셔너리에 'Nationality' : 'Korea' 딕셔너리 쌍 추가
>>> me
{'name' : 'SeongJin-Hong', 'Nationality', 'Korea'}

물론 앞서 말했지만, 리스트형태도 딕셔너리 쌍으로 추가가 가능하다

- 딕셔너리 쌍 삭제
>>> me = {'name' : 'SeongJin-Hong', 'Nationality' : 'Korea'}
>>> del me['Nationality']           # me 딕셔너리에 있는 Nationality를 키로 갖는 쌍을 삭제
>>> me
{'name' : 'SeongJin-Hong'}

- 딕셔너리 사용

- Key를 이용해서 Value 값을 얻기

>>> test = {'name' : 'SeongJin-Hong', 'Nationality' : 'Korea'}
>>> test['name']        # test 딕셔너리에 name 을 Key로 갖는 Value를 반환해달라
SeongJin-Hong
>>> test['Nationality']      # test 딕셔너리에 Nationality 를 Key로 갖는 Value를 반환해달라
Korea

☆ 딕셔너리를 만들때 똑같은 키가 겹치지 않도록 해야 합니다.
