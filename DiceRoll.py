#DiceRoll.py
#Name:Mauricio Martinez
#Date:02/26/25
#Assignment:Lab 6
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  numRolls=10000
  for count in range(10000):
   
     dice1=random.randint(1,6)
     dice2=random.randint(1,6)
     total=dice1 + dice2
     rolls[total-2]=rolls[total-2] +1
     #print(dice1,dice2,total)

  
  #find the sum total of the two dice
  
  #print statictics for dice rolls
  num=2
  
  for r in rolls:
    percent=r/numRolls * 100,1
    print(num,":",r,percent)
    num=num+1
    #print(r)
if __name__ == '__main__':
  main()
