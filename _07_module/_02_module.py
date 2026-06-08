"""
모듈이린 : .py 파일을 의미
프로그램된 코드 재사용성을 높이기 위해 module 단위로 코드를 관리
모듈에 작성된 변수, 함수, 클래그 등은 외부에서 import에 사용 가능
단, _, __으로 시작하는 이름은 내부용(Private)이라는 관례 존재
    -> 외부에서 사용하는 것은 지양

import * -> 모듈 내 모든 변수, 함수, 클래스 가져오기
         -> _, __가 붙은 것들은 자동으로 제외

파이썬 내장 모듈 math 가져오는 법
-> import math
"""

# import math
# from idlelib import __main__
#
# print('math .pi :', math.pi)
#
# # dir : 모듈 내 사용가능 함수 확인
#
# print('dir(math) :', dir(math))
#
# print('dir() :', dir())

# 모듈명 확인
# - import 시 모듈명.py
# - 모듈 실행 시 '__main__' 뱐환
# print('__name__ :', __name__)

print('-'*100)


"""
사용자 정의 모듈 가져오기
파이썬 패키지 가져오기 
"""

# from SKN import my_math # from -> 파일 위치, import -> 사용할 모듈
#
# print('my_math.pi :', my_math.pi)
# print('my_math.x :', my_math.x)
# print('반지름 10 :', my_math.get_circle_area(10))
# print('dir(my_math) :', dir(my_math))
# print('my_math.__z :', my_math.__z) # 가져올 수 있지만 권장하지 않음

""" import * 사용법 """

# from SKN.my_math import *
#
# print('pi :', pi)
# print('x :', x)
# print('get_circle_area(10):', get_circle_area(10))
# print('__z :', __z) NameError: name '__z' is not defined

""" import 모듈 별칭 처리 """

# import 모듈명, import 패키지명.모듈명: 지정된 모듈 가져오기
# -> 사용법 : 모듈명.변수명 | 패키지명.모듈명.변수멸

# 별칭 처리 as 사용 : from 패키지명 import 모듈명 as(alias) 별칭
# -> 사용법 : 별칭.변수명

from SKN import my_math as mm # 많이 사용됨

print('mm.x', mm.x)
print('mm.pi', mm.pi)
print('mm.get_circle_area(10)', mm.get_circle_area(10))

"""
import *을 이용해서 가져 오는 것 보다 import 모듈명 | import 모듈명 as 별칭 이 권장 됨
- 함수명 변수명 충돌 방지와 가독성 상승
"""

# 현재 모듈의 이름 반환
# if __name__ == __main__: # 현재 모듈을 import 할 때 하위 코드 실행 방지
#     pass







