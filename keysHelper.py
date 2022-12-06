cashtags = 'your, multiple, cashtags, here'
cashtags = cashtags.split(",")
BEARER_TOKENS = ''
CONSUMER_KEYS= ''
CONSUMER_SECRETS= ''
ACCESS_TOKENS= ''
ACCESS_TOKEN_SECRETS= ''

for tags in cashtags:
    BEARER_TOKENS += (input(f'{tags}\'s BEARER TOKEN: ') + ',')
    CONSUMER_KEYS += (input(f'{tags}\'s CONSUMER KEY: ') + ',')
    CONSUMER_SECRETS += (input(f'{tags}\'s CONSUMER SECRET: ') + ',')
    ACCESS_TOKENS += (input(f'{tags}\'s ACCESS TOKEN: ') + ',')
    ACCESS_TOKEN_SECRETS += (input(f'{tags}\'s ACCESS TOKEN SECRET: ') + ',')
    print()

print('BEARER:')
print(BEARER_TOKENS)
print('CONSUMER KEY:')
print(CONSUMER_KEYS)
print('CONSUMER SECRETS:')
print(CONSUMER_SECRETS)
print('ACCESS TOKENS:')
print(ACCESS_TOKENS)
print('ACCESS SECRETS:')
print(ACCESS_TOKEN_SECRETS)

