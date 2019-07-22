import requests
import json
import datetime
import time
from random import randint
import config

def sendSMS(phone,account,amount,ReceiptNo,mpesaRef,names):
	msg = f"Dear {names}, Your payment of KES {amount} for {account} to MERU COUNTY GOVERNMENT has been received. Receipt No {ReceiptNo}."

	payload={'SenderName':'merupay','Mobile':phone,'Message':msg}
	headers = {'content-type': 'application/x-www-form-urlencoded', 'DeveloperKey':config.DeveloperKey, 'Password':config.password}	
	response = requests.post(config.url, data=payload, headers=headers)

	if (response.status_code ==200 ):
		x = datetime.datetime.now()
		print(phone + ':  Message Sent   :  ' + x.strftime("%d-%m-%Y %H:%M:%S"))
		cursor.execute("update MpesaTransactions set ResponseCode = 200,ResponseMessage='OK' where PayloadModel_TransID ='%s'" % mpesaRef)
		config.conn.commit() 
print('Application Running:  ' + datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

while True:
	cursor = config.conn.cursor(as_dict=True)
	cursor.execute("SELECT * FROM dbo.MpesaTransactions where PayloadModel_BusinessShortCode = '440112' and ResponseCode=0")
	result = cursor.fetchall()

	for res in result:
	    phone = res['PayloadModel_MSISDN']
	    account = res['PayloadModel_BillRefNumber']
	    amount = res['PayloadModel_TransAmount']
	    ReceiptNo = randint(100,2000002)
	    mpesaRef = res['PayloadModel_TransID']	    
	    names = res['PayloadModel_FirstName']
	    sendSMS(phone,account,amount,ReceiptNo,mpesaRef,names)
	time.sleep(3)
	
	# print('Waiting for messages...' )

config.conn.close()