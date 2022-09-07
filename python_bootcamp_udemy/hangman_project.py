import random
from hangman_art import stages, logo # 모듈 활용하기
from hangman_words import word_list # 모듈 활용하기 
from replit import clear # 절차에 따른 화면 하나만 보여주기

print(logo)

# While문에서 활용하기 위해 초기값 설정
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# 글자 수 만큼 ["_","_","_","_","_",] 만들기
display = []
for _ in range(word_length):
    display += "_"


# 철자 맞추기 반복하기
while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    #Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    # 틀리면 목숨 차감하기
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True # while문 종결 코드
            print("You lose.")
    
    if not "_" in display:
        game_is_finished = True # while문 종결 코드
        print("You win.")

    print(stages[lives])