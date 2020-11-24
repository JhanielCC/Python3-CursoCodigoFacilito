import sys

#          ==
if __name__!='main':
    if len(sys.argv)==1:
        print("Es necesario colocar por lo menos un argumento")
    else:
        if sys.argv[1] == 'help':
            print("Puedes contactar a soporte para ayuda, jhaart3@gmail.com")
        print(sys.argv[1])

