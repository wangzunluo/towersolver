
print('hi')


a = [[3,2,5,1,3],[2,2,1,2,3]]
b = [[3,2,2,1,3],[2,2,1,3,3]]


sightleft = [0] * 5
sightright = [0] * 5
sighttop = [0] * 5
sightbottom = [0] * 5

rowcontents = []
columncontents = []
for i in range(5):
	rowcontents.append({})
	columncontents.append({})

c = [0] * 5
for i in range(5):
	c[i] = [0] * 5
	
print(a)
print(b)
print(c)

# #left
# for i in range(5):
	# #left
	# if a[0][i] == 1:
		# c[i][0] = 5
		# sightleft[i] = 1
		# sightright[i] = 1
		# rowcontents[i][5] = 0
		# columncontents[0][5] = 0

	# #right
	# if a[1][i] == 1:
		# c[i][4] = 5
		# sightleft[i] = 1
		# sightright[i] = 1
		# rowcontents[i][5] = 0
		# columncontents[4][5] = 0

	# #top
	# if b[0][i] == 1:
		# c[0][i] = 5
		# sighttop[i] = 1
		# sightbottom[i] = 1
		# rowcontents[0][5] = 0
		# columncontents[i][5] = 0

	# #bottom
	# if b[1][i] == 1:
		# c[4][i] = 5
		# sighttop[i] = 1
		# sightbottom[i] = 1
		# rowcontents[4][5] = 0
		# columncontents[i][5] = 0
		
def checkValid(row, col):
	if row == 4:
		if col == 0:
			exit()
	seenleft = 1
	seenright = 1
	seentop = 1
	seenbottom = 1
	highLR = c[row][0]
	highTB = c[0][col]
	for i in range(1, 5):
		if c[row][i] > highLR:
			highLR = c[row][i]
			seenleft += 1
			
		if c[i][col] > highTB:
			highTB = c[i][col]
			seentop += 1
	
	if seenleft > a[0][row]:
		return False
		
	if seentop > b[0][col]:
		return False
		
	highest = c[row][4]
	highset = c[4][col]
	for i in range(4, -1, -1):
		if c[row][i] > highLR:
			highLR = c[row][i]
			seenright += 1
			print("SEEN")
			print(seenright)
		
		if c[i][col] > highTB:
			highTB = c[i][col]
			seenbottom += 1

	if seenright > a[1][row]:
		return False
		
	if seenbottom > b[1][col]:
		return False
	
	return True
		

i=0
j=0
check = 1
#test a number in the cell
#if no violations, continue
#if yes violation, go back to previous cell
#violations include sight and usage of numbers in row/col

while i<5:
	
	while j<5:
		if c[i][j] != 0:
			check = c[i][j] + 1
		while check < 6:
			print(i)
			print(j)
			print(check)
			print(rowcontents)
			print(columncontents)
			if check in rowcontents[i]:
				check += 1
				continue
			if check in columncontents[j]:
				check += 1
				continue
			
			c[i][j] = check
			if checkValid(i, j):
				rowcontents[i][check] = 0
				columncontents[j][check] = 0
				check = 1
				break
			check += 1
		if check == 1:
			j+=1
		else:
			print("ASD")
			
			print("ASD2")
			c[i][j] = 0
			if j == 0:
				j=4
				i-=1
			else:
				j-=1
				
			del rowcontents[i][c[i][j]]
			del columncontents[j][c[i][j]]
	
	i+=1
	j=0
	
print(c)