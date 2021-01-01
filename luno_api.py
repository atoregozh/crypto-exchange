from luno_python.client import Client


def run_luno():
    c = Client(api_key_id="grk2h4dr99mhm", api_key_secret="Xy_LPW_vvTXm9sjAHNH4fXX4WWErJcgLMqtcFCVcXxQ")

    try:
        res = c.get_ticker(pair='XBTZAR')
        print(res)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print("Hello World - Luno API")
    run_luno()