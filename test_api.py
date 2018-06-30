import unittest
import json

API = "./mock_data/api.json"
RATE = "./mock_data/rate.json"

class Coin:
    def __init__(self):
        self.list = ["BTC", "ETH", "XRP", "GRS", "ADA"]
        self.exchange = json.load(open(RATE, "r"))
        self.rate = None

    def jsonify(self):
        return json.load(open(API, "r"))

    def get_rate(self):
        if self.rate:
            return self.rate
        for ratio in self.exchange:
            if ratio["name"] == "USDKRW=X":
                self.rate = ratio["rate"]
                return self.rate


class Test_test1(unittest.TestCase):
    def test_BTC_TYPE(self):
        fp = json.load(open(API, "r"))
        self.assertEqual(fp["RAW"]["BTC"]["BTC"]["TYPE"], "5")


    def test_exchange_rate(self):
        fp = json.load(open(RATE, "r"))
        yen_won = fp[0]
        self.assertEqual(yen_won["date"], "2018-01-13 07:01:57")
        self.assertEqual(yen_won["name"], "JPYKRW=X")
        self.assertEqual(yen_won["rate"], 9.541107263480457)

    def test_print(self):
        c = Coin()
        coin = c.jsonify()
        won_dollar = c.get_rate()
        for item in c.list:
            krw = float(coin["DISPLAY"][item]["KRW"]["PRICE"].replace(",", "")[2:])
            usd = round(float(coin["DISPLAY"][item]["USD"]["PRICE"].replace(",", "")[2:]) * won_dollar, 2)
            print("[ {0} ] KP : {1} % || ".format(item, round((krw - usd) / (usd * 100), 2)),
                  "KRW : {} / USD : {}".format(krw, usd))

if __name__ == '__main__':
    unittest.main()


