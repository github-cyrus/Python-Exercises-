import random

def game(Pc  , User):
      if Pc == User:
            return None
      if Pc == 's':
            if User == 'w':
                  return False
            elif User == 'g':
                  return True
      elif Pc == 'w':
            if User == 's':
                  return True
            elif User == 'g':
                  return 
      elif Pc == 'g':
            if User == 's':
                  return False
            elif User == 'w':
                  return True


print("Computer Turm : Snake(s), Water(w) Or Gun(g)?")

Pc = random.randint(1,3)

if Pc == 1:
      Pc = "s"
elif Pc == 2:
      Pc = "w"
elif Pc == 3:
      Pc = "g"

User = input("Yours Turn : Snake(s), Water(w) Or Gun(g)? ")
 
print(f"Computer Choose {Pc}")
print(f"You Choose {User}")

if game == None:
      print("Game is Tie")
elif game == False :
      print("You Loose !!")
else :
      print("You Win !!")


game(Pc , User)
 