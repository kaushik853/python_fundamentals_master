'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''
string = input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print(f"Number of vowels are: {vowels}")
