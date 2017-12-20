import requests

# 참고 할 사이트
# http://noplanlife.com/?p=1339 (requests 모듈 사용)
# http://pureani.tistory.com/4919

COINS = ["BTC", "ETH", "ETC", "DASH", "QTUM",
         "XRP", "GRS", "BTG", "BCH", "EMC2"]

COIN_URL = "https://min-api.cryptocompare.com/data/pricemultifull?" \
           "fsyms={0}" \
           "&" \
           "tsyms=BTC,KRW,BTC,USD".format(",".join(COINS))

EXCHANGE_URL = "https://api.manana.kr/exchange/rate.json"



coin = 0
exchange = 0

def coin_info():
    global coin
    r = requests.get(COIN_URL)
    coin = r.json()
    print("COIN : ", r.json())

def exchange_info():
    global exchange
    r = requests.get(EXCHANGE_URL)
    exchange = r.json()
    print("EXCHANGE : ", r.json())

def kimchi_premium():
    print("kimchi")
    # 코인의 현재가격(우리나라꺼, 해외꺼)
    # 환율
    for _coin in COINS:
        krw = float(coin["DISPLAY"][_coin]["KRW"]["PRICE"].replace(",", "")[2:])
        usd = float(coin["DISPLAY"][_coin]["USD"]["PRICE"].replace(",", "")[2:]) * exchange[1]["rate"]
        # print("KRW : {} / USD : {}".format(krw, usd))
        print("[{0}] kimchi-premium : {1} % || ".format(_coin, round((krw - usd) / usd * 100, 2)), "KRW : {} / USD : {}".format(krw, usd))


def main():
    coin_info()
    exchange_info()

    while(not coin and not exchange): pass

    kimchi_premium()

if __name__ == "__main__":
    main()
