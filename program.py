import os
import time
import random

sizefrom = int(os.getenv('SIZEFROM'))
sizeto = int(os.getenv('SIZETO'))
timeoutfrom = float(os.getenv('TIMEOUTFROM'))
timeoutto = float(os.getenv('TIMEOUTTO'))

while True:
	n = random.randint(sizefrom, sizeto)
	tmp = 'a' * n
	if timeoutfrom.is_integer() and timeoutto.is_integer():
		timeout = random.randint(timeoutfrom, timeoutto)
	else:
		timeout = random.uniform(timeoutfrom, timeoutto)
	print(n)
	time.sleep(timeout)
	del tmp
