def somma(val1,val2):
      return int(val1)+int(val2)
def sottrazione(val1,val2):
      return  int(val1)-int(val2)
def moltiplicazione(val1,val2):
      return  int(val1)*int(val2)
def divisione(val1,val2):
      return int(val1)/int(val2)

print("premi 1 per somma\npremi 2 per sottrazione\n"
      "premi 3 per moltiplicazione\npremi 4 per divisione")
val = (input("inserisci il numero: "))

op1 = input("inserisci op1: ")
op2 = input("inserisci op2: ")

if int(val) == 1:
      res = somma(op1,op2)
      print("il risultato della somma di "+op1+" e di "+op2+" è: "+str(res))

elif int(val) == 2:
      res = sottrazione(op1,op2)
      print("il risultato della sottrazione di " + op1 + " e di " + op2 + " è: " + str(res))

elif int(val) == 3:
      res = moltiplicazione(op1,op2)
      print("il risultato della moltiplicazione di " + op1 + " e di " + op2 + " è: " + str(res))

elif int(val) == 4:
      res = divisione(op1,op2)
      print("il risultato della divisione di " + op1 + " e di " + op2 + " è: " + str(res))

else:
      print("comando errato")



