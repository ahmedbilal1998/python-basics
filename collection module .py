from collections import Counter
numbers=[1,2,2,3,3,4]
count = Counter(numbers)
print(count)
text= "haleema"
result= Counter(text)
print(result)
data=["apple","mango", "orange", "kiwi"]
c= Counter(data)
c.update(['grapes','gobi'])
print(c)
votes=["ali","sara","ahmed","ali","sara","haleema"]
c=Counter(votes)
c.update(["waqas"])
print(c)

