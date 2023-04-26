def say_the_number(n):
	d = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
	teens = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
	tens = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
	
	def say_small(n):
		if n>=20: return tens[n//10] + "-"*bool(n%10) + d[n%10]*bool(n%10)
		if n>=10: return teens[n]
		return d[n]
	
	def say_smaller(n):
		
		return (d[n//100]+" hundred")*bool(n//100) + " and "*(bool(n//100) and bool(n%100)) + say_small(n%100)*bool(n%100)
		
	if n==0: return "Zero."
	
	n_cla = ["", " thousand", " million", " billion", " trillion"]
	cla = [(n//(10**(3*i)))%1000 for i in range(5)]
	
	pieces = [say_smaller(cla[i]) + n_cla[i] for i in range(5) if cla[i]!=0]
	
	ans = ", ".join(pieces[1:][::-1]) + " and " + pieces[0] if len(pieces)>1 and cla[0]<100 else ", ".join(pieces[::-1]) if len(pieces)>1 else pieces[0]
	
	return ans[0].upper() + ans[1:] + "."
	

    
