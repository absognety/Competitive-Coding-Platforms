
def encrypted_string(strg):
    EncryptedString = [strg[0]]
    for t in range(1,len(strg)):
        if (t%2 == 1):
            EncryptedString.append(strg[t])
        else:
            EncryptedString.insert(0,strg[t])
    return (''.join(EncryptedString))

print (encrypted_string('geeks'))
print (encrypted_string('geeksforgeeks'))
print (encrypted_string('strive'))
print (encrypted_string('vikaschitturi'))
print (encrypted_string('padmachitturi'))
print (encrypted_string('hackerrank'))
print (encrypted_string('hackerearth'))
print (encrypted_string('codechef'))
print (encrypted_string('IamVikas'))
print (encrypted_string('HelloHowareyou'))
print (encrypted_string('whatareyoudoing'))




def decrypted_string(strg):
    if (len(strg)%2!=0):
        DecryptedString = [strg[0]]
        for t in range(1,len(strg)):
            DecryptedString.append(strg[-1*t])
            DecryptedString.append(strg[t])
        DecryptedString = DecryptedString[:len(strg)][::-1]
        return (''.join(DecryptedString))
    else:
        reverse_strg = strg[::-1]
        DecryptedString=[reverse_strg[0]]
        for t in range(1,len(reverse_strg)):
            DecryptedString.append(reverse_strg[-1*t])
            DecryptedString.append(reverse_strg[t])
        DecryptedString = DecryptedString[:len(reverse_strg)][::-1]
        return (''.join(DecryptedString))
    
    
print(decrypted_string('segek'))
print(decrypted_string('segosegekfrek'))
print(decrypted_string('vrstie'))
print(decrypted_string('iuthskviacitr'))
print(decrypted_string('iuthadpamcitr'))
print(decrypted_string('nrechakrak'))
print(decrypted_string('hreechakrat'))
print(decrypted_string(encrypted_string('IamVikas')))
print(decrypted_string(encrypted_string('HelloHowareyou')))
print(decrypted_string(encrypted_string('whatareyoudoing')))

