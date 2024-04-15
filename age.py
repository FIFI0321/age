driving = input ('請問你有開過車嗎?')
if driving !='有' and driving !='沒有' :
	print ('只能輸入有/沒有')
	raise SystemExit

age = input ('請問你幾歲?')
age = int (age)
if driving == '有' :
	if age >= 18 :
		print ('你通過駕車測試了')
	else :
		print ('小提醒 未滿18歲不能開車喔!!')
if driving =='沒有' :
	if age >=18 :
		print ('你已經符合考駕照資格囉!可以去報名了')
	else :
		print ('等你滿18歲就可以考駕照囉!!')