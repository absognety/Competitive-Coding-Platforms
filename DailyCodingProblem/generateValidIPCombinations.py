"""
Daily Coding Problem #213

This problem was asked by Snapchat.

Given a string of digits, generate all possible valid IP address 
combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are 
numbers between 0 and 255. Zero-prefixed numbers, such as 01 and 065, 
are not allowed, except for 0 itself.

For example, given "2542540123", you should return 
['254.25.40.123', '254.254.0.123'].

"""

# Python3 code to check valid possible IP 

# Function checks whether IP digits 
# are valid or not. 
def is_valid(ip): 

	# Splitting by "." 
	ip = ip.split(".") 
	
	# Checking for the corner cases 
	for i in ip: 
		if (len(i) > 3 or int(i) < 0 or
						int(i) > 255): 
			return False
		if len(i) > 1 and int(i) == 0: 
			return False
		if (len(i) > 1 and int(i) != 0 and
			i[0] == '0'): 
			return False
			
	return True

# Function converts string to IP address 
def convert(s): 
	
	sz = len(s) 

	# Check for string size 
	if sz > 12: 
		return [] 
	snew = s 
	l = [] 

	# Generating different combinations. 
	for i in range(1, sz - 2): 
		for j in range(i + 1, sz - 1): 
			for k in range(j + 1, sz): 
				snew = snew[:k] + "." + snew[k:] 
				snew = snew[:j] + "." + snew[j:] 
				snew = snew[:i] + "." + snew[i:] 
				
				# Check for the validity of combination 
				if is_valid(snew): 
					l.append(snew) 
					
				snew = s 
				
	return l 

# Driver code		 
A = "25525511135"
B = "25505011535"
C = "2542540123"

print(convert(A)) 
print(convert(B))
print (convert(C))