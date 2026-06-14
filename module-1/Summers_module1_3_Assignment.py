#Jack Summers Module 1.3 Assignment
#06/14/2026
#purpose: User enters the number of beer bottles they have on a wall. Program counts down by 1 until user runs out of beer.


def count_bottles(bottles):
    #while loop to count down, + print msg
    #stops at 1 bottle of beer, and prints special message
    while bottles > 1:
        print(f'{bottles} bottles of beer on the wall, {bottles} bottles of beer.')
        print(f'Take one down and pass it around, {bottles-1} bottle(s) of beer on the wall.')
        print()
        bottles -= 1

        #there's got to be a better way to write this, I just came back from vacation and my brain is rusty.
        #I hate leaving so much duplicated code in here.
        #I should probably make some sort of print function since that's where all the duplication is coming from,
        #but I am on a time crunch this week. Next week I will have more time to spend on assignments.
        if bottles == 1:
            print(f'{bottles} bottle of beer on the wall, {bottles} bottle of beer.')
            print(f'Take one down and pass it around, {bottles-1} bottle(s) of beer on the wall.')
            print()
            bottles -= 1


    #while loop stops at 1 bottle, then subtracts bottle to 0
    #once bottle hits 0, this prints the re-stock message
    if bottles == 0:
        print("WE'RE OUT OF BEER!\nTime to buy more bottles of beer.")
        print('-'*553)


def main():
    #captures number of bottles on the wall
    #passes that number into the fuction count_bottles().
    num_bottles = int(input("Enter number of bottles: "))
    print()
    count_bottles(num_bottles)

if __name__ == '__main__':
    main()



