#import pymysql
import requests
import json
token = '473906297:AAElyClsMSIIhZ6AWAabsgx5xCTvt4S3ezo'
chat_id = {  'kirill':'343398748',
				'vitya':'385985954'}
text = 'я научился получать ответ в виде словаря, это оказалось очень легко'
def sendMessage(chat_id, text):
	global token
	request = 'https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+chat_id+'&text='+text
	return json.loads(requests.get(request).text)
print(sendMessage(chat_id['vitya'], text))
