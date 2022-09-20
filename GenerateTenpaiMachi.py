import itertools
import datetime
import sys
import pandas as pd
from AgariChecker import AgariChecker

TenpaiMachiPath = 'TenpaiMachi.csv'
kTenpai = 'Tenpai'
kMachi = 'Machi'

def tenpaiStr(tenpai)->str:
	ret = ''
	for i in range(1,10):
		if tenpai[i] >= 1:
			ret += str(i) * tenpai[i]
	return ret

def machiStr(machi)->str:
	ret = ''
	for i in machi:
		ret += str(i)
	return ret

if __name__ == '__main__':	
	##tenpaiList = []
	##tenpaiList.append((0,3,1,1,1,1,1,1,1,3))
	##tenpaiList.append((0,0,0,2,4,2,2,1,2,0))
	##a = AgariChecker()
	##tenpaiMachi = []
	##for tenpai in tenpaiList:
	##	machi = a.calcMachi(list(tenpai))
	##	tenpaiMachi.append([tenpaiStr(tenpai), machiStr(machi)])
	##df = pd.DataFrame(tenpaiMachi, columns = [kTenpai,kMachi])
	##print(df)
	##df.to_csv(TenpaiMachiPath)
	
	##loaddf = pd.read_csv(TenpaiMachiPath)
	##print(loaddf.head())
	##print(loaddf.dtypes)
	
	##query
	##x = loaddf.query('Machi == 378')
	##print(x)
	##tenpai = x[kTenpai].values
	##print(tenpai)
	##print(type(tenpai[0]))
	
	##sys.exit(0)
	
	startTime = datetime.datetime.now()
	
	allHai = []
	for i in range(1,10):
		allHai.extend([i] * 4)
	##print(allHai)
	combi = itertools.combinations(allHai, 14)
	combiSet = set(combi)
	print(f'len(combi14) = {len(combiSet)}')
	agariSet = set()
	a = AgariChecker()
	for i in combiSet:
		tehai = (0,i.count(1),i.count(2),i.count(3),i.count(4),i.count(5),i.count(6),i.count(7),i.count(8),i.count(9))
		a.tehai = list(tehai)
		b = a.isAgari()
		if b:
			agariSet.add(tehai)
		
	print(f'len(agari14) = {len(agariSet)}')
	
	tenpaiSet = set()
	for agari in agariSet:
		for i in range(1,10):
			if agari[i] >= 1:
				tenpai = list(agari)
				tenpai[i] -= 1
				tenpaiSet.add(tuple(tenpai))
	
	print(f'len(tenpai13) = {len(tenpaiSet)}')
	
	tenpaiMachi = []
	for tenpai in tenpaiSet:
		machi = a.calcMachi(list(tenpai))
		tenpaiMachi.append([tenpaiStr(tenpai), machiStr(machi)])
	df = pd.DataFrame(tenpaiMachi, columns = [kTenpai,kMachi])
	df.to_csv(TenpaiMachiPath)
	
	endTime = datetime.datetime.now()
	print('elasped time = {}'.format(endTime - startTime))