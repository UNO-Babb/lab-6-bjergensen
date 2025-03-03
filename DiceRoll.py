#DiceRoll.py
#Name:
#Date:
#Assignment:
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  sum_rolls = [0] * 11
  #Create two dice values ranging from 1 - 6 each
  for r in range(10000):
    dice1 = random.randint(1,6)
    rolls[dice1 - 1] = rolls[dice1 - 1] + 1
    dice2 = random.randint(1,6)
    rolls[dice2 - 1] = rolls[dice2 - 1] + 1

  #find the sum total of the two dice
    sum_total = dice1 + dice2
    sum_rolls[sum_total - 2] += 1
  #print statictics for dice rolls
  dice = 1
  for count in rolls:
    print(dice, ":", count)
    dice = dice + 1

  print("two dice")
  for i in range(2, 13):
    print(i, ":", sum_rolls[i - 2])

if __name__ == '__main__':
  main()
