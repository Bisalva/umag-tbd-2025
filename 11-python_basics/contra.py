def contra(contra_len):
    lista_dic = ["a","b","c","d","e","f","g","h","i","j","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for contra in range(contra_len):
        str = random.choices(lista_dic)
        contralista = contralista.join(str)
    print(contralista)      

contra(10)