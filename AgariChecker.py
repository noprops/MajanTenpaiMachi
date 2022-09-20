class AgariChecker():
	def __init__(self):
		self.agari = False
		self.tehai = []
		## self.tehai = [0,3,1,1,1,2,1,1,1,3]
	
	def isAgari(self)->bool:
		self.agari = False
		
		for i in range(1,10):
			if self.tehai[i] >= 2:
				## jantou
				self.tehai[i] -= 2
				##print(f'jantou is {i}')
				b = self.mentuCut(1)
				self.tehai[i] += 2
				if b:
					return b
		self.mentuCut(1)
		return self.agari
	
	def mentuCut(self, i_:int)->bool:
		i = i_
		while i <= 9 and self.tehai[i] == 0:
			i += 1
		if i > 9:
			for j in range(1,10):
				if self.tehai[j] > 0:
					##print(f'mentuCut : {self.tehai} False')
					return False
			self.agari = True
			##print(f'mentuCut : {self.tehai} True')
			return True
		if self.tehai[i] >= 3:
			## kotu
			self.tehai[i] -= 3
			b = self.mentuCut(i)
			self.tehai[i] += 3
			if b:
				return b
		if i+2 <= 9 and self.tehai[i] >= 1 and self.tehai[i+1] >= 1 and self.tehai[i+2] >= 1:
			## shuntu
			self.tehai[i] -= 1
			self.tehai[i+1] -= 1
			self.tehai[i+2] -= 1
			b = self.mentuCut(i)
			self.tehai[i] += 1
			self.tehai[i+1] += 1
			self.tehai[i+2] += 1
			if b:
				return b
		return self.mentuCut(i+1)
	
	def calcMachi(self, tehai:list)->tuple:
		ret = []
		for i in range(1,10):
			if tehai[i] >= 4:
				continue
			self.tehai = list(tehai)
			self.tehai[i] += 1
			if self.isAgari():
				ret.append(i)
		return tuple(ret)