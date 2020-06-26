height = input ('請輸入身高:')
weight = input ('請輸入體重:')
height = int(height) / 100
BMI = weight / height / height     

if BMI < 18.5:
	print ('體重過輕')
elif BMI >= 18.5 and BMI < 24:
	print ('正常範圍')
else:
	print ('體重過重')

print ('你的BMI值為', BMI)
