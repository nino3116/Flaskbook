# 경로값을 알아오기 위하여
from pathlib import Path

baseDir = Path(__file__).parent


# BaseConfig 클래스 작성
class BaseConfig:
    SECRET_KEY = "DM5Fq1G9XtMzWAeqYWNR"
    WTF_CSRF_SECRET_KEY = "El1oD921KMdGKONsydDa"


# 상황데  따른 환경 설정 작업 (BaseConfig 클래스 각 상황별로 상속하여 처리)
# LocalTest 상황
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{baseDir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


# Testing 상황
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{baseDir / 'testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False


# 실제 상황
class DeployConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{baseDir / 'deploy.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# config 사전 매핑 작업
config = {"testing": TestingConfig, "local": LocalConfig, "deploy": DeployConfig}