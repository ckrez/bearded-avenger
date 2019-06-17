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

REQUEST_TIMEOUT = 60
REQUEST_TIMEOUT = os.getenv('CIF_ES_REQ_TIMEOUT', REQUEST_TIMEOUT)

UPSERT_MODE = os.getenv('CIF_STORE_ES_UPSERT_MODE', False)
if UPSERT_MODE == '1':
    UPSERT_MODE = True

PARTITION = os.getenv('CIF_STORE_ES_PARTITION', 'month')

UPSERT_MATCH = os.getenv('CIF_STORE_ES_UPSERT_MATCH', 'indicator, provider, confidence, tags, group, tlp, rdata')
UPSERT_MATCH = UPSERT_MATCH.split(',')
UPSERT_MATCH = set((x.strip() for x in UPSERT_MATCH))

# es agg searches for feeds
AGG_ENABLED = os.getenv('CIF_STORE_ES_AGG_MODE', False)
if AGG_ENABLED in [1, '1']:
    AGG_ENABLED = True
else:
    AGG_ENABLED = False
