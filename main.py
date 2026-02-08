from life import dead_state, random_state, render, next_board_state, load_pattern, place_pattern
import time
import msvcrt
import copy
import os

if __name__ == "__main__":
    while True:
        os.system("cls")
        print("choose patterns:")
        print("1. Pattern with customize width and height (random alive cell)")
        print("2. Fixed patterns")
        print("3. Quit")

        command = input("input command: ")

        if command == "1":
            os.system("cls")
            try:
                width = int(input("input width of the state: "))
                height = int(input("input height of the state: "))
            except ValueError:
                print("Please input an integer!")

            initial_state = random_state(width, height)
            board = copy.deepcopy(initial_state)

            while True:
                os.system("cls")
                board = next_board_state(board)
                print("Final state:")
                render(board)
                print("press 'SPACE' to stop the loop")
                time.sleep(0.3)

                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    if key == b' ':
                        print("Loop is stopped")
                        break

            while True:
                print("\nInitial state:")
                render(initial_state)
                input("press ENTER to back to main command")
                break

        elif command == "2":
            os.system("cls")
            print("1. pulsar")
            print("2. gospel glider gun")
            print("3. around the world")

            choose = input("Choose pattern: ")
            if choose == "1":

                a_dead_state = dead_state(width=20, height=20)
                pulsar = load_pattern("patterns/pulsar.txt")
                initial_state = place_pattern(a_dead_state, pulsar, start_x=3, start_y=3)
                board = copy.deepcopy(initial_state)

                while True:
                    os.system("cls")
                    board = next_board_state(board)
                    print("Final state:")
                    render(board)

                    print("press 'SPACE' to stop the loop")
                    time.sleep(0.1)

                    if msvcrt.kbhit():
                        key = msvcrt.getch()
                        if key == b' ':
                            print("Loop is stopped")
                            break
                while True:
                    print("\n'Pulsar' Initial state:")
                    render(initial_state)
                    input("press ENTER to back to main command ")
                    break
                
            elif choose == "2":
                
                a_dead_state = dead_state(width=50, height=25)
                gospel_glider_gun = load_pattern("patterns/gosper_glider_gun.txt")
                initial_state = place_pattern(a_dead_state, gospel_glider_gun, start_x=3, start_y=3)
                board = copy.deepcopy(initial_state)

                while True:
                    os.system("cls")
                    board = next_board_state(board)
                    print("Final state:")
                    render(board)

                    print("press 'SPACE' to stop the loop")
                    time.sleep(0.1)

                    if msvcrt.kbhit():
                        key = msvcrt.getch()
                        if key == b' ':
                            print("Loop is stopped")
                            break
                while True:
                    print("\n'Gospel glider gun' Initial state:")
                    render(initial_state)
                    input("press ENTER to back to main command")
                    break
            
            elif choose == "3":
                
                a_dead_state = dead_state(width=80, height=70)
                atw = load_pattern("patterns/ATW.txt")
                initial_state = place_pattern(a_dead_state, atw, start_x=10, start_y=20)
                board = copy.deepcopy(initial_state)

                while True:
                    os.system("cls")
                    board = next_board_state(board)
                    print("Final state:")
                    render(board)

                    print("press 'SPACE' to stop the loop")
                    time.sleep(0.1)

                    if msvcrt.kbhit():
                        key = msvcrt.getch()
                        if key == b' ':
                            print("Loop is stopped")
                            break
                while True:
                    print("\n'Around the world' Initial state:")
                    render(initial_state)
                    input("press ENTER to back to main command")
                    break
        
        elif command == "3":
            print("Goodbye 🖐🏾🖐🏾")
            break

        else:
            print("Invalid command")
                