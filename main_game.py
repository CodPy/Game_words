# создание сообщения для отправки в SPLUNK
# передает индекс куда писать в SPLUNK, url-адрес сервиса к которому обращаемся, действие и окружение тестовое или пром
def create_splunk_message(index_to_save,url,action,message, env,company_name,time_rep,count_bso):
    dictjson = {
        "index": index_to_save,
        "sourcetype": "JSON",
        "event": {
            "url": url,
            "message": message,
            "Action": action,
            "Company":company_name,
            "Time_RSA":time_rep,
            "Count_free_bso":count_bso,
            "SystemUSE": "PYTHON_SCRIPT"
        }
    }
    return dictjson

def writejsontosplunk (jsontext,adr,port_,token_):
    url =adr
    port = port_
    securitytoken = token_
    os.environ['NO_PROXY'] = url
    # authHeader = {'Authorization': 'Splunk {}'.format(securitytoken)}

    authHeader = {'Authorization': 'Splunk {}'.format(securitytoken),'Content-type': 'application/json; profile=urn:splunk:event:1.0; charset=utf-8'}

    print (authHeader)
    jsonDict = jsontext
    try:
     print('''https://''' + url + ':' + port + '/services/collector/event''')
     r1 = requests.post('''http://''' + url + ':' + port + '/services/collector/event', headers=authHeader,json=jsonDict, verify=False)
     print ('''https://''' + url + ':' + port + '/services/collector/event''')
     d = eval(r1.text)
     r = (d["code"])
     print (r)
    except:
        # РєРѕРґ 777 СЃРѕРѕС‚РІРµС‚СЃС‚РІСѓРµС‚ РЅРµСѓСЃРїРµС€РЅРѕР№ Р·Р°РїРёСЃРё РІ РЎРїР»Р°РЅРє
        r=777
    return r
