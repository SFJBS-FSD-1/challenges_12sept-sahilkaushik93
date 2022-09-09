# allow 7 chances to each attempt
# if num generated is greater or smaller than the user input then notify the user
# if user is able to guess correctly notify user and congratulate user and tell how many attempts user took to crack it
# if user not able to crack it print all chances exhausted

# import random
# computer_number = random.randint(1,100)
#
# chances_took = []
# for i in range(1,8):
#     user_number = int(input("Time to Guess and Test your luck, Choose a number b/w 1 to 100: "))
#
#     if user_number == computer_number:
#         print("Congratulations you are a born Gambler !!")
#         chances_took.append(i)
#         total_chances = len(chances_took)
#         print(f"You cracked the game in {total_chances}")
#     elif user_number > computer_number:
#         print("your guessed number is greater than computer number")
#     elif user_number < computer_number:
#         print("your guessed number is smaller than computer number")
#
# else:
#     print("OOPS!! you have exhausted all your chances.")
#     print(f"The number you needed to win was: {computer_number}")


from passlib.hash import pbkdf2_sha256
password = "hello"
hashed = pbkdf2_sha256.hash(password)
print(hashed)

if pbkdf2_sha256.verify("hello", hashed):
    print("pw matched successfully")
else:
    print("pw didn't matched")



