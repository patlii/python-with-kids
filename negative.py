#!/usr/bin/env python3

for person in range(1,10):
	if (3 * person + 8) == (5 * person + 2):
		print('person: %d' % person)
		print('apple: %d' % (3 * person + 8))

print('-----')

for person in range(1,10):
	if (3 * person + 8) == (5 * person - 2):
		print('person: %d' % person)
		print('apple: %d' % (3 * person + 8))
