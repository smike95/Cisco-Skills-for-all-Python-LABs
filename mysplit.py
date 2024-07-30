def mysplit(strng):
    mylist = []
    print(strng, "Lenth of strng is " + str(len(strng)) + "\n", sep = "\n")
    #'''
    while len(strng) > 1:
        print(strng, "Lenth of strng is " + str(len(strng)) + "\n", sep = "\n")
        substrng = strng.lstrip()[:strng.find(" ")] # в останньому колі він не знаходить пробіла і find() певертає -1, тому сабстрінг залищається без останньої літери а стрнг на завжди лишається довжиною 1 і мість ту саму литеру
        mylist.append(substrng)
        strng = strng.lstrip(substrng).lstrip()
    return mylist
    #'''


print(mysplit("To be or not to be, that is the question"))

    