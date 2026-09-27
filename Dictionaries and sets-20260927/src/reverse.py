##
#  This program reads, scales and reverses a sequence of scores.
#

def main():
   scores = readFloats(5)
   multiply(scores, 10)
   print("\nReversed numbers: ")
   printReversed(scores)

## Reads a sequence of floating-point numbers.
#  @param numberOfInputs the number of inputs to read
#  @return a list containing the input values
#
def readFloats(numberOfInputs):
   print("Enter", numberOfInputs, "numbers:")
   inputs = []
   for i in range(numberOfInputs):
      value = float(input(""))
      inputs.append(value)
      
   return inputs

## Multiplies all elements of a list by a factor.
#  @param values a list of numbers
#  @param factor the value with which element is multiplied
#
def multiply(values, factor):
   for i in range(len(values)):
      values[i] = values[i] * factor

## Prints a list in reverse order.
#  @param values a list of numbers
#
def printReversed(values):
   for value in reversed(values):
     print(value)
   
# Start the program.
main()
