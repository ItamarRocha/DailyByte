"""
This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

Ex: Given the following strings...

	"USA", return true
	"Calvin", return true
	"compUter", return false
	"coding", return true
"""

# Time O(n) n->len of string | Space O(1)
"""
	Basically, we check the first two chars to see how our string must behave. If the second is capitalized and the first is not,
	then we can return False. If thats not true, it means that for the next chars, the result of is_cap must be equal to the sec
	ond_cap.
"""
def correct_capitalization(string):
	if len(string) <= 1:
		return True
	first_cap = is_cap(string[0])
	second_cap = is_cap(string[1])
	
	if second_cap and not first_cap:
		return False
	
	for i in range(2, len(string)):
		if is_cap(string[i]) != second_cap:
			return False

	return True

def is_cap(char):
	return 65 <= ord(char) <= 90

print(correct_capitalization("USA"))
print(correct_capitalization("Calvin"))
print(correct_capitalization("CompUter"))
print(correct_capitalization("coding"))