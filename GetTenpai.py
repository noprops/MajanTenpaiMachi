import pandas as pd
import GenerateTenpaiMachi
import sys

TenpaiMachiPath = 'TenpaiMachi.csv'
kTenpai = 'Tenpai'
kMachi = 'Machi'

if __name__ == '__main__':
	args = sys.argv
	if len(args) != 2:
		print('usage : python3 GetTenpai.py 123456789')
		exit(0)
	machi = list(args[1])
	li = []
	for s in machi:
		if s.isdecimal():
			li.append(int(s))
	li = list(set(li))
	li.sort()
	machiStr = GenerateTenpaiMachi.machiStr(li)
	print(f'Machi\n{machiStr}')
	df = pd.read_csv(TenpaiMachiPath)
	##print(df)
	##x = df.query('Machi == @machiStr')
	x = df.query(f'Machi == {machiStr}')
	tenpai = x[kTenpai].values
	print('Tenpai')
	for i in tenpai:
		print(i)