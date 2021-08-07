from ichibaitem_ranking import get_api,ranking_to_csv

def test_ichibaitem_ranking():
    APP_ID = "1048230508650001298"
    genre_id = "110411"
    url=f"https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?applicationId={APP_ID}&format=json&page=1&genreId={genre_id}"

    res = get_api(url)
    assert len(res['Items']) >= 1

