# "Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

## for loop that will print numbers 1 thru 100 (range goes up to 101 bc the last number is not printed/looped thru )
for i in range (1, 101):
    # asking immediately if number is divisible by BOTH 3 AND 5, so that there are no inaccuracies in printing; if both conditions are true, "FizzBuzz" is printed
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # if number isnt divisble by BOTH 3 AND 5, an else if (elif) statement asks if the number is divisible just by 5 
    # if this is the case, just "Buzz" is printed
    elif i % 5 == 0:
        print("Buzz")
    #if number isnt divisble by BOTH 3 and 5 OR just 5, an else if (elif) statement asks if the number is divisible just by 3
    # if this is the case, just "Fizz" is printed
    elif i % 3 == 0:
        print("Fizz")
    # if the number is NOT divisible by either 3 or 5, then the number will hit the last statement (else)
    # the number in the sequence is just then printed
    else: 
        print(i)