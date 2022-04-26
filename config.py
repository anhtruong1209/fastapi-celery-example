# configs.py

"""===========Library=========="""
from pathlib import Path
from typing import Optional, List, cast
from pydantic import BaseSettings, Field, BaseModel
import logging, datetime
curr_time = datetime.datetime.now()


class LoggingConfig(BaseSettings):
    LOGGING_LEVEL: int = logging.INFO

class AppConfig(BaseModel):
    """Application configurations."""

    # question classification settings
    SPACY_MODEL_IN_USE: str = "ja_core_news_md"

    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    
    SETTINGS_DIR: Path = BASE_DIR.joinpath('settings')
    SETTINGS_DIR.mkdir(parents=True, exist_ok=True)

    LOGS_DIR: Path = BASE_DIR.joinpath('logs')
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    MODELS_DIR: Path = BASE_DIR.joinpath('models')
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    
    APP_DIR: Path = Path(__file__).resolve().parent.parent
    ASSETS_DIR: Path = APP_DIR.joinpath('assets')
    ASSETS_DIR.mkdir(parents= True, exist_ok=True)

    # Min Qualtity Speakers
    MIN_QUANTITY_SPEAKERS: Optional[int] = Field(
        2, env="MIN_QUANTITY_SPEAKERS")
    # Max Qualtity Speakers
    MAX_QUANTITY_SPEAKERS: Optional[int] = Field(
        3, env="MAX_QUANTITY_SPEAKERS")

    # Question classification model to use
    CLASSIFICATION_MODEL: Path = MODELS_DIR.joinpath(
        'sale_man_detection.sav')
    VERTORIZER: Path = MODELS_DIR.joinpath(
        'vectorizer.pk')
    
    # Criteria 4 - Template
    TEMPLATE_CRITERIA_SCORING_4: Path = ASSETS_DIR.joinpath(
        # 'template_criteria_scoring_4.csv'
        'template_4.csv'
    )
    SCORE_DATA: Path = ASSETS_DIR.joinpath(
        'scoredata.csv'
    )
    NAME_FILE: Path = ASSETS_DIR.joinpath(
        'feb_name2.csv'
    )
    # FOLDER CACHE
    CACHE_DIR: Optional[str] = "cache/"

    # Threshold comparing
    THRESHOLD_COMPARING: Optional[float] = 10.0
    
"""----------GLOBAL CONFIGUATIONS----------"""

class GlobalConfig(BaseSettings):
    # Create APP_CONFIG objects
    APP_CONFIG: AppConfig = AppConfig()
    # Create LOGGING_CONFIG objects
    LOGGING_CONFIG: LoggingConfig = LoggingConfig()

    # API settings
    API_NAME: Optional[str] =  None
    API_DESCRIPTION: Optional[str] =  None
    API_ENDPOINT: Optional[str] = None
    API_VERSION: Optional[str] = None
    API_DEBUG_MODE: Optional[bool] = None

    # CORSMiddleware Settings
    CORSMIDDLEWARE_MAX_AGE: Optional[int] = Field(None, env="CORSMIDDLEWARE_MAX_AGE")
    CORSMIDDLEWARE_ALLOW_CREDENTIALS: Optional[bool] = Field(None, env="CORSMIDDLEWARE_ALLOW_CREDENTIALS")
    CORSMIDDLEWARE_ALLOW_METHODS: Optional[list] = Field(None, env="CORSMIDDLEWARE_ALLOW_METHODS")
    CORSMIDDLEWARE_ALLOW_HEADERS: Optional[list] = Field(None, env="CORSMIDDLEWARE_ALLOW_HEADERS")
    CORSMIDDLEWARE_ALLOW_ORIGINS: Optional[list] = Field(None, env="CORSMIDDLEWARE_ALLOW_ORIGINS")

    # Define global variables with the Field class
    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    # Logging configuration file
    LOG_CONFIG_FILENAME: Optional[str] = Field(None, env="LOG_CONFIG_FILENAME")

    # Environment specific variables do not need the Field class  https://www.uvicorn.org/
    HOST: Optional[str] = None
    # PORT production
    PORT: Optional[int] = None
    # Name Queue 
    QUEUE_NAME: Optional[str] = None
    HOST_QUEUE: Optional[str] =  Field(None, env="HOST_QUEUE")
    PORT_QUEUE: Optional[str] = Field(None, env="PORT_QUEUE")
    
    # [critical|error|warning|info|debug|trace]
    LOG_LEVEL: Optional[str] =  Field(None, env="LOG_LEVEL")
    USE_COLORS: Optional[bool] =  Field(None, env="USE_COLORS")
    WORKERS: Optional[str] = Field(None, env="WORKERS")
    RELOAD: Optional[str] = Field(None, env= "RELOAD")
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    AWS_ACCESS_KEY_ID: Optional[str] =  None
    AWS_REGION_NAME: Optional[str] = None
    URL: Optional[str] = None
    
    LANGUAGE_CODE: Optional[str] = 'ja-JP'
    MEDIA_FORMAT: Optional[str] = 'mp4'
    JOB_EXECUTION_SETTINGS: Optional[dict] = {'AllowDeferredExecution': True}
    # Database setting
    DB: Optional[str] = None

    class Config:
        """Loads the dotenv file."""
        env_file: str = ".env"
        case_sensitive: bool = True


class DevAIConfig(GlobalConfig):
    """Development configurations."""

    class Config:
        env_prefix: str = "DEVAI_"
        
class DevAPPConfig(GlobalConfig):
    """Local configurations."""
    
    class Config:
        env_prefix: str = "DEVAPP_"

class StagingConfig(GlobalConfig):
    """Statging configurations."""
    
    class Config:
        env_prefix: str = "STAGING_"

class ProdConfig(GlobalConfig):
    """Production configurations."""

    class Config:
        env_prefix: str = "PROD_"

class FactoryConfig:
    """Returns a config instance depending on the ENV_STATE variable."""

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):
        if self.env_state == "devai":
            return DevAIConfig()

        elif self.env_state == "prod":
            return ProdConfig()
        
        elif self.env_state == "devapp":
            return DevAPPConfig()
        
        elif self.env_state == "staging":
            return StagingConfig()


settings = FactoryConfig(GlobalConfig().ENV_STATE)()
# print(settings.__repr__())
