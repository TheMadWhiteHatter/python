from random import randint
def randlist(r):
	alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","10","`","[","]"","",""\","";","’",","".""/","~""!","@""","#","$","%","^","&","*","(",")","_","+","{","}","|",":","”","<",">""?"] 
	usedlist[r] = 1
	c = alpha[r]
	return c 
	
def main():
	count = 0
	checklist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	while True:
		r = randint(0,96)
		print(checklist)
		checklist[r]=1
		c = randlist(r)
		print(c, end="")
		if (count == 26):
			break
		count = count+1
	print()
if __name__ == '__main__':
	main()
