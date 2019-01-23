strg = input().strip().split()
bin_to_string = ''
for s in strg:
    bin_to_string = bin_to_string + chr(int(s,2))
print (bin_to_string)

