import requests
import json

base_url = "https://jsonmock.hackerrank.com/api/countries/search?name="
def getCountries(s, p):
    res = requests.get(base_url + s)
    res_json = json.loads(res.text)
    result = 0
    for country in res_json['data']:
        if country['population'] > p:
            result += 1

    num_pages = res_json['total_pages']
    counter = 2
    while counter<=num_pages:
        res=requests.get(base_url + s+"&num="+str(counter))
        counter+=1
        res_json = json.loads(res.text)
        for country in res_json['data']:
            if country['population'] > p:
                result += 1
    return result


print(getCountries('in',1000000))