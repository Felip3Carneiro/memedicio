oi Felipe dict = {
    "Cringe": "algo vergonhoso ou constrangedor",
    "Stalkear": "investigar a vida de alguém online",
    "Vdd": "abreviação da palavra |verdade|",
    "Hater": "pessoa que está constantemente criticando os outros",
    "Boila": "conjundo de fitas pequenas",
    "Reentrância": "cavidade, depressão a uma superficie relativo ao seu nivel"
        }

def achar():
    word = str(input("Digite uma palavra moderna que voce nao entende: \n 0 - Dicionario inteiro"))
    print("\n")
    
    if word == "0":
        for words in dict:
            print(words+":")
            print("É", dict[words])
            print("\n")
            
    if word.capitalize() in dict:
        print(word+":")
        print("É", dict[word])
        
    else:
        print("Tente novamente!")

    achar()

achar()
