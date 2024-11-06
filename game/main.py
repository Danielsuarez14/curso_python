import random
print('Bienvenido al juego piedra, papel y tijera')

def choose_options():
  options = ['piedra', 'papel', 'tijera']
  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()
  computer_option = random.choice(options)
  if not user_option in options:
    print('Esa opción no es válida')
    # continue
    return None, None
  return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    try:
        if user_option == computer_option:
            print('Empate')
        elif user_option == 'piedra':
            if computer_option == 'tijera':
                print('Piedra gana a tijera\n')
                print('Punto para el user 🧑\n')
                user_wins += 1
            else:
                print('Papel gana a piedra\n')
                print('Punto para el computador 🤖\n')
                computer_wins += 1
        elif user_option == 'tijera':
            if computer_option == 'papel':
                print('Tijera gana a Papel\n')
                print('Punto para el user 🧑\n')
                user_wins += 1
            else:
                print('Piedra gana a tijera\n')
                print('Punto para el computador 🤖\n')
                computer_wins += 1
        elif user_option == 'papel':
            if computer_option == 'piedra':
                print('Papel gana a piedra\n')
                print('Punto para el user 🧑\n')
                user_wins += 1
            else:
                print('Tijera gana a papel\n')
                print('Punto para el computador 🤖\n')
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
      print('El ganador es el usuario🧑')
      break
    elif computer_wins == 3:
      print('El ganador es la computadora 🤖')
      break


run_game()
