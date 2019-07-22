
import pymssql
conn = pymssql.connect(
	    host=r'JAMBOPAYAPPS\SQL2014',
	    user=r'WEBTRIBE1\smunyaga',
	    password='Muny@gz000',
	    database='LAIFOMS'
	)
password = '1d95a4c6d681ede5b18c89b21ceb46bfea7b8e4d8f824107615a2ee297493710'
DeveloperKey = '084049D0-AB72-4EE2-9EDE-0C25C1D1268C'
url = 'http://192.168.11.225/SMSService/API/SMS'

	# conn = pymssql.connect(
	#     host=r'.\SQL2012',
	#     user=r'broker',
	#     password='123grt2#',
	#     database='Mpesa_IPN'
	# )