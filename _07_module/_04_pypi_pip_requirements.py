# PyPI(Python Package Index)
# 파이썬 패키지를 올리고 내려 받는 공식 저장소
import importlib

# pip: PyPI 에서 패키지 검색, 설치, 삭제 도구

# requirements.txt : 프로젝트에 필요한 패키지 목록을 적어두는 파일로 해당 패키지 목록을 이용하여 일괄 설치 가능
#                    (의존성 명시 파일)


# requirements.txt 예시 내용
# requirements.txt 예시 내용
sample_requirements = """
# 웹 요청 라이브러리
requests==2.32.3

# 환경변수 파일(.env) 로딩
python-dotenv>=1.0.1

# 테스트 도구
pytest~=8.3.0
"""


pip_commands = [
    "python -m venv .venv", # 가상 환경 생성 - 폴더로 생성됨 폴더명 - .venv
    ".venv\\Scripts\\activate", # windows
    "python -m pip --version",
    "python -m pip install requests", # requests 패키지 설치
    "python -m pip show requests", # requests 패키지 정보 출력
    "python -m pip freeze > requirements.txt", # 현재 가상 환경의 패키지 목록을 requirements.txt에 저장 (프로젝트 공유시)
                                               # 프로젝트마다 저장되어 있음
    "python -m pip install -r requirements.txt", #requirements.txt 내 패키지들을 install
    "python -m pip uninstall requests", # install 된 패키지 중 해당 패키지 제거
]


# 필수 패키지 목록
REQUIRED_PACKAGES = {
    'requests' : 'requests',
    'colorama' : 'colorama',
    'python-dotenv' : 'dotenv'
}

# 패키지 확인

from importlib import import_module
from importlib.metadata import version, PackageNotFoundError
from io import StringIO

def find_missing_packages() -> list[str]:
    """ requirements.txt 작성된 패키지가 설치되어 있는지 """

    missing_packages = [] # 설치 안된 패키지 저장 리스트

    for package_name in REQUIRED_PACKAGES:
        try:
            version(package_name) # 패키지 존재 시 버전 정보 문자열로 반환, 단, 해당 패키지 없을 시 PackageNotFoundError가 발생
        except PackageNotFoundError:
            missing_packages.append(package_name)

    return missing_packages

def print_installed_versions() -> None:
    """ 설치된 패키지 버전 출력"""
    for package_name in REQUIRED_PACKAGES:
        print(f"{package_name} == {version(package_name)}")

def print_import_results() -> None:
    """ 설치된 패키지를 실제 Python Module로 import 가능한지 확인 """
    for package_name, module_name in REQUIRED_PACKAGES.items():
        import_module(module_name)
        print(f"{package_name} == {module_name} import 성공")

missing_packages = find_missing_packages() # 설치되지 않은 패키지 리스트

if missing_packages: # 리스트 내부 요소 존재
    print("설치 되지 않은 패키지", missing_packages)
    for package_name in missing_packages:
        print(f"python -m pip install {package_name}")

else: # 리스트 내부 요소 X
    print('필수 패키지 모두 설치됨')
    print_installed_versions()
    print_import_results()

