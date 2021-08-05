
def my_prime():
      re_mainder = 0
      numero = 0
      numero_sq = 0.0
 #Aprime number is diviable by1 and itself composite numbers
      numero = int(input("Please pick a random number from your head:  "))
      if numero <= 1:
         print('Please number cannot be less or equal to 1')
      elif numero > 1 and numero %2 == 0:
         print(" This is not a prime number, try another ")
         return      
      numero_sq = round((numero **.5))
      fraction = False
      for p in range(2,numero_sq-1):
         if numero_sq % p != 0: fraction = True
         break
      print(f"{numero},{p} : This is  prime number")
    
      #print(" {} My friend that's a whole number ".format(numero))
my_prime()
cd43687ca9d6c8a721de1c7d8bc97f23d3ad0c6f
