import random

attack_count = 0

bear_attack_count = 0
centaur_attack_count = 0
dragon_attack_count = 0

sword_swing_count = 0
bow_shot_count = 0

bear_alive = True
centaur_alive = True
dragon_alive = True
#make a class called player that tkes in a username, health amount and an item count.

class Player:
   def __init__(self, username, health,item_count, items, level):
      self.username = username
      self.health = health
      self.player_items = item_count
      self.items = items
      self.level = level


#boss class in this case a dragon.
class Boss:
  #funtion that takes in the dragons health, damage and level.
   def __init__(self, health, damage, level):
      self.health = health
      self.damage = damage
      self.level = level

#class that handles all of the potions
class Potions_Count:
   def __init__(self, heal, damage):
      self.heal = heal
      self.damage = damage

#class that handles all of the weapons like a sword and bow
#sword damage is 10 and bow damage is 5
class Weapons:
   def __init__(self):
      self.sword = "sword"
      self.bow = "bow"
      self.sword_damage = 10
      self.bow_damage = 5

#class of the mobs that the player will fight
class Mob:
   def __init__(self, health):
      self.health = health


def farm():
   print("Teleporting to a land to farm mobs.\n")
   print("While you are here, you will want to attack the mobs to gain weapon xp to help fight the dragon.")
   in_farm = True
   while in_farm is True:
      farm_input = input("Enter a command: \nAttack\nCheck\nLeave\n").lower()
      if farm_input == "attack":
         farm_weapon_input = input(f"Enter a weapon: {weapon1.sword} or {weapon1.bow}: ")
         if farm_weapon_input == "sword":
            mob_input = input("Enter a mob to attack: \nZombie\nSkeleton\n").lower()

            #Sword Zombie Farm
            if mob_input == "zombie":
               zombie.health -= weapon1.sword_damage
               print(f"You have attacked the {mob_input}")
               print(f"The {mob_input} has {zombie.health} health left\n")
               if zombie.health <= 0:
                  print("You have defeated killed a zombie!")
                  print("You have gained .05x damage on both weapons\n")
                  weapon1.sword_damage = weapon1.sword_damage * 1.05
                  weapon1.bow_damage = weapon1.bow_damage *  1.05
                  zombie.health = 20
            #Sword skeleton farm
            if mob_input == "skeleton":
               skeleton.health -= weapon1.sword_damage
               print(f"You have attacked the {mob_input}")
               print(f"The {mob_input} has {skeleton.health} health left\n")
               if skeleton.health <= 0:
                  print("You have defeated killed a skeleton!")
                  print("You have gained .02x damage on both weapons\n")
                  weapon1.sword_damage = weapon1.sword_damage * 1.02
                  weapon1.bow_damage = weapon1.bow_damage *  1.02
                  skeleton.health = 10

            #Bow farm
         if farm_weapon_input == "bow":
            mob_input = input("Enter a mob to attack: \nZombie\nSkeleton\n").lower()
            if mob_input == "zombie":
               zombie.health -= weapon1.bow_damage
               print(f"You have attacked the {mob_input}")
               print(f"The {mob_input} has {zombie.health} health left\n")
               if zombie.health <= 0:
                  print("You have defeated killed a zombie!")
                  print("You have gained .05x damage on both weapons\n")
                  weapon1.sword_damage = weapon1.sword_damage * 1.05
                  weapon1.bow_damage = weapon1.bow_damage *  1.05
                  zombie.health = 20
            #Bow skeleton farm
            if mob_input == "skeleton":
               skeleton.health -= weapon1.bow_damage
               print(f"You have attacked the {mob_input}")
               print(f"The {mob_input} has {skeleton.health} health left\n")
               if skeleton.health <= 0:
                  print("You have defeated killed a skeleton!")
                  print("You have gained .02x damage on both weapons\n")
                  weapon1.sword_damage = weapon1.sword_damage * 1.02
                  weapon1.bow_damage = weapon1.bow_damage *  1.02
                  skeleton.health = 10

         
      if farm_input == "check":
         print("Player Information:")
         player1.health = round(player1.health, 2)
         print(f"\nYour health is {player1.health}")
         #print(f"Your damage is {player1.damage}")
         print(f"Your sword damage is {weapon1.sword_damage}")
         print(f"Your bow damage is {weapon1.bow_damage}")

      if farm_input == "leave":
         in_farm = False

def check():
   print("\nPlayer Information:")
   player1.health = round(player1.health, 2)
   print(f"Your health is {player1.health}")
   weapon1.sword_damage = round(weapon1.sword_damage, 2)
   weapon1.bow_damage = round(weapon1.bow_damage, 2)
   print(f"Your sword damage is {weapon1.sword_damage}")
   print(f"Your bow damage is {weapon1.bow_damage}")
   print(f"Your level is {player1.level}\n")
   if bear_alive is True:
      print("Bear Information:")
      bear.health = round(bear.health, 2)
      print(f"The bear has {bear.health} health")
      print(f"The bear has {bear.damage} damage\n")
   elif centaur_alive is True:
      print("Centaur Information:")
      centaur.health = round(centaur.health, 2)
      print(f"The centaur has {centaur.health} health")
      print(f"The centaur has {centaur.damage} damage\n")
   elif dragon_alive is True:
      print("Dragons Information:")
      dragon.health = round(dragon.health, 2)
      print(f"The dragon has {dragon.health} health")
      print(f"The dragon has {dragon.damage} damage\n")

def heal():
   if potion1.heal <= 0:
      print("You have no more healing potions")
   else:
      player1.health += 50
      print(f"You have healed for {potion1.heal} health")
      print(f"Your health is now {player1.health}\n")
      potion1.heal -= 1

def strength():
   if potion1.damage <= 0:
      print("You have no more strength potions")
   else:
      print(f"You have increased both {weapon1.sword} and {weapon1.bow} damage by 1.25x")
      weapon1.sword_damage = weapon1.sword_damage * 1.25
      weapon1.bow_damage = weapon1.bow_damage * 1.25
      potion1.damage -= 1
   


player1 = input("Enter a character: \nBerzerker\nAssassin\nSiren\n").lower()

#Characters
berzerker = Player("Berzerker", 100, 0, [], 1) # Create a Player instance
assassin = Player("Assassin", 1150, 0, [], 1) # Create a Player instance
siren = Player("Siren", 200, 0, [], 1) # Create a Player instance

print("You will fight 3 different bosses...\n1. Grizzly Bear\n2. Centaur\n3. Dragon\n")

#Bosses
bear = Boss(100, 10, 1) # Create a Bear instance
centaur = Boss(500, 20, 1) # Create a Centaur instance
dragon = Boss(1500, 30, 1) # Create a Dragon instance


potion1 = Potions_Count(1, 1) # Create a Potion instance
weapon1 = Weapons() # Create a Weapon instance
zombie = Mob(20)
skeleton = Mob(10)


if player1 == "berzerker":
   player1 = berzerker
   print(f"You are {player1.username}")

if player1 == "assassin":
   player1 = assassin
   print(f"You are {player1.username}")
   weapon1.sword_damage = 20
   weapon1.bow_damage = 2

if player1 == "siren":
   player1 = siren
   print(f"You are {player1.username}")
   weapon1.sword_damage = 5
   weapon1.bow_damage = 20

while bear_alive is True:
   user_input = input("Enter a command: \nAttack\nCheck\nHeal\nStrength\nExit\nFarm\n:::Kill:::").lower()

   if user_input == "attack":
      weapon_input = input(f"Enter a weapon: {weapon1.sword} or {weapon1.bow}: ")
      if weapon_input == "sword":
         bear.health -= weapon1.sword_damage
         print("\nYou attacked the bear")
         if bear.health <= 0:
            print("\nYou have defeated the bear!")
            bear_alive = False
         else:
            bear.health = round(bear.health, 2)
            print(f"The bear has {bear.health} left\n")
         sword_swing_count += 1
         if sword_swing_count % 2 == 0:
            weapon1.sword_damage += weapon1.sword_damage * 0.5
            print(f"Your damage is {weapon1.sword_damage}")

      if weapon_input == "bow":
         bear.health -= weapon1.bow_damage
         print("\nYou attacked the bear")
         if bear.health <= 0:
            print("\nYou have defeated the bear!")
            bear_alive = False
         else:
            bear.health = round(bear.health, 2)
            print(f"The bear has {bear.health} left\n")
         bow_shot_count += 1
         if bow_shot_count % 2 == 0:
            weapon1.bow_damage += weapon1.bow_damage * 0.75
            print(f"Your damage is {weapon1.bow_damage}")
      
      attack_count += 1
      #Bear level up after two attacks
      if attack_count % 2 == 0:
         bear.level += 1
         bear.damage += bear.damage * 0.5
         bear.health += bear.health * 0.5
         print(f"The bear has leveled up to level {bear.level}")
         print(f"The bear has {bear.damage} damage")
         print(f"The bear has {bear.health} health\n")

      if attack_count % 5 == 0:
         crit_attack = random.randint(1, 10)
         bear.health -= crit_attack
         print(f"You have attacked the bear with a critical attack of {crit_attack}")
         if bear.health <= 0:
            print("\nYou have defeated the bear!")
            bear_alive = False
         else:
            bear.health = round(bear.health, 2)
            print(f"The bear has {bear.health} left\n")

      #Bear attacks player after two attacks
      bear_attack_count += 1
      if bear_attack_count % 2 == 0:
         print("While attacking the bear you also got attacked!\n")
         player1.health -= bear.damage
         player1.health = round(player1.health, 2)
         bear.health = round(bear.health, 2)
         print(f"The bear has {bear.health} health")
         print(f"You have {player1.health} health\n")


      #Player level up after two attacks
      player1.level += 1
      if player1.level % 2 == 0:
         print(f"You leveled up! Your new level is {player1.level}")
         player1.health += player1.health * 0.1
         player1.health = round(player1.health, 2)
         print(f"Your health is {player1.health}\n")
   
   if user_input == "check":
      check()
   
   if user_input == "heal":
      heal()

   if user_input == "strength":
      strength()

   if user_input == "exit":
      bear_alive = False
      centaur_alive = False
      dragon_alive = False
      break


   if user_input == "farm":
      farm()

   if player1.health <= 0:
      bear_alive = False
      centaur_alive = False
      dragon_alive = False
      break

if bear_alive is False:
   print("Since you managed to kill the Bear, it is time to up your damage.")
   print("Both your sword and bow have been increased by 3.5x damage.")
   weapon1.sword_damage = weapon1.sword_damage * 3.5
   weapon1.bow_damage = weapon1.bow_damage * 3.5
   print("You will fight the centaur...\n")


while centaur_alive is True:
   user_input = input("Enter a command: \nAttack\nCheck\nHeal\nStrength\nExit\nFarm\n:::Kill:::").lower()

   if user_input == "attack":
      weapon_input = input(f"Enter a weapon: {weapon1.sword} or {weapon1.bow}: ")
      if weapon_input == "sword":
         centaur.health -= weapon1.sword_damage
         print("\nYou attacked the centaur")
         if centaur.health <= 0:
            print("\nYou have defeated the centaur!")
            centaur_alive = False
         else:
            centaur.health = round(centaur.health, 2)
            print(f"The centaur has {centaur.health} left\n")
         sword_swing_count += 1
         if sword_swing_count % 2 == 0:
            weapon1.sword_damage += weapon1.sword_damage * 0.5
            print(f"Your damage is {weapon1.sword_damage}")
            player1.health = round(player1.health, 2)
            print(f"Your health is {player1.health}\n")
         
      if weapon_input == "bow":
         centaur.health -= weapon1.bow_damage
         print("\nYou attacked the centaur")
         if centaur.health <= 0:
            print("\nYou have defeated the centaur!")
            centaur_alive = False
         else:
            centaur.health = round(centaur.health, 2)
            print(f"The centaur has {centaur.health} left\n")
         bow_shot_count += 1
         if bow_shot_count % 2 == 0:
            weapon1.bow_damage += weapon1.bow_damage * 0.75
            print(f"Your damage is {weapon1.bow_damage}")

      attack_count += 1
      #Centaur level up after two attacks
      if attack_count % 2 == 0:
         centaur.level += 1
         centaur.damage += centaur.damage * 0.5
         centaur.health += centaur.health * 0.2
         print(f"\nThe centaur is level {centaur.level}\n")
         

      #If player attacks 5 times 
      if attack_count % 5 == 0:
         crit_attack = random.randint(30, 50)
         centaur.health -= crit_attack
         print(f"\nYou have landed a critical hit!\n")
         #format centaur health to end in 2 decimal places
         if centaur.health <= 0:
            print("\nYou have defeated the centaur!")
            centaur_alive = False
         else:
            centaur.health = round(centaur.health, 2)
            print(f"The centaur has {centaur.health} health\n")


      #Centaur attacks player after two attacks
      centaur_attack_count += 1
      if centaur_attack_count % 2 == 0:
         print("While attacking the centaur you also got attacked!\n")
         player1.health -= centaur.damage
         player1.health = round(player1.health, 2)
         centaur.health = round(centaur.health, 2)
         print(f"The centaur has {centaur.health} health")
         print(f"You have {player1.health} health\n")


      #Player level up after two attacks
      player1.level += 1
      if player1.level % 2 == 0:
         print(f"You leveled up! Your new level is {player1.level}")
         player1.health += player1.health * 0.1
         player1.health = round(player1.health, 2)
         print(f"Your health is {player1.health}\n")

   if user_input == "check":
      check()
   
   if user_input == "heal":
      heal()

   if user_input == "strength":
      strength()

   if user_input == "exit":
      bear_alive = False
      centaur_alive = False
      dragon_alive = False
      break


   if user_input == "farm":
      farm()

   if player1.health <= 0:
      bear_alive = False
      centaur_alive = False
      dragon_alive = False
      break

while dragon_alive is True:
   user_input = input("Enter a command: \nAttack\nCheck\nHeal\nStrength\nExit\nFarm\n").lower()
   if user_input == "attack":
      weapon_input = input(f"Enter a weapon: {weapon1.sword} or {weapon1.bow}: ")
      if weapon_input == "sword":
         dragon.health -= weapon1.sword_damage
         print("\nYou attacked the dragon")
         if dragon.health <= 0:
            print("You have defeated the dragon!")
            break
         else:
            dragon.health = round(dragon.health, 2)
            print(f"The dragon has {dragon.health} health\n")
         sword_swing_count += 1
         if sword_swing_count % 2 == 0:
            weapon1.sword_damage += weapon1.sword_damage * 0.5
            print(f"Your damage is {weapon1.sword_damage}")
            player1.health = round(player1.health, 2)
            print(f"Your health is {player1.health}\n")
      if weapon_input == "bow":
         dragon.health -= weapon1.bow_damage
         print("\nYou attacked the dragon")
         if dragon.health <= 0:
            print("You have defeated the dragon!")
            break
         else:
            dragon.health = round(dragon.health, 2)
            print(f"The dragon has {dragon.health} health\n")
         bow_shot_count += 1
         if bow_shot_count % 2 == 0:
            weapon1.bow_damage += weapon1.bow_damage * 0.75
            print(f"Your damage is {weapon1.bow_damage}")

         
      attack_count += 1
      #Dragon level up after two attacks
      if attack_count % 2 == 0:
         if dragon.health <= 0:
            dragon_alive = False
         else:
            dragon.level += 1
            dragon.damage += dragon.damage * 0.5
            dragon.health += dragon.health * 0.2
            print(f"\nThe dragon is level {dragon.level}\n")
      

      #If player attacks 5 times 
      if attack_count % 5 == 0:
         crit_attack = random.randint(100, 250)
         dragon.health -= crit_attack
         print(f"\nYou have landed a critical hit!\n")
         if dragon.health <= 0:
            print("You have defeated the dragon!")
            break
         else:
            dragon.health = round(dragon.health, 2)
            print(f"The dragon has {dragon.health} health\n")


      #Dragon attacks player after two attacks
      dragon_attack_count += 1
      if dragon_attack_count % 2 == 0:
         if dragon.health <= 0:
            print("You have defeated the dragon!")
            break
         else:
            print("While attacking the dragon you also got attacked!\n")
            player1.health -= dragon.damage
            player1.health = round(player1.health, 2)
            dragon.health = round(dragon.health, 2)
            print(f"The dragon has {dragon.health} health")
            print(f"You have {player1.health} health\n")


      #Player level up after two attacks
      player1.level += 1
      if player1.level % 2 == 0:
         print(f"You leveled up! Your new level is {player1.level}")
         player1.health += player1.health * 0.1
         player1.health = round(player1.health, 2)
         print(f"Your health is {player1.health}\n")


    #Check players health, damage and level and dragon health
   if user_input == "check":
      check()


    #Players potion health
   if user_input == "heal":
      heal()
         

   #Players strength potion to increase overall damage
   if user_input == "strength":
      strength()


   #allows a player to break the while statement therefore ending the game
   if user_input == "exit":
      break


   #Game ends if a player has no health remaining
   if player1.health <= 0:
      print("You have died")
      break


   if user_input == "farm":
      farm()

      #append strength to player items
