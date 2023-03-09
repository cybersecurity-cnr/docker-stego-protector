import os
import time
import random

sizefrom = int(os.getenv('SIZEFROM'))
sizeto = int(os.getenv('SIZETO'))
timeout = int(os.getenv('TIMEOUT'))

while True:
	n = random.randint(sizefrom, sizeto)
	tmp = 'a' * n
	print(n)
	time.sleep(timeout)
	del tmp
