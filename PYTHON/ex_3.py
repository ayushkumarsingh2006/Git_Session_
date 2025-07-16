#AYUSH KUMAR SINGH USN:-2102408006
#wap to read a atring and print all characters except vowels
text = input("enter the word:>")
vowels = 'AEIOU'.lower()

for char in text:
    if char in vowels:
        continue
    print(char)