#!/usr/bin/env python3
import random


right = 0
wrong = 0
max = 10

while True:
	a = random.randint(1, max)
	b = random.randint(1, max)


	try:

		while True:
			print('%d + %d = ' % (a, b), end = '')
			answer = input('').strip()

			try:
				n_answer = int(answer)
			except Exception as e:
				continue

			if n_answer == a + b:
				print('√')
				right = right + 1
			else:
				print('×')
				wrong = wrong + 1
			break
	except Exception as e:
		print('\n正确：%d，错误：%d' % (right, wrong))
		break
