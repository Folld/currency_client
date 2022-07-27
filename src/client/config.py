from enum import Enum
from typing import Optional
from aiohttp import BasicAuth
import global_settings


class AuthEnum(Enum):
    basic: str = 'basic'


DEFAULTS = {
    'AUTH': {
        'auth_type': AuthEnum.basic,
        'login': None,
        'password': None
    },
    'BASE_URL': 'https://api.cloudpayments.ru',
    'REQUEST_TIMEOUT': None,
    'CONNECT_TIMEOUT': None,
}


class Config:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__base_url: Optional[str] = None
        self.__auth: Optional[BasicAuth] = None
        self.__request_timeout: Optional[float] = None
        self.__connect_timeout: Optional[float] = None
        self.__config: dict = {}
        self.__init_config(DEFAULTS, external=global_settings.CLOUD_PAYMENTS_CONFIG)

    @property
    def config(self):
        return self.__config

    @property
    def auth(self):
        return self.__auth

    @property
    def request_timeout(self):
        return self.__request_timeout

    @property
    def connection_timeout(self):
        return self.__connect_timeout

    @property
    def base_url(self):
        return self.__base_url

    def __init_config(self, defaults: dict, external: Optional[dict] = None):
        """You can use global_settings in your project. But for example I'll use default config."""

        self.__config = defaults.copy()
        if isinstance(external, dict):
            self.__config.update(external)
        if 'AUTH' in self.config:
            self.__init_auth(**self.config['AUTH'])
        self.__base_url = self.config.get('BASE_URL')
        self.__request_timeout = self.config.get('REQUEST_TIMEOUT')
        self.__connect_timeout = self.config.get('CONNECT_TIMEOUT')

    def __init_auth(self, auth_type: AuthEnum, **kwargs):
        if AuthEnum(auth_type).value == 'basic':
            if kwargs.get('login') and kwargs.get('password'):
                self.__auth = BasicAuth(**kwargs)


config = Config()
