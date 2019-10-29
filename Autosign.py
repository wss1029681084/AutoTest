#---------------------------叮咚买菜
url2="http://ddxq.mobi/api/v2/user/sign/"

cookie=dict( DDXQSESSID='a026968bcc3c9e51e1978c35b17c6c14')
cookie2=requests.utils.cookiejar_from_dict(cookie)
Ast2="sign_series"
res2=requests.post(url2,cookies=cookie2)
res2=requests.post(url2,cookies=cookie2).content.decode('utf-8')
if( Ast2 in str(res2)):
    logging.info(res2)
else:
    logging.error(res2)
#--------------------饿了么
#每日签到
url2="https://h5.ele.me/restapi/marketing/v1/wechat_signin/users/321606090"

cookie={'SID': 'mKWw1DXUdMiQlUs7hOwDhLDsJlkpQ0OCAybw', ' USERID': '321606090', ' isg': 'BLOzYuZ37LPFqaBnZl-ui7pbSLPd6EeqEK2552VQC1IJZNcG-rnc-y9_GlIvX5-i', ' track_id': '1542009860|9308d7b20438040825282d939f7beb334c407d1e1ae068ad58|caf69cba2bf958fe64392f614c53ec7d', ' _utrace': 'f2cf00483c9340d8d691d626be6b35cb_2018-11-12', ' cna': '3yFwFJRdDy4CAXxKS87k7Y4x', ' ubt_ssid': 'fbfi1uucahi2cgqnb505iicptvjmbusg_2018-11-12', ' perf_ssid': '32n7xavqjclo57flepe54e67cxzus0ej_2018-11-12'}
cookie2=requests.utils.cookiejar_from_dict(cookie)
#Ast2="sign_series"
res2=requests.post(url2,cookies=cookie2)
res2=requests.post(url2,cookies=cookie2).content.decode('utf-8')
logging.info("饿了么每日签到----------"+res2)
#翻牌
url2="https://h5.ele.me/restapi/traffic/campagin/basketball/lotteryDraw"
url="https://h5.ele.me/restapi/traffic/campagin/basketball/queryQualification?sceneType=1"
data={"sceneType":1,"prizeLocation":1}
res=requests.post(url)
res2=requests.post(url2,data,cookies=cookie2).content.decode('utf-8')
logging.info("饿了么每日翻牌----------"+res2)
#会员签到
url2="https://h5.ele.me/restapi/member/v1/users/321606090/sign_in"
data={"user_id":321606090,"latitude":31.250991821289062,"longitude":121.51677703857422,"source":"main"}
res2=requests.post(url2,data,cookies=cookie2).content.decode('utf-8')
logging.info("饿了么会员签到----------"+res2)
#签到翻牌
url2="https://h5.ele.me/restapi/member/v1/users/321606090/sign_in/daily/prize"
data={"user_id":321606090,"latitude":31.250991821289062,"longitude":121.51677703857422}
res2=requests.post(url2,data,cookies=cookie2).content.decode('utf-8')
logging.info("饿了么会员翻牌----------"+res2)
#水果页面签到
url2="https://newretail.ele.me/gdintegral/integral/setsignininfo?device_id=3B0EE632-2E54-45F8-953F-6FB9AB9F8889&user_id=321606090&lng=121.51692962646484&lat=31.250530242919922&shardlocation=121.51692962646484,31.250530242919922&city_id=1"

res2=requests.post(url2,data,cookies=cookie2).content.decode('utf-8')
logging.info("饿了么水果超市签到----------"+res2)

#东财签到

url2="https://emuserh5.eastmoney.com/IntegralSystem/Signing?UserId=1959065161664864&Version=7.7&pi=19590651616648640027059724a55734f6b3831315876343151556338356c496165686e44394e6735325477674163354450342f556554436e766f77776d736e71674f434e477471774945353666507478495253674841455137515268492f3765305358314b654f4e44705a583334437a777257773d&ProductType=cft&ct=PxKGWgHDHOnaITgyNoVXwDrPa1Tdjqe-WDgGWvXJE84eHFuQhyFHULAXpBTCwLSj-RiljprQsx1RuVfvVPzeHYcQT96b8zkfvhtK2aj7mj7mOxt3_GqrgiVTLsaPpsW3iaXKYbcTbaMSTxmsFzzDqoVhle18WhUqmsQ6Zipz-Yk&Sys=12.1&ut=FobyicMgeV6_oa5YYcxre0J91p4f7WY-Rz5NWrVWOjQaqNzcflTYNzTYbW10fUua2dhM8Alegd5XiagQcxLjGTJgWW2hqrtL4zhpTlmCnnONr3DdM0eb68YAJRR_eD47k8K76zr5ZFG2hnQsiKwI0gPMf8x0Lw5vLvlhFHhzukpQtSZPy9GjC4nHMqih9KWToKrXa6N7zIhJmLRJi8Ul_Lcb6naBPAO9rRsPOg0rIBC0GaB7A__Y28jvMSJnoXot6xciQtnHKqEn48RKMnFpGfAjDRDcZbqg63AU67bpQZSLhL_5VULG2g&DeviceType=iOS%2012.1&UniqueID=B73384D1C937-D5BF-4672-B484-2463CDEDF1B1610C&DeviceModel=iPhone7%2C1"
res2=requests.post(url2).content.decode('utf-8')
logging.info("东方财富签到----------"+res2)

#巴乐兔租房app签到
headers={'Content-Type':'application/x-www-form-urlencoded'}
cookie="_ga=GA1.2.48101134.1556521203; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22169cc7ef5e865c-0a89c9d366a21b-450c1c31-304704-169cc7ef5e9d7%22%2C%22%24device_id%22%3A%22169cc7ef5e865c-0a89c9d366a21b-450c1c31-304704-169cc7ef5e9d7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; acw_tc=2f624a6915585805288001428e582a87f06108bd4918ed06afb8d38ffeff1c; PHPSESSID=59279e5cd9f3fe00e692cea3b36df0cc"
url="https://api.baletu.com/App401/UserPoints/checkInCoupon"
n=1
while n<4:
    data = "city_id=1&contract_id=463151&device_id=9051F906-EB90-4D08-8E50-AB1B99E0EE44&from=2&preset_parameters=%7B%0A%20%20%22%24os_version%22%20%3A%20%2212.2%22%2C%0A%20%20%22%24device_id%22%20%3A%20%2271CA293E-5FF6-4267-9954-D44BC8E3984E%22%2C%0A%20%20%22distinct_id%22%20%3A%20%221001370011%22%2C%0A%20%20%22%24os%22%20%3A%20%22iOS%22%2C%0A%20%20%22%24carrier%22%20%3A%20%22%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A%22%2C%0A%20%20%22%24screen_height%22%20%3A%20736%2C%0A%20%20%22%24is_first_day%22%20%3A%20false%2C%0A%20%20%22%24screen_width%22%20%3A%20414%2C%0A%20%20%22%24model%22%20%3A%20%22iPhone7%2C1%22%2C%0A%20%20%22%24wifi%22%20%3A%20true%2C%0A%20%20%22%24network_type%22%20%3A%20%22WIFI%22%2C%0A%20%20%22%24app_version%22%20%3A%20%224.8.6%22%2C%0A%20%20%22%24manufacturer%22%20%3A%20%22Apple%22%2C%0A%20%20%22%24lib%22%20%3A%20%22iOS%22%2C%0A%20%20%22gps_city%22%20%3A%20%22%E4%B8%8A%E6%B5%B7%E5%B8%82%22%2C%0A%20%20%22%24lib_version%22%20%3A%20%221.10.24%22%0A%7D&public_parameters=%7B%0A%20%20%22uuid%22%20%3A%20%2293394619a3c21e032e18742cb04bcc40%22%2C%0A%20%20%22cookies_id%22%20%3A%20%220%22%2C%0A%20%20%22project_role%22%20%3A%20%22%E7%A7%9F%E5%AE%A2%22%2C%0A%20%20%22channel%22%20%3A%20%22AppStore%22%2C%0A%20%20%22is_login%22%20%3A%20true%2C%0A%20%20%22is_has_contract%22%20%3A%20true%2C%0A%20%20%22openid%22%20%3A%20%220%22%2C%0A%20%20%22gps_city%22%20%3A%20%22%E4%B8%8A%E6%B5%B7%E5%B8%82%22%2C%0A%20%20%22new_project_name%22%20%3A%20%221%22%2C%0A%20%20%22platformType%22%20%3A%20%22iOS%22%2C%0A%20%20%22city_code%22%20%3A%20%22310100%22%2C%0A%20%20%22device_id%22%20%3A%20%229051F906-EB90-4D08-8E50-AB1B99E0EE44%22%2C%0A%20%20%22blt_user_id%22%20%3A%20%221001370011%22%0A%7D&type=" + str(
        n) + "&udid=93394619a3c21e032e18742cb04bcc40&user_id=1001370011&ut=2637bab35f7dcc8f48d87655c715a722a4b9223a&v=4.8.6"

    res2=requests.post(url,data.encode('utf-8'),cookie,headers=headers).content.decode('utf-8')
    logging.info("巴乐兔租房app签到------------------"+res2)
    n+=1
data1="city_id=1&contract_id=463151&coupon_id=125&device_id=9051F906-EB90-4D08-8E50-AB1B99E0EE44&from=2&preset_parameters=%7B%0A%20%20%22%24os_version%22%20%3A%20%2212.4%22%2C%0A%20%20%22%24device_id%22%20%3A%20%2271CA293E-5FF6-4267-9954-D44BC8E3984E%22%2C%0A%20%20%22distinct_id%22%20%3A%20%221001370011%22%2C%0A%20%20%22%24os%22%20%3A%20%22iOS%22%2C%0A%20%20%22%24carrier%22%20%3A%20%22%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A%22%2C%0A%20%20%22%24screen_height%22%20%3A%20736%2C%0A%20%20%22%24is_first_day%22%20%3A%20false%2C%0A%20%20%22%24screen_width%22%20%3A%20414%2C%0A%20%20%22%24model%22%20%3A%20%22iPhone7%2C1%22%2C%0A%20%20%22%24wifi%22%20%3A%20true%2C%0A%20%20%22%24network_type%22%20%3A%20%22WIFI%22%2C%0A%20%20%22%24app_version%22%20%3A%20%224.9.7%22%2C%0A%20%20%22%24manufacturer%22%20%3A%20%22Apple%22%2C%0A%20%20%22%24lib%22%20%3A%20%22iOS%22%2C%0A%20%20%22gps_city%22%20%3A%20%22%E4%B8%8A%E6%B5%B7%E5%B8%82%22%2C%0A%20%20%22%24lib_version%22%20%3A%20%221.10.24%22%0A%7D&public_parameters=%7B%0A%20%20%22uuid%22%20%3A%20%2293394619a3c21e032e18742cb04bcc40%22%2C%0A%20%20%22cookies_id%22%20%3A%20%220%22%2C%0A%20%20%22project_role%22%20%3A%20%22%E7%A7%9F%E5%AE%A2%22%2C%0A%20%20%22channel%22%20%3A%20%22AppStore%22%2C%0A%20%20%22is_login%22%20%3A%20true%2C%0A%20%20%22is_has_contract%22%20%3A%20true%2C%0A%20%20%22openid%22%20%3A%20%220%22%2C%0A%20%20%22gps_city%22%20%3A%20%22%E4%B8%8A%E6%B5%B7%E5%B8%82%22%2C%0A%20%20%22new_project_name%22%20%3A%20%221%22%2C%0A%20%20%22platformType%22%20%3A%20%22iOS%22%2C%0A%20%20%22city_code%22%20%3A%20%22310100%22%2C%0A%20%20%22device_id%22%20%3A%20%229051F906-EB90-4D08-8E50-AB1B99E0EE44%22%2C%0A%20%20%22blt_user_id%22%20%3A%20%221001370011%22%0A%7D&udid=93394619a3c21e032e18742cb04bcc40&user_id=1001370011&ut=2637bab35f7dcc8f48d87655c715a722a4b9223a&v=4.9.7"
url1="https://api.baletu.com/App401/UserPoints/CouponAward"
res=requests.post(url1,data1.encode('utf-8'),cookie,headers=headers).content.decode('utf-8')
logging.info("巴乐兔租房app签到兑奖------------------"+res)


https://m.lhjing.com/act/lucky_draw?clientId=1&apiVer=1.0.0&appVer=1.3.1&channel=
   cookie=sid=IjDTq5bCOytP6sFm1PV06SS0d2f75eDqJsJYq0FkRTQ=; acw_tc=3a14c53115709713522854734ee8bc5c3b96764eea707bcc9db755b9c2

