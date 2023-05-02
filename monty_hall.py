import random

def monty_hall_game():
    doors = [1, 2, 3]
    car = random.choice(doors)
    first_choice = int(input("문을 선택하세요 (1, 2, 3): "))
    goat_door = random.choice([door for door in doors if door != car and door != first_choice])
    switch_decision = input(f"문 {goat_door}에 염소가 있습니다. 바꾸시겠습니까? (yes, no): ").lower()
    final_choice = [door for door in doors if door != goat_door and door != first_choice][0] if switch_decision == "yes" else first_choice
    print(f"{'축하합니다' if final_choice == car else '안타깝네요'}, 문 {final_choice} 뒤에 {'자동차' if final_choice == car else '염소'}가 있습니다!")

if __name__ == "__main__":
    monty_hall_game()
