"""
This question is asked by Amazon. Given two strings representing sentences, return the words that are not common to both strings (i.e. the words that only appear in one of the sentences). You may assume that each sentence is a sequence of words (without punctuation) correctly separated using space characters.

Ex: given the following strings...

    sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
    sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", return ["beat", "to", "lost"]
    sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]
"""

def uncommonwords(sentence1, sentence2):
    sentence1 = sentence1.split(" ")
    sentence2 = sentence2.split(" ")

    uncommonset1 = set(sentence1)
    uncommonset2 = set(sentence2)

    for el in sentence1:
        if el in uncommonset2:
            uncommonset2.remove(el)

    for el in sentence2:
        if el in uncommonset1:
            uncommonset1.remove(el)

    output = []

    for el in uncommonset1:
        output.append(el)

    for el in uncommonset2:
        output.append(el)          
        
    return output

print(uncommonwords("the quick", "brown fox"))
print(uncommonwords("the tortoise beat the haire", "the tortoise lost to the haire"))
print(uncommonwords("copper coffee pot", "hot coffee pot"))