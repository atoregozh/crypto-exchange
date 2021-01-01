from luno_python.client import Client
import configparser



def run_luno():
    config = configparser.RawConfigParser()
    config.read('secret.properties')

    luno_key_id = config.get('LunoSection', 'luno.key_id')
    luno_secret = config.get('LunoSection', 'luno.secret')
    c = Client(api_key_id=luno_key_id, api_key_secret=luno_secret)

    try:
        res = c.get_ticker(pair='XBTZAR')
        print(res)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    run_luno()