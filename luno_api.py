from luno_python.client import Client


def run_luno():
    c = Client(api_key_id="", api_key_secret="")

    try:
        res = c.get_ticker(pair='XBTZAR')
        print(res)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print("Hello World - Luno API")
    run_luno()