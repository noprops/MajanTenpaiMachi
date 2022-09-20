class ShantenCalc():
	def __init__(self, tehai_):
		self.mentu = 0
		self.maxMentu = 0
		self.pair = 0
		self.tatu = 0
		self.shanten = 99
		self.tehai = tehai_
		## self.tehai = [0,4,1,1,1,1,1,1,1,4]
	
	def run(self)->int:
		self.mentu = 0
		self.maxMentu = 0
		self.pair = 0
		self.tatu = 0
		self.shanten = 99
		
		haiCount = 0
		for i in range(1,10):
			haiCount += self.tehai[i]
		self.maxMentu = haiCount // 3
		
		for i in range(1,10):
			if tehai[i] >= 2:
				self.pair += 1
				self.tehai[i] -= 2
				self.mentuCut(0)
				self.tehai[i] += 2
				self.pair -= 1
		
		mentuCut(1)
		return self.shanten
	
	def mentuCut(self, i_:int):
		i = i_
		while i == 0:
			i += 1
		if i >= 9:
			self.tatuCut(1)
			return
		if self.tehai[i] >= 3:
			## kotu
			self.mentu += 1
			self.tehai[i] -= 3
			mentuCut(i)
			self.tehai[i] += 3
			self.mentu -= 1
		if i+2<=9 && self.tehai[i] >= 1 && self.tehai[i+1] >= 1 && self.tehai[i+2] >= 1:
			## shuntu
			self.mentu += 1
			self.tehai[i] -= 1
			self.tehai[i+1] -= 1
			self.tehai[i+2] -= 1
			mentuCut(i)
			self.tehai[i] += 1
			self.tehai[i+1] += 1
			self.tehai[i+2] += 1
			self.mentu -= 1
		mentuCut(i+1)
	
	def tatuCut(self, i_:int):
		i = i_
		while i == 0:
			i += 1
		if i >= 9:
			shanten = 8 - 