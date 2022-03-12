from random import *
money = 10000
print("코인 게임에 오신 것을 환영합니다.")
print("이곳에는 배코인, 사과코인, 호박코인이 있고,", "변동성은 배코인 : -20% ~ 20%, 사과코인 : -5% ~ 5%, 호박코인 : -40% ~ 40% 입니다. 돈은 10000골드가 있습니다." )
pear_coin = {"cost" : 500, "count" : 0}
pumpkin_coin = {"cost":500, "count":0}
apple_coin = {"cost":500, "count":0}
while True:
	print("현재 자본" , money)
	print("배코인 가격 :", pear_coin['cost'], "수량:", pear_coin['count'], ", 사과코인 가격 :", apple_coin['cost'], "수량 :", apple_coin['count'],", 호박코인 가격 :", pumpkin_coin['cost'], "수량:", pumpkin_coin['count'])
	print("사려면 b, 팔려면 s, 아무 것도 안하시려면 w, 그만 두려면 아무글자나 입력하세요.")
	action = input()
	if action == 'b':
		print("어떤 코인을 사시겠습니까? 배코인을 사시려면 1을, 사과코인을 사시려면 2를 호박코인을 사시려면 3을 입력하세요.")
		b_whatcoin = input()
		if b_whatcoin == '1':
			print("몇개를 사시겠습니까?")
			b_1_count = int(input())
			if b_1_count >= 0:
				pear_coin['count'] += b_1_count
				money -= pear_coin['count'] * pear_coin['cost']
				if money < 0:
					print("잘못된 수량 입니다.")
					money += b_1_count * pear_coin['cost']
					pear_coin["count"] -= b_1_count
					continue
		elif b_whatcoin == '2':
			print("몇개를 사시겠습니까?")
			b_2_count = int(input())
			if b_2_count >= 0:
				apple_coin['count'] += b_2_count
				money -= apple_coin['count'] * apple_coin['cost']
				if money < 0:
					print("잘못된 수량 입니다.")
					money += b_2_count * apple_coin['cost']
					apple_coin["count"] -= b_2_count
					continue
		elif b_whatcoin == '3':
			print("몇개를 사시겠습니까?")
			b_3_count = int(input())
			if b_3_count >= 0:
				pumpkin_coin['count'] += b_3_count
				money -= pumpkin_coin['count'] * pumpkin_coin['cost']
				if money < 0:
					print("잘못된 수량 입니다.")
					money += b_3_count * pumpkin_coin['cost']
					pumpkin_coin["count"] -= b_3_count
					continue
	elif action == 's':
		print("어떤 코인을 파시겠습니까? 배코인을 파시려면 1을, 사과코인을 파시려면 2를 호박코인을 파시려면 3을 입력하세요.")
		s_whatcoin = input()
		if s_whatcoin == '1':
			print("몇개를 파시겠습니까?")
			s_1_count = int(input())
			if s_1_count >= 0:
				money += s_1_count * pear_coin['cost']
				pear_coin['count'] -= s_1_count
			if pear_coin['count'] < 0:
				print("잘못된 수량입니다.")
				money -= s_1_count * pear_coin['cost']
				pear_coin["count"] += s_1_count
				continue
		elif s_whatcoin == '2':
			print("몇개를 파시겠습니까?")
			s_2_count = int(input())
			if s_2_count >= 0:
				money += s_2_count * apple_coin['cost']
				apple_coin['count'] -= s_2_count
			if apple_coin['count'] < 0:
				print("잘못된 수량입니다.")
				money -= s_2_count * apple_coin['cost']
				apple_coin["count"] += s_2_count
				continue
		elif s_whatcoin == '3':
			print("몇개를 파시겠습니까?")
			s_3_count = int(input())
			if s_3_count >= 0:
				money += s_3_count * pumpkin_coin['cost']
				pumpkin_coin['count'] -= s_3_count
			if pumpkin_coin['count'] < 0:
				print("잘못된 수량입니다.")
				money -= s_3_count * pumpkin_coin['cost']
				pumpkin_coin["count"] += s_3_count
				continue
	elif action == 'w':
		pass
	else:
		print("안녕히가십시오.")
		exit()
	def vari(vari_coin):
		if vari_coin == 1:
			luck = randint(0,1)
			ratofch = randrange(0, 41) / 100
			if luck == 0:
				pumpkin_coin['cost'] += int(pumpkin_coin['cost'] * ratofch)
			else:
				pumpkin_coin['cost'] -= int(pumpkin_coin['cost'] * ratofch)
		elif vari_coin == 2:    
			luck = randint(0,1)
			ratofch = randrange(0, 21) / 100
			if luck == 0:
				pear_coin['cost'] += int(pear_coin['cost'] * ratofch)
			else:
				pear_coin['cost'] -= int(pear_coin['cost'] * ratofch)
		elif vari_coin == 3:
			luck = randint(0,1) 
			ratofch = randrange(0, 6) / 100
			if luck == 0:
				apple_coin['cost'] += int(apple_coin['cost'] * ratofch)
			else:
				apple_coin['cost'] -= int(apple_coin['cost'] * ratofch)
	vari(1)
	vari(2)
	vari(3)
