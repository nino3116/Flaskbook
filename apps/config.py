# 경로값을 알아오기 위하여
from pathlib import Path

baseDir = Path(__file__).parent.parent


# BaseConfig 클래스 작성
class BaseConfig:
    SECRET_KEY = "DM5Fq1G9XtMzWAeqYWNR"
    WTF_CSRF_SECRET_KEY = "El1oD921KMdGKONsydDa"
    # 이미지 업로드 경로에 apps/images를 지정한다.
    UPLOAD_FOLDER = str(Path(baseDir, "apps", "images"))
    # 물체 감지에 이용하는 라벨
    LABELS = [
        "unlabeled",
        "person",
        "bicycle",
        "car",
        "motorcycle",
        "airplane",
        "bus",
        "train",
        "truck",
        "boat",
        "traffic light",
        "fire hydrant",
        "street sign",
        "stop sign",
        "parking meter",
        "bench",
        "bird",
        "cat",
        "dog",
        "horse",
        "sheep",
        "cow",
        "elephant",
        "bear",
        "zebra",
        "giraffe",
        "hat",
        "backpack",
        "umbrella",
        "shoe",
        "eye glasses",
        "handbag",
        "tie",
        "suitcase",
        "frisbee",
        "skis",
        "snowboard",
        "sports ball",
        "kite",
        "baseball bat",
        "baseball glove",
        "skateboard",
        "surfboard",
        "tennis racket",
        "bottle",
        "plate",
        "wine glass",
        "cup",
        "fork",
        "knife",
        "spoon",
        "bowl",
        "banana",
        "apple",
        "sandwich",
        "orange",
        "broccoli",
        "carrot",
        "hot dog",
        "pizza",
        "donut",
        "cake",
        "chair",
        "couch",
        "potted plant",
        "bed",
        "mirror",
        "dining table",
        "window",
        "desk",
        "toilet",
        "door",
        "tv",
        "laptop",
        "mouse",
        "remote",
        "keyboard",
        "cell phone",
        "microwave",
        "oven",
        "toaster",
        "sink",
        "refrigerator",
        "blender",
        "book",
        "clock",
        "vase",
        "scissors",
        "teddy bear",
        "hair drier",
        "toothbrush",
    ]


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
    # 이미지 업로드처에 tests/detector/images를 지정한다.
    UPLOAD_FOLDER = str(Path(baseDir, "tests", "detector", "images"))


# 실제 상황
class DeployConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{baseDir / 'deploy.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# config 사전 매핑 작업
config = {"testing": TestingConfig, "local": LocalConfig, "deploy": DeployConfig}



    