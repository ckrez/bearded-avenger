import os

VALID_FILTERS = ['indicator', 'confidence', 'provider', 'itype', 'group', 'tags', 'rdata']

LIMIT = 5000
LIMIT = os.getenv('CIF_ES_LIMIT', LIMIT)

LIMIT_HARD = 500000
LIMIT_HARD = os.getenv('CIF_ES_LIMIT_HARD', LIMIT_HARD)

WINDOW_LIMIT = 250000
WINDOW_LIMIT = os.getenv('CIF_ES_WINDOW_LIMIT', WINDOW_LIMIT)

TIMEOUT = '120'
TIMEOUT = os.getenv('CIF_ES_TIMEOUT', TIMEOUT)
TIMEOUT = '{}s'.format(TIMEOUT)

UPSERT_MODE = os.getenv('CIF_STORE_ES_UPSERT_MODE', False)
if UPSERT_MODE == '1':
    UPSERT_MODE = True

PARTITION = os.getenv('CIF_STORE_ES_PARTITION', 'month')

DELETE_FILTERS = os.getenv('CIF_STORE_ES_DELETE_FILTERS', 'id, indicator, provider')
DELETE_FILTERS = DELETE_FILTERS.split(',')
DELETE_FILTERS = list(set((x.strip() for x in DELETE_FILTERS)))
