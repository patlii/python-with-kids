#!/usr/bin/env python3
import random


right = 0
wrong = 0
max = 9

while True:
	a = random.randint(1, max)
	b = 7 #random.randint(1, max)

	a_real = a % 5
	a_image = 5 - a_real

	if b > 5:
		tail = b - 5
	else:
		tail = 5 - b

	try:

		while True:
			print('%d + %d = ' % (a, b), end = '')
			answer = input('').strip()

			try:
				n_answer = int(answer)
			except Exception as e:
				continue

			if n_answer == a + b:
				print('v ', end = '')
				right = right + 1
			else:
				print('x ', end = '')
				wrong = wrong + 1

			if a_image >= b:
				print('加看虚指，够加直加，', end = '')
			elif b == 5:
				print('加5反手，', end = '')
			elif b <= 5 and a_real >= tail:
				print('直加不够，减内凑(%d)反手，' % tail, end = '')
			elif b >= 5 and a_image >= tail:
				print('直加不够，加外凑(%d)反手，' % tail, end = '')
			elif b >= 5 and a_image < tail:
				print('减补进1')
				break

			if a + b > 10:
				print('拇指由伸变曲进1')
			elif a + b == 10:
				print('十指全伸进1')
			else:
				print()

			break
		print()
	except Exception as e:
		print('\n正确：%d，错误：%d' % (right, wrong))
		break
