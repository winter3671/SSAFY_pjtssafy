from pprint import pprint
import requests

def get_seoul_weather():
    # API KEY
    API_KEY = '864c38ae22febca57bbff765c89a7ebd'

    # 서울의 위도와 경도
    lat = 37.56
    lon = 126.97
    city_name = 'seoul'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&lat={lat}&lon={lon}&appid={API_KEY}'

    response = requests.get(url).json()

    temperature = response['main']['temp']
    print(f"캘빈 온도: {temperature}")

# API 요청 보내기
    return response

# 캘빈 온도 출력
                                  

result = get_seoul_weather()
pprint(result)
