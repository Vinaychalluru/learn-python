# 1) Ask for user input. Store it in a variable. Print it
# 2) Ask for user input two times. Concatenate the inputs and Print it 
# 3) Ask for two user inputs. One a string. Another an integer. Concatenate both and Print it
# 4) Ask for two user inputs. Both integer. Add them and Print the output of their sum
# 5) Ask for two user inputs. Both integer. Divide and print the remainder
# 6) In the above #5, if the second number is 0, print 'Not possible to divide'
# 7) Print Numbers 1 to 10 using a for loop
# 8) Print Numbers 1 to 10 using a While loop

numbers = [1,4,5,6,77,554,333,6665,44]

numbers

for number in numbers:
    if number%2 == 0:
        print("Even number is", number)
    else :
        print("Odd number is", number)
