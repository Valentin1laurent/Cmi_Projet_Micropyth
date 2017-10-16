    import requests
    import json
    #Http requests
    url="http://api.openweathermap.org/data/2.5/forecast?id=2998323&appid=<key>"
    r=requests.get(url)
    data=r.json()
    #Temperature et Descritpion
    temp0=int(data['list'][0]['main']['temp']-273)
    desc0=data['list'][0]['weather'][0]['description']
    temp1=int(data['list'][1]['main']['temp']-273)
    desc1=data['list'][1]['weather'][0]['description']
