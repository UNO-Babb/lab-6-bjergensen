#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("gettysberg.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0
  for line in textFile:
    lineCount += 1
    words = line.split()
    wordCount += len(words)
    for char in line:
      if char.isalpha():
        letterCount += 1
    # print(line)
  
  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Letters:", letterCount)
  

if __name__ == '__main__':
  main()
