def dictionary(word):
    dic ={}
    word = word.lower()
    for i in word:
        dic[i] = dic.get(i,(0))+1
    return print(dic)
dictionary("LoOk")