def palin_texto(texto_test_2):
    if texto_test_2[::-1] == texto_test_2:
        print("es palindromo")
    else :
        print("no es palindromo")

palin_texto("ana")