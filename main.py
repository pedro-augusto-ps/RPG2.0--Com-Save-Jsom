import funcoes
import time

funcoes.main_menu()
game_load_or_save = int(input("[1] New Game    [2] Load Game \n"))
if game_load_or_save == 2:
    player = funcoes.game_load()
    if player is None:
        player = funcoes.player_function()     #No save? this line creates one
else:
    player = funcoes.player_function()           #No save? this line creates one
        
game_end = True
while game_end:
    monsters = [funcoes.monster1(),funcoes.monster2(),funcoes.monster3()]
    for enemy in monsters:
        print(f"An enemy appeared, HP: {enemy['life']}")

        while True:
            
            print("[1] Attack  [2]Items [3]Shop")

            player_choice = int(input("Choose you action: "))

            if player_choice == 1:
                print("Attack SELECTED")
                enemy['life'] -= player['attack']
            
            elif player_choice == 2:
                print("Itens SELECTED")
                print(f"Your items: {player.get('inventory', 'NONE')}")
                print(f"[1] for Healing Potion")
                print(f"[5] to Leave")
                items_selected = int(input("Which Items you wanna use? "))
                if items_selected == 1:
                    player = funcoes.potion(player)
                    continue
                elif items_selected == 5:
                    continue

            elif player_choice == 3:
                print("Shop SELECTED")
                player = funcoes.shop(player)
                print("-" * 40)
                continue
            else:
                print("You can't do this")

            print("-" * 40)    

            time.sleep(1)

            if enemy['life'] <= 0:
                print("You deffeat this monster, wait...")
                player['gold'] += enemy['gold']
                player['life'] += 10
                print("+10 HP")
                print(f"Player HP:{player['life']}, his GOLD: {player['gold']}")
                print("-" * 40)
                funcoes.game_save(player)
                break
                
            print(f"Enemy turn, his HP: {enemy['life']}")
            player['life'] -= enemy['attack']  
            print(f"Enemy attack, your HP now: {player['life']}")
            print("-" * 40)

            if player['life'] <= 0:
                print("You lost, but you always can GET UP")
                game_end = False
                break

        if enemy == monsters[-1]:
            print("A worthy opponent on path...")