s = input(" Enter a string:")
vowels = sum(1 for char in s.lower() if char in 'aeiou')
print("total count:",vowels)