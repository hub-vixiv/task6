import urllib
import requests
import sys
import time
import datetime as dt

def get_api(url, params):
    # ranking = requests.get(url).json()
    ranking = requests.get(url,params)

    if not(300 > ranking.status_code >= 200):
        print("失敗")
        return None
    else:
        ranking = ranking.json()
    return ranking

def ranking_to_csv(ranking):

    need_keys =['rank','itemName','itemPrice','shopName','itemUrl']

    with open("ranking_list.csv", mode='w', encoding='utf-8') as f:
        f.write("順位,商品名,価格,ショップ名,商品URL")
        for item in ranking['Items']:
            item_info = item['Item']
            for key in need_keys:
                f.write(f"{item_info[key]},")
            f.write("\n")
        now_time = dt.datetime.now()
        f.write(f"{'-'*20}上位{len(ranking['Items'])}件 {now_time:%Y%m%d-%H%M%S}　現在 {'-'*20}")

def main():
    APP_ID = "1048230508650001298"
    format = "json"
    genre_id = "110411"     #分類コード
    # url=f"https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?applicationId={APP_ID}&format=json&page=1&genreId={genre_id}"
    url=f"https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?"
    params = dict(
        applicationId = APP_ID,
        format = format,
        page = "1",
        genreId = genre_id
    )
    ranking = get_api(url, params=params)
    print(len(ranking['Items']))
    ranking_to_csv(ranking)

if __name__ == '__main__':
    main()
