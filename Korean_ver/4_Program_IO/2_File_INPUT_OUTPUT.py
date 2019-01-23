이번에는 파일 입출력에 대해 알아보도록 하자.

파일 입출력이란 파일내에 원하는 문자열이나 값을 기록하고 그 값을 다시 불러와서 파이썬내에서 출력하는 행위를 말한다.

먼저 파일을 만들어보자.

>>> a = open("NewFile.txt", 'w')   # a객체를 만들고 NewFile.txt 란 파일을 만들고 쓰기모드로 전환
>>> a.close() # 객체를 닫음

여기서 쓰기모드란 파일이름 뒤에 나오는 w를 뜻하며, 다른 키워드는 r, w, a가 있다.

w - 쓰기모드 - 파일에 내용을 작성할때 사용함
r - 읽기모드 - 파일의 내용을 읽을때 사용함
a - 내용추가모드 - 기존 파일의 마지막을 기준으로 새로운 내용을 추가함

그럼 이번에는 파일을 만들고 작성까지 해보자.

>>> a = open("NewFile.txt", 'w')   # a객체를 만들고 NewFile.txt 란 파일을 만들고 쓰기모드로 전환
>>> a.write("Hello, World!\n")   # write로 Hello, World! 를 a객체내에 등록된 파일인 NewFile.txt 에 작성함
>>> a.close()  # 객체를 닫음

이런식으로 작성을 한다면 소스코드와 같은 디렉터리에 NewFile.txt 란 파일내에 Hello, World! 가 정상적으로 적혀있는것을 확인할 수 있다.

그럼 이제 원하는 파일내에 등록된 내용이 무슨내용인지 알아야 한다. 예제를 통해 알아보도록 하자.

>>> a = open("NewFile.txt", 'r')   # a객체를 만들고 NewFile.txt 을 읽기모드로 전환
>>> b = a.readline()  # a객체에 등록된 파일 첫번째줄을 읽고 그 값을 b에 저장
>>> print(b)  # b출력
>>> a.close()  # 객체를 닫음

결과는 Hello, World! 가 나오게된다.

그럼 이제 쓰고 읽기를 해보았다. 이제 남은건 기존 파일의 내용을 이어서 작성해야 한다. 예제를 보며 익혀보자.

>>> a = open("NewFile.txt", 'a')   # a객체를 만들고 NewFile.txt 을 내용추가모드로 전환
>>> a.write("이어서 작성!")
>>> a.close()

이제 결과를 확인하기위해 NewFile.txt를 확인해보자

이어서 작성! 이라는 문자열이 아래에 정상적으로 등록되어있는것을 확인할 수 있다.


문제 - readline() 함수는 한줄만 읽게되는데, 여러줄을 읽는 프로그램을 구현하시오.