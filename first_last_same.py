
# Link : https://pynative.com/python-basic-exercise-for-beginners/
# Ex3 : Write a code to return True if the first and last number of a list are the same

def first_last_same(lst):
  print("List given:", lst)
  print("Result is", lst[0] == lst[len(lst) - 1])

def main():
  numbers_x = [10, 20, 30, 40, 10]
  numbers_y = [75, 65, 35, 75, 30]

  first_last_same(numbers_x)
  first_last_same(numbers_y)

if __name__ == "__main__":
  main()
