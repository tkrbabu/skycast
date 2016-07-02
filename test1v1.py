a = map(int, raw_input().split()) # lower and upper bounds
b = map(int, raw_input().split()) # block channels
c = map(int, raw_input().split()) # required channels
blck=b[1::]
req=c[1::]
blck.sort()
req.sort()
diff_blck=[]
diff_req=[]
for i in range(0,len(req)-1):
	diff_req.append(req[i+1]-req[i])
print(req)
print(diff_req)
sumval=(len(str(req[0])))
for i in range(0,len(diff_req)):
	if diff_req[i]<len(str(req[i+1])):
		if diff_req[i]==0:
			sumval=sumval+1
		else:
			sumval=sumval+diff_req[i]
	else:
		sumval=sumval+(len(str(req[i+1])))
print(sumval)
