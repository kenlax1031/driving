country = input('請問你是哪國人: ')
age = input('輸入年齡: ')
age = int(age)
if country == '台灣' :
	if age >= 18:
		print('你可以考駕照')
	else:
		print('還沒買到雞腿')
elif country == '美國':
	if age >=16:
		print('你可以開車')
	else:
		print('還沒買到雞腿')
else:
	print('你只能輸入台灣或美國')