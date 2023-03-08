secret_word = 'python'
guess = ''
guess_count = 0
guess_limit = 5
out_of_guesses = False


while secret_word !=guess and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input('Enter your guesses: ')
        guess_count += 1
    else:
        out_of_guesses = True    


if out_of_guesses:
    print('You Lose out of guesses')
else:
    print('You Win')    