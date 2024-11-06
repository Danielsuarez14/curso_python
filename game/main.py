import random
print('Welcome to the game rock, scissors and paper')

def choose_options():
  options = ['rock', 'scissors', 'paper']
  user_option = input('rock, scissors or paper => ')
  user_option = user_option.lower()
  computer_option = random.choice(options)
  if not user_option in options:
    print('That option is not valid')
    # continue
    return None, None
  return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    try:
        if user_option == computer_option:
            print('Tie')
        elif user_option == 'rock':
            if computer_option == 'scissor':
                print('Rock beats Scissor\n')
                print('Point for the user 🧑\n')
                user_wins += 1
            else:
                print('Paper beats Rock\n')
                print('Point for the computer 🤖\n')
                computer_wins += 1
        elif user_option == 'scissor':
            if computer_option == 'paper':
                print('Scissor beats Paper\n')
                print('Point for the user 🧑\n')
                user_wins += 1
            else:
                print('Rock beats Scissors\n')
                print('Point for the computer 🤖\n')
                computer_wins += 1
        elif user_option == 'paper':
            if computer_option == 'rock':
                print('Paper beats Rock\n')
                print('Point for the user 🧑\n')
                user_wins += 1
            else:
                print('Scissors beats Paper\n')
                print('Point for the computer 🤖\n')
                computer_wins += 1
        return user_wins, computer_wins
    except Exception as e:
        print(f'Error: {e}')
  


def run_game():
  rounds = 1
  user_wins = 0
  computer_wins = 0
  while True:
    print('*' * 10)
    print('Round: ',rounds)
    print('*' * 10)
    print(f'''Computer points🤖 => {computer_wins}\n
User points🧑 => {user_wins}\n''')
    
    rounds += 1
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option,
                                           user_wins, computer_wins)
    print(f'''Computer option🤖 => {computer_option}
User option🧑 => {user_option}\n''')
    if user_wins == 3:
      print('User Wins🧑')
      break
    elif computer_wins == 3:
      print('Computer Wins 🤖')
      break


run_game()
