sentence = input("Lütfen bir cümle giriniz.")
list1 = []
list2 = []
for i in sentence:
    if i not in list1 :
        list1.append(i)
        list2.append(sentence.count(i))

dict = dict(zip(list1,list2))

print(dict)