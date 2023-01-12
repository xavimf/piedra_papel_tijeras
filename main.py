import random

options = ('piedra', 'papel', 'tijera')
computer_wins = 0
user_wins = 0
rounds = 1

print('-' * 43)
print('|  BIENVENID@! - PIEDRA, PAPEL O TIJERAS  |')
print('-' * 43)

while True:
  print('*' * 15)
  print('    ROUND', rounds)
  print('*' * 15)

  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()
  print('\n')
  
  if not user_option in options:
    print('Esa opción no es valida!!! Vuelve a intentarlo ')
    continue
    
  computer_option = random.choice(options) #escoger de forma aleatoria un elemento de la lista options
  
  print('User option => ', user_option)
  print('Computer option => ', computer_option)
  
  if user_option == computer_option:
    print('<< EMPATE! >>')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('<< Piedra gana a tijera >>')
      print('Usuario gano esta ronda!')
      user_wins += 1
    else:
      print('<< Papel gana a piedra >>')
      print('Computadora gano esta ronda!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('<< Papel gana a piedra >>')
      print('Usuario gano esta ronda!')
      user_wins += 1
    else:
      print('<< Tijera gana a papel >>')
      print('Computadora gano esta ronda!')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('<< Tijera gana a papel >>')
      print('Usuario gano esta ronda!')
      user_wins += 1
    else:
      print('<< Piedra gana a tijera >>')
      print('Computadora gano esta ronda!')
      computer_wins += 1

  print('\n')
  print('>> Computer: ', computer_wins)
  print('>> Usuario: ', user_wins)
  print('\n')
  
  if computer_wins == 2:
    print('*' * 22)
    print(' Gano la computadora!')
    print('*' * 22)
    break
  if user_wins == 2:
    print('*' * 18)
    print(' Gano el usuario!')
    print('*' * 18)
    break
  rounds += 1