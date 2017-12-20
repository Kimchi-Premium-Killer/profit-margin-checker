import requests
import time

# 참고 할 사이트
# http://noplanlife.com/?p=1339
# http://pureani.tistory.com/4919

COIN_URL = "https://min-api.cryptocompare.com/data/pricemultifull?" \
           "fsyms=BTC,ETH,ETC,XRP,LTC,DASH,BCH,XMR,QTUM,ZEC,BTG" \
           "&" \
           "tsyms=BTC,KRW,BTC,USD"
EXCHANGE_URL = "https://api.manana.kr/exchange/rate.json"

def coin_info():
    # while True:
    #     time.sleep(1)

    r = requests.get(COIN_URL)
    print("COIN : ", r.json())

def exchange_info():
    r = requests.get(EXCHANGE_URL)
    print("EXCHANGE : ", r.json())

def main():
    coin_info()
    exchange_info()

if __name__ == "__main__":
    main()
