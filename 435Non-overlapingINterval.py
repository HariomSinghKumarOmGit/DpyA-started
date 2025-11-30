prev = 0
count = 1
for i in range(0,n):
    if intarvals[i][0]>=intarvals[prev][1]:
        count+=1
        prev = i

return n-count