from functools import lru_cache
from pydantic import BaseSettings
from os import environ
from typing import List

class _BaseSettings(BaseSettings):
    # INVALID_DOC_ERR: Callable = lambda x: f"{x}: Text PDF or Invalid File"
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
    ACCEPT_PDF: List[str] = [".pdf"]
    ACCEPT_IMAGE: List[str] = ['.jpg', '.png']
    ACCEPT_FILES: List[str] = ACCEPT_IMAGE + ACCEPT_PDF
    FILE_CONVERSION_LIST: List[str] = ['.jpeg']

    WHICH_LOGGER: str= environ.get('WHICH_LOGGER')
    
    APP_NAME: str = environ.get("APP_NAME")
    APP_VERSION: str = environ.get("APP_VERSION")
    ENV_NAME: str = environ.get("ENV_NAME")

    GMAIL_APP_PASSWORD: str = environ.get("GMAIL_APP_PASSWORD")
    TEST_EMAIL: str = environ.get("TEST_EMAIL")


    INPUT_BUCKET: str = environ.get('INPUT_BUCKET')
    AWS_REGION: str = environ.get('AWS_REGION')
    MONGO_URI: str = environ.get('MONGO_URI')
    MONGO_DB_NAME: str = environ.get('MONGO_DB_NAME')
    # ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    # DATA_DIR = os.path.join(ROOT_DIR, 'data')
    # COMPANY_ENUM_FILE: str = environ.get('COMPANY_ENUM_FILE')
    # BASE_DIR_FILES: Path = environ.get('BASE_DIR_FILES')

@lru_cache()
def get_settings() -> BaseSettings:
    return _BaseSettings()
