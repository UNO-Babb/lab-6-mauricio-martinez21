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
