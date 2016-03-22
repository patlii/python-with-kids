#!/usr/bin/env python3

total = 7
s = 0
position = 0;

for i in range(2, total + 1):
	s = (s + 5) % i

position = s + 1

print(position)
