import random

def monty_hall_game():
    # 문 3개를 표현하는 리스트 생성 (0, 1, 2)
    doors = [0, 1, 2]
    
    # 자동차가 있는 문을 무작위로 선택
    car = random.choice(doors)
    
    # 참가자의 첫 번째 선택을 사용자로부터 입력받음
    first_choice = int(input("문을 선택하세요 (0, 1, 2): "))
    
    # 참가자가 선택하지 않은 문 중에서 자동차가 없는 문(염소가 있는 문)을 선택
    goat_door = random.choice([door for door in doors if door != car and door != first_choice])
    
    # 참가자의 결정을 입력받음
    switch_decision = input(f"문 {goat_door}에 염소가 있습니다. 바꾸시겠습니까? (yes, no): ").lower()
    
    # 참가자가 전략을 바꾸면 염소가 있는 문이 아닌 나머지 문을 선택, 그렇지 않으면 처음 선택한 문을 유지
    final_choice = [door for door in doors if door != goat_door and door != first_choice][0] if switch_decision == "yes" else first_choice
    
    # 최종 선택 결과를 출력
    print(f"{'축하합니다' if final_choice == car else '안타깝네요'}, 문 {final_choice} 뒤에 {'자동차' if final_choice == car else '염소'}가 있습니다!")

if __name__ == "__main__":
    monty_hall_game()
