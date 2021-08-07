import requests
import urllib
import sys


def get_api(url):
    result = requests.get(url).json()

    print(f"【総　数】：{result['count']}件")
    print("-"*30)

    counter = 0 
    for item in result['Items']:
        counter +=1
        item_info = item['Item']
        print (f"【商品名】：{item_info['itemName'][:50]}...")
        print (f"【価　格】：¥{item_info['itemPrice']}")


def main():
    # keyword = "鬼滅"
    # url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1019079537947262807".format(
    # keyword)
    APP_ID = "1048230508650001298"
    args = sys.argv
    keyword = args[1]
    url=f"https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?applicationId={APP_ID}&format=json&keyword={keyword}"
    get_api(url)


if __name__ == '__main__':
    main()
