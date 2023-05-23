VERSION = 0.1
DIRECTORY_INPUT = './data/input/'
DIRECTORY_OUTPUT = './data/output/'
DIRECTORY_MODELS = './models/'
DIRECTORY_LOGS = './logs/'
APP_BASE_URL = 'http://127.0.0.1/'

keys = (
    'invoice_id',
    'customer_id',
    'stream_id',
    'price',
    'view_count',
    'country',
    'year',
    'month',
    'day'
)

key_names = {
    'invoice': 'invoice_id',
    'customer_id': 'customer_id',
    'stream_id': 'stream_id',
    'price': 'price',
    'times_viewed': 'view_count',
    'country': 'country',
    'year': 'year',
    'month': 'month',
    'day': 'day',
    'total_price': 'price',
    'TimesViewed': 'view_count',
    'StreamID': 'stream_id'
}

key_types = {
    'invoice_id': int,
    'customer_id': int,
    'stream_id': int,
    'price': float,
    'view_count': int,
    'country': str,
    'year': int,
    'month': int,
    'day': int
}
