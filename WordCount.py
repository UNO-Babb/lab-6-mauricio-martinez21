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
