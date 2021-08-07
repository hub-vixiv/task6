import urllib
import requests
import sys
import time

def get_api(url):
    ranking = requests.get(url).json()
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

def main():
    APP_ID = "1048230508650001298"
    genre_id = "110411"
    url=f"https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?applicationId={APP_ID}&format=json&page=1&genreId={genre_id}"
    ranking = get_api(url)
    print(len(ranking['Items']))
    ranking_to_csv(ranking)

if __name__ == '__main__':
    main()
