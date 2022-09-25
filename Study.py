# page 113

print("Q1")
score = {"국어" : 80, "영어" : 75, "수학" : 55}
total = sum(score.values())

print(total / len(score.values()))



print("\nQ2")
num = 13
if(num % 2 == 0):
	print("짝수")
else:
	print("홀수")



print("\nQ3")
pin = "881120-1068234"

yyyymmdd = pin[:pin.find("-")]
num = pin[pin.find("-") + 1:]

print(yyyymmdd)
print(num)



print("\nQ4")
if(int(pin[pin.find("-") + 1]) % 2 == 0):
	print("여자")
else:
	print("남자")



print("\nQ5")
