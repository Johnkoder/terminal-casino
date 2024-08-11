import random
import os
import time

def clear():
    os.system("cls || clear")

def is_money_valid(input_money):
  return type(input_money) != str or input_money >= 1

class Casino:
  def __init__(self):
    self.savings = 0
 
  def deposit(self):
    self.savings += amount

  def pick_game(self):
    game_num = int(input("Press 1 to play COINFLIP -- 2 for ROULETTE -- 3 for SLOTS -- 4 to EXIT: "))
    return game_num
  
  def render(self):
    print(f"Savings: ${self.savings}")

  def no_money_msg(self):
    print("You don't have enough savings.")
    time.sleep(4)


class CoinFlip:
  def __init__(self):
    self.bet = 0
    self.sides = ["heads", "tails"]
    self.user_side = None

  def enter_bet(self):
    bet_amt = int(input("Enter your BET: "))
    self.bet = bet_amt
    return bet_amt

  def play(self):
    self.user_side = input("Heads or Tails?: ")
    winning_side = random.choice(self.sides)

    if self.user_side == winning_side:
      self.render(1)
      return self.bet * 2
    else:
      self.render(0)
      return 0

  def render(self, outcome):
    print("Flipping...")
    time.sleep(2)
    if outcome == 1:
      print("You win!")
      print(f"You won ${self.bet * 2}!")
    else:
      print("You Lost.")


class Roulette:
  def __init__(self):
    self.bet = 0
    self.nums = []
    self.user_nums = []
    self.correct = 0

  def enter_bet(self):
    bet_amt = int(input("Enter your BET: "))
    self.bet = bet_amt
    return bet_amt

  def play(self):
    while(len(self.user_nums) < 5):
      clear()
      print(f"Your chosen numbers: {self.user_nums}")
      rnd_num = random.randint(1,10)

      if rnd_num not in self.nums:
        user_num = int(input("Pick 5 numbers (1 to 10): "))
        if user_num < 1 or user_num > 10:
          print("Choose a number from 1 to 10!")
          time.sleep(2)
          continue
      else: 
        continue

      if user_num in self.user_nums:
        print("Do not repeat your number!")
        time.sleep(2)
        continue

      self.nums.append(rnd_num)
      self.user_nums.append(user_num)  

    # animation function
    self.animate_roulette();

    correct_ans = list(filter(lambda x: x in self.nums, self.user_nums))
    self.correct += len(correct_ans)
    
    return (self.bet * 0.30) * 2 * self.correct
  
  # roulette animation
  def animate_roulette(self):
    count_ans = 0

    while count_ans < 5:
      range_num = 10
      for i in range(1, 5):
        if i == 4:
          range_num = self.nums[count_ans]
          count_ans += 1

        for j in range(0, range_num):
          clear()
          print("[1][2][3][4][5][6][7][8][9][10]")
          pointer = ["---"]*10
          pointer[j] = "-^-"
          print(''.join(e for e in pointer))
          print(f"Your numbers: {self.user_nums}")
          
          if i == 4:
            time.sleep(0.2)
          else:
            time.sleep(0.1)

      print(f"Winning numbers: {self.nums[:count_ans]}")
      time.sleep(3)

  
  def render(self, total_winnings):
    print(f"You got {self.correct} correct guesses!")
    print(f"You won ${total_winnings}")


# Slots class
class Slots:
  def __init__(self):
    self.fee = 100
    self.combos = list(range(1,5))
    self.win_combos = []
    self.num_value = {
      "1": 10,
      "2": 20,
      "3": 30,
      "4": 40,
      "5": 50
    }

  def play(self):
    print(f"Slots fee: ${self.fee}")
    input("Enter any KEY to roll!: ")

    while(len(self.win_combos) < 3):
      self.win_combos.append(random.choice(self.combos))

    winnings = self.num_value[str(self.win_combos[0])] + self.num_value[str(self.win_combos[1])] + self.num_value[str(self.win_combos[2])]

    if all(i == 5 for i in self.win_combos):
      winnings *= 3
    elif all(i == self.win_combos[0] for i in self.win_combos):
      winnings *= 2

    self.animate_slots()

    return winnings

  def animate_slots(self):
    count_ans = 0
    x = random.randint
    output = [x] * 9

    while count_ans <= 3:
      if count_ans == 1:
        output_copy = output[:]
        output_copy[0] = x(1,5)
        output_copy[3] = self.win_combos[0]
        output_copy[6] = x(1,5)
        output = output_copy
      elif count_ans == 2:
        output_copy = output[:]
        output_copy[1] = x(1,5)
        output_copy[4] = self.win_combos[1]
        output_copy[7] = x(1,5)
        output = output_copy
      elif count_ans == 3:
        output_copy = output[:]
        output_copy[2] = x(1,5)
        output_copy[5] = self.win_combos[2]
        output_copy[8] = x(1,5)
        output = output_copy

      for i in range(1,20):
        clear()
        inner_output = output[:]
        final_string = ''
        for j, item in enumerate(inner_output):
          if type(item) is not int:
            final_string += f"[{str(item(1,5))}]"
          else:
            final_string += f"[{str(item)}]"
          
          if j == 2 or j == 5 or j == 8:
            final_string += '\n'

        print("- SLOTS -")
        print(final_string)
        time.sleep(0.05)

      count_ans += 1
      
        
  
  def render(self, total_winnings):
    print(f"[{self.win_combos[0]}] [{self.win_combos[1]}] [{self.win_combos[2]}]")
    print(f"You won ${total_winnings}")


casino = Casino()

# Main loop
while True:
  clear()
  casino.render()
  answer = int(input("Press 1 to DEPOSIT -- 2 to PICK A GAME: "))

  if answer == 1:
    clear()
    amount = int(input("Enter amount to deposit: "))
    if is_money_valid(amount):
      casino.deposit()
    else:
      print("Please input a valid number.")
      time.sleep(4)
      continue
  elif answer == 2:
    game = None

    while(game != 4):
      clear()
      casino.render()
      game = casino.pick_game()

      if game == 1:
        coin_flip = CoinFlip()

        clear()
        total_bet = coin_flip.enter_bet()
        if total_bet > casino.savings:
          casino.no_money_msg()
          continue
        casino.savings -= total_bet
        total_winnings = coin_flip.play()
        casino.savings += total_winnings

        casino.render()
        time.sleep(4)
      elif game == 2:
        roulette = Roulette()

        clear()
        total_bet = roulette.enter_bet()
        if total_bet > casino.savings:
          casino.no_money_msg()
          continue
        casino.savings -= total_bet
        total_winnings = roulette.play()
        casino.savings += total_winnings

        roulette.render(total_winnings)
        time.sleep(4)
      elif game == 3:
        slots = Slots()

        clear()
        if casino.savings < slots.fee:
          casino.no_money_msg()
          continue
        casino.savings -= slots.fee
        total_winnings = slots.play()
        casino.savings += total_winnings

        slots.render(total_winnings)
        time.sleep(4)
      elif game == 4:
        continue