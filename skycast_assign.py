# Coder: T. K . Ramesh Babu ##

#### Class for initial input ####
class skycast:
	def __init__(self):
		pass
	def initialinput(self):
		self.boundary = map(int, raw_input().split()) # lower and upper bounds
		self.blockch = map(int, raw_input().split()) # block channels
		self.wishch = map(int, raw_input().split()) # wish channels
#### Class for findign the difference ####
class chsort(skycast):
	 def __init__(self):
		skycast.__init__(self)
	 def finddiff(self):
		self.blockchmodified=self.blockch[1::]
		self.wishchmodified=self.wishch[1::]
		self.wishchmodified.sort()
		self.diff_req=[]
		for i in range(0,len(self.wishchmodified)-1):
			self.diff_req.append(self.wishchmodified[i+1]-self.wishchmodified[i])
#### Class for finding the sum value ####
class minsum(chsort):
	def __init__(self):
		chsort.__init__(self)
	def calsum(self):
		self.sumval=(len(str(self.wishchmodified[0])))
		for i in range(0,len(self.diff_req)):
			if self.diff_req[i]<len(str(self.wishchmodified[i+1])):
				if self.diff_req[i]==0:
					self.sumval=self.sumval+1
				else:
					self.tmp=self.wishchmodified[i]
					for j in range(0,self.diff_req[i]):
						if self.tmp not in self.blockchmodified:
							self.sumval=self.sumval+self.diff_req[i]
							self.tmp=self.tmp+1
						else:
							self.sumval=self.sumval-1
			else:
				self.sumval=self.sumval+(len(str(self.wishchmodified[i+1])))
		return(self.sumval)
#### Class for condition checkings ####
class checker:
	def __init__(self):
		pass
	# boundary and high channel check
	def boundchecker(self,bound):
		if bound[0]<0:
			return false
		if bound[1]>10000 and bound[1]>bound[0]:
			return False
		return True
	# checking block channels lessthan or equal to 40
	def blockcheck(self,blocksiz):
		if blocksiz>40:
			return False
		return True
	# checking wish channels count 1>=x<=50
	def wcheck(self,wsiz):
		if wsiz<1 and wsiz>50:
			return False
		return True
	# finding the same neighbouring channels in wish lists count
	def ncheck(self,wishch):
		cnt=0
		for i in range(0,len(wishch)-1):
			if wishch[i]==wishch[i+1]:
				cnt=cnt+1
		return cnt
c=minsum()	
c.initialinput()
check=checker()
if check.boundchecker(c.boundary) and check.blockcheck(c.blockch[0]) and check.wcheck(c.wishch[0]):
	c.finddiff()
	print("Minimum number of clicks required is=")
	print(c.calsum()-check.ncheck(c.wishch))
else:
	print("Invalid Inputs")
