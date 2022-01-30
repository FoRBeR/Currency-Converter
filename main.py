import requests
import json


def get_val(our_code, code):
    url = 'http://www.floatrates.com/daily/' + our_code.lower() + '.json'
    r = requests.get(url)
    jdict = json.loads(r.text)
    return jdict[code.lower()]['rate']


cache = dict()
our_code = input()
if our_code.lower() == 'usd':
    cache['usd'] = 1
    cache['eur'] = get_val(our_code, 'eur')
elif our_code.lower() == 'eur':
    cache['eur'] = 1
    cache['usd'] = get_val(our_code, 'usd')
else:
    cache['usd'] = get_val(our_code, 'usd')
    cache['eur'] = get_val(our_code, 'eur')

cod = input()
while cod != '':
    val = float(input())
    print('Checking the cache...')
    if cod.lower() in cache:
        print('Oh! It is in the cache!')
        final_val = val * cache[cod.lower()]
        print(f'You received {final_val:.2f} {cod.upper()}.')
    else:
        print('Sorry, but it is not in the cache!')
        cache[cod.lower()] = get_val(our_code, cod)
        final_val = val * cache[cod.lower()]
        print(f'You received {final_val:.2f} {cod.upper()}.')
    cod = input()
