import hashlib

i = 0
a = str(input("Enter the hash you want to Decrypt?\n"))

b = str(i)
hashB = hashlib.sha256(b.encode())
resultB = hashB.hexdigest()

while(a != resultB):
  i += 1
  b = str(i)
  hashB = hashlib.sha256(b.encode())
  resultB = hashB.hexdigest()

print("Your Decrypted Hash Number is: " + b)