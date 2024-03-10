driving = input('請問你是否有開過車?')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('你不應該開過才對')
elif driving == '沒有':
	if age >= 18:
		print('你去考駕照啊!')
	else:
		print('長大去考啊!')
else:
	print('只能輸入 有/沒有')
