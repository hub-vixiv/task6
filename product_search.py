import urllib
import requests
import sys

def get_api(url, params):
    # result = requests.get(url).json()
    result = requests.get(url,params)

    if not(300 > result.status_code >= 200):
        print("失敗")
        return None
    else:
        result = result.json()

        counter = 0 
        for product in result['Products']:
            counter += 1
            product_info = product['Product']

            print (f"【商品名】：{product_info['productName'][:20]:<20s}", end="")
            print (f"【最高値】：{product_info['maxPrice']:>6}円", end="")
            print (f"【最安値】：{product_info['minPrice']:>6}円")

        print(f"{'-'*30}\n【総　数】：{result['count']}件")

def main():
    APP_ID = "1048230508650001298"
    format = "json"
    args = sys.argv
    keyword = args[1]
    # url=f"https://app.rakuten.co.jp/services/api/Product/Search/20170426?applicationId={APP_ID}&format=json&keyword={keyword}"
    url=f"https://app.rakuten.co.jp/services/api/Product/Search/20170426"
    params = dict(
        applicationId = APP_ID,
        format = format,
        keyword = keyword
    )
    get_api(url, params=params)

if __name__ == '__main__':
    main()
