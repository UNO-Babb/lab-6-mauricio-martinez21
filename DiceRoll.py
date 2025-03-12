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

#WordCount.py
#Name:mauricio martinez
#Date:02/26/25
#Assignment:Lab 6 

def main():
  textFile = open("fish.txt", 'r')
  lineCount=0
  wordCount=0
  letterCount=0


  
  for line in textFile:
    lineCount+=1
    print(line)
    words=line.split()
    
    for word in words:
      wordCount+=1
      print("Lines:",lineCount)
      print("word:wordCount")
      words=line.split()
      
      for letter in word:
        print(letter)
  
  print("lines:",lineCount)

if __name__ == '__main__':
  main()

  #WordIndex.py
#Name:Mauricio Martinez
#Date:02/26/25
#Assignment:Lab 6

def main():
  textFile = open ("gettysberg.txt",'r')
                  
  wordList = {} #create an empty dictionary

  LineNum=0
  for line in textFile:
    LineNum = LineNum + 1
    words=line.split()
    for word in words:
      word=word.lower()
      word=word.replace(",","")
      word=word.replace(".","")
      word=word.replace("\n","")
      word=word.replace("!","")
    
      if word in wordList:
        wordList[word].append(LineNum) #add to existing entry 
      else:
        wordList[word]=[LineNum] #add word to list

  print(wordList)
  for word in wordList:
    print(word,wordList[word])
    
    
 



if __name__ == '__main__':
  main()