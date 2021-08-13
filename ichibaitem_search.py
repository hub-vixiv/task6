import requests
import urllib
import sys

def get_api(url,params):

    # result = requests.get(url,params).json()
    result = requests.get(url,params)

    if not(300 > result.status_code >= 200):
        print("失敗")
        return None
    else:
        result = result.json()
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
    # url=f"https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?applicationId={APP_ID}&format=json&keyword={keyword}"
    args = sys.argv
    APP_ID = "1048230508650001298",
    format = "json",
    keyword = args[1]   #検索キーワード

    url=f"https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    params = dict(
        applicationId = APP_ID,
        format = format,
        keyword = args[1]   #検索キーワード
    )

    get_api(url, params=params)

if __name__ == '__main__':
    main()