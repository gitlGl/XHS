import requests,urllib3,time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from urllib3.util.retry import Retry

url = "https://example.com"#这个网站真实存在，emmm
session = requests.Session()
retry = Retry(total=3, backoff_factor=0.1, 
              status_forcelist=[ 500, 502, 503, 504 ])

adapter = HTTPAdapter(max_retries=retry)
session.mount('https://', adapter)
session.mount('http://', adapter)
#total=3，重试3次
#backoff_factor=0.1,间隔时间，会随着重试次数指数递增
#status_forcelist=[ 500, 502, 503, 504 ]这些状态码强制重试
response = session.get(url)

if response.status_code == 200:
    print("请求成功",response.text)
else:
    print("请求失败")
    
    
#利用try与while进行粗暴重试

while True:
    try:
        requests.get(url)
        break
    except Exception as e:
        print(e)
        time.sleep(2)#两秒重试一次
        