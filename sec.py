import random
import hashlib
import string

letters = string.lowercase

def generateMatrixFromFile(f):
	digest = getDigest(f.read())
	matrix = generateMatrix(digest)
	print(matrix)
	return matrix

def generateMatrix(digest):
	l = []
	print(digest)
	digest = toNumbers(digest)
	while len(digest)!=0:
		subl = []
		digestSlice = digest[:2]
		subl.append(int(digestSlice[0])*30)
		subl.append(int(digestSlice[1])*30)
		l.append(subl)
		digest = digest[2:]
	return l

def toNumbers(digest):
	newDigest = ''
	i = 0 
	while i<len(digest):
		if digest[i] in letters:
			newDigest+=str(letters.index(digest[i])+1)
		else :
			newDigest+=str(digest[i])
		i+=1
	return newDigest

def getDigest(data):
	hash_object = hashlib.sha256(data)
	hex_dig = hash_object.hexdigest()
	return hex_dig