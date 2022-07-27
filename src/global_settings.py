import os

CLOUD_PAYMENTS_CONFIG = {
    'AUTH': {
        'auth_type': 'basic',
        'login': os.getenv('PAYMENTS_PUBLIC_ID', 'test'),
        'password': os.getenv('PAYMENTS_API_SECRET', 'test')
    },
    'BASE_URL': 'https://api.cloudpayments.ru',
    'REQUEST_TIMEOUT': 5,
    'CONNECT_TIMEOUT': 5,
}
