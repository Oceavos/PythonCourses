이번에는 딕셔너리 자료형에서 사용하는 함수들에 대해 알아보자.

- 딕셔너리의 Key만 모아서 리스트로 리턴 (keys)

>>> dic = {'name' : 'SeongJin-Hong', 'gender' : 'male'}
>>> dic.keys()
dict_keys(['name', 'gender'])     # dict_keys 란 이름의 객체를 리턴해줌


- 딕셔너리의 Value만 모아서 리스트로 리턴 (values)

>>> dic = {'name' : 'SeongJin-Hong', 'gender' : 'male'}
>>> dic.values()
dict_values(['SeongJin-Hong', 'male'])        # dict_values 란 이름의 객체를 리턴

- Key를 이용한 Value값 얻기 (get)

>>> dic = {'name' : 'SeongJin-Hong', 'gender' : 'male'}
>>> dic.get('name')
'SeongJin-Hong'
>>> dic.get('gender')
'male'

- 딕셔너리 초기화 (clear)
>>> dic = {'name' : 'SeongJin-Hong', 'gender' : 'male'}
>>> dic.clear()         # 딕셔너리 값 초기화
{}

- Key, Value 쌍 얻기 (items)
>>> dic = {'name' : 'SeongJin-Hong', 'gender' : 'male'}
>>> dic.items()
dict_items([('name', 'SeongJin-Hong'), ('getnder', 'male')])     # dict_items 라는 객체로 리턴함
