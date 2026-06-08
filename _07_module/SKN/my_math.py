# 사용자 모듈
from IPython.lib.pretty import pretty

if __name__ == "__main__":
    print('my_math.py를 직접 실행함')
    pass
else:
    print("다른 .py에 my_math가 import 되었습니다.",__name__)
    print("*" *100)
    print("*" *100)


pi: float = 3.14

x: int = 20

def get_circle_area(r: float|int) -> float:
    return pi * (r ** 2)

# Private 변수 설정 - Python 특성상 강제 되진 않으나 외부에서 직접 호출은 지양하며 import * 에서 호출 제외
__z: str = "hello"






