import urllib
import requests
import sys

def get_api(url):
    result = requests.get(url).json()
    
    print(f"【総　数】：{result['count']}件")
    print("-"*30)

    counter = 0 
    for product in result['Products']:
        counter +=1
        product_info = product['Product']

        print (f"【商品名】：{product_info['productName'][:20]:<20s}", end="")
        print (f"【最高値】：{product_info['maxPrice']:>6}円", end="")
        print (f"【最安値】：{product_info['minPrice']:>6}円")

def main():
    APP_ID = "1048230508650001298"
    args = sys.argv
    keyword = args[1]
    url=f"https://app.rakuten.co.jp/services/api/Product/Search/20170426?applicationId={APP_ID}&format=json&keyword={keyword}"
    get_api(url)


if __name__ == '__main__':
    main()
