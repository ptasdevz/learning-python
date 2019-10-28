

secret_word = "python"
input_word =  ""
guess_limit = 3
guess_count =0;


while input_word != secret_word:
    if guess_count < guess_limit:
        input_word = input("Enter word: ")
        guess_count +=1
    else:
        break

if guess_count == guess_limit:
    print("you are out of guesses, YOU LOST!")
else:
    print ("you win!!")