#save file as psc.py
def asc2():
	for i in range(256):
		c = chr(i)
		print ("[", i,"=",c,"]", end="")
		if (i % 10 == 0):
				print("\n")
def main():
	asc2()
	
main() 

