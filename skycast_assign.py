
#### Class for initial input ####
import sys
class skycast:
	def __init__(self):
		pass
	def initialinput(self,argv):
		self.boundary = map(int, argv[0].split()) # lower and upper bounds
		self.blockch = map(int, argv[1].split()) # block channels
		self.wishch = map(int, argv[2].split()) # wish channels
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
if __name__ == '__main__':
	gauravclicks=minsum()	
	gauravclicks.initialinput(sys.argv[1:]) #Inputs are take through command line.
	check=checker()
	if check.boundchecker(gauravclicks.boundary) and check.blockcheck(gauravclicks.blockch[0]) and check.wcheck(gauravclicks.wishch[0]):
		gauravclicks.finddiff()
		print("Minimum number of clicks required is=")
		print(gauravclicks.calsum()-check.ncheck(gauravclicks.wishch))
	else:
		print("Invalid Inputs")
