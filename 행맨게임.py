import sys
import random as r
import time

def hard():
    inplst = []
    c_word = r.choice(words)
    count = 0
    cor = 0 # 맞춘 알파벳 개수
    t = 10
    print("\nSTART!!!\n")
    print("기회는 총 {}번\n".format(t))
    time.sleep(1) # 게임 실행 속도를 조절하기 위해 사용
    while count <= t:
        
        print("\n단어: ",end="")
        s = True
        for i in c_word:
            if i in inplst:
                print(i,end=" ")
            else:
                print("_",end=" ")
                s = False
        time.sleep(1)
        if s == True: # 남은 기회가 있는데 알파벳을 전부 맞추었으면 탈줄
                print("\n\n알파벳을 모두 맞췄습니다 !@@! 축하해요~\n")
                break
        if t-count != 0:
            print("\n\n남은 기회는 {}번 !!".format(t-count))
            time.sleep(0.5)
            if t-count == 3:
                if (t-count) != (len(c_word)-cor):
                    print("신중히 고르세요! 남은 기회가 많지 않아요")
                    time.sleep(0.5)
        if (len(c_word)-cor) != 0: # 알파벳을 다 맞췄으면 맞춰야 할 알파벳 수를 알려주는 것은 불필요
            print("맞춰야 할 알파벳 수는 {}개!".format(len(c_word)-cor))
            if (len(c_word)-cor) == (t-count):
                time.sleep(1)
                print("한번이라도 틀리면 실패에요... 신중하세요!@!@!@!")
        if t-count == 0: # 기회 소진시 
            if s == True: # 기회를 다 썼는데 알파벳도 다 맞췄으면 축하해주고 탈출
                print("\n\n알파벳을 모두 맞췄습니다 !@@! 축하해요~\n")
            break
        ########
        time.sleep(1)
        # 알파벳 입력 & 잘못된 입력을 받았을 경우
        print("\n어떤 알파벳을 고를건가요? -> ",end="")
        alp = sys.stdin.readline().rstrip()
        print()
        if alp.isdigit(): # True값을 반환하면 숫
            print("흠... 숫자가 아니라 알파벳을 입력하여야합니다ㅏㅏㅏㅏ")
            time.sleep(0.5)
            print("다시 입력하세요\n")
            time.sleep(0.5)
            continue # 알파벳이 아니면 밑의 코드들을 실행하지 않는다. -> 카운트가 늘어나지 않는다.
        elif len(alp) > 1:
            print("흠... 하나의 알파벳을 입력하여야합니다ㅏㅏㅏㅏ")
            time.sleep(0.5)
            print("다시 입력하세요\n")
            time.sleep(0.5)
            continue
        
        if alp not in c_word:
            print("ㅣㅜ_ㅜㅣ 틀렸어요 ㅠㅠ\n")
        else:
            if alp not in inplst:
                print("\.> _ <./ 정답이에요 @!!@!\n") 
                inplst.append(alp)
                for i in c_word: # 한 단어에 같은 알파벳이 여러개라면 맞춰야 할 알파벳 수도 그만큼 더 줄어든다.
                    if alp == i:
                        cor += 1
            else: # 이미 맞춘 알파벳을 다시 입력한다면
                print("이미 맞춘 알파벳이군요. 다른 알파벳을 입력해주세요.\n")
                print("남은 기회는 {}번!!".format(t-count))
                continue
        count += 1
        #####
        time.sleep(1)
        if (t-count) < (len(c_word)-cor): # 맞춰야 할 알파벳이 남은 기회보다 많아지면 조기종료
            break
        if (len(c_word)-cor) == 0: # 알파벳을 다 맞춰 더이상 맞출 알파벳이 없ㅇ면 아래 문장은 불필요하다.
            continue
    if s == False:
        print("\n정답: {}".format(c_word))
        print("\n아쉽네요 ㅠㅠ 다시 도전해주세요\n")

def normal():
    inplst = []
    c_word = r.choice(words)
    count = 0
    cor = 0 # 맞춘 알파벳 개수
    t = 15
    print("\nSTART!!!\n")
    print("기회는 총 {}번\n".format(t))
    time.sleep(1)
    while count <= t:
        
        print("\n단어: ",end="")
        s = True
        for i in c_word:
            if i in inplst:
                print(i,end=" ")
            else:
                print("_",end=" ")
                s = False
        time.sleep(1)
        if s == True: # 남은 기회가 있는데 알파벳을 전부 맞추었으면 탈줄
                print("\n\n알파벳을 모두 맞췄습니다 !@@! 축하해요~\n")
                break
        if t-count != 0:
            print("\n\n남은 기회는 {}번 !!".format(t-count))
            time.sleep(0.5)
            if t-count == 3:
                if (t-count) != (len(c_word)-cor):
                    print("신중히 고르세요! 남은 기회가 많지 않아요")
                    time.sleep(0.5)
        if (len(c_word)-cor) != 0: # 알파벳을 다 맞췄으면 맞춰야 할 알파벳 수를 알려주는 것은 불필요
            print("맞춰야 할 알파벳 수는 {}개!".format(len(c_word)-cor))
            if (len(c_word)-cor) == (t-count):
                time.sleep(1)
                print("한번이라도 틀리면 실패에요... 신중하세요!@!@!@!")
        if t-count == 0: # 기회 소진시 
            if s == True: # 기회를 다 썼는데 알파벳도 다 맞췄으면 축하해주고 탈출
                print("\n\n알파벳을 모두 맞췄습니다 !@@! 축하해요~\n")
            break
        ########
        time.sleep(1)
        # 알파벳 입력 & 잘못된 입력을 받았을 경우
        print("\n어떤 알파벳을 고를건가요? -> ",end="")
        alp = sys.stdin.readline().rstrip()
        print()
        if alp.isdigit(): # True값을 반환하면 숫
            print("흠... 숫자가 아니라 알파벳을 입력하여야합니다ㅏㅏㅏㅏ")
            time.sleep(0.5)
            print("다시 입력하세요\n")
            time.sleep(0.5)
            continue # 알파벳이 아니면 밑의 코드들을 실행하지 않는다. -> 카운트가 늘어나지 않는다.
        elif len(alp) > 1:
            print("흠... 하나의 알파벳을 입력하여야합니다ㅏㅏㅏㅏ")
            time.sleep(0.5)
            print("다시 입력하세요\n")
            time.sleep(0.5)
            continue
        
        if alp not in c_word:
            print("ㅣㅜ_ㅜㅣ 틀렸어요 ㅠㅠ\n")
        else:
            if alp not in inplst:
                print("\.> _ <./ 정답이에요 @!!@!\n") 
                inplst.append(alp)
                for i in c_word: # 한 단어에 같은 알파벳이 여러개라면 맞춰야 할 알파벳 수도 그만큼 더 줄어든다.
                    if alp == i:
                        cor += 1
            else: # 이미 맞춘 알파벳을 다시 입력한다면
                print("이미 맞춘 알파벳이군요. 다른 알파벳을 입력해주세요.\n")
                print("남은 기회는 {}번!!".format(t-count))
                continue
        count += 1
        #####
        time.sleep(1)
        if (t-count) < (len(c_word)-cor): # 맞춰야 할 알파벳이 남은 기회보다 많아지면 조기종료
            break
        if (len(c_word)-cor) == 0: # 알파벳을 다 맞춰 더이상 맞출 알파벳이 없ㅇ면 아래 문장은 불필요하다.
            continue
    if s == False:
        print("\n아쉽네요 ㅠㅠ 다시 도전해주세요\n")

def easy():
    inplst = []
    c_word = r.choice(words)
    count = 0
    cor = 0 # 맞춘 알파벳 개수
    t = 20
    print("\nSTART!!!\n")
    print("기회는 총 {}번\n".format(t))
    time.sleep(1)
    while count <= t:
        
        print("\n단어: ",end="")
        s = True
        for i in c_word:
            if i in inplst:
                print(i,end=" ")
            else:
                print("_",end=" ")
                s = False
        time.sleep(1)
        if s == True: # 남은 기회가 있는데 알파벳을 전부 맞추었으면 탈줄
                print("\n\n알파벳을 모두 맞췄습니다 !@@! 축하해요~\n")
                break
        if t-count != 0:
            print("\n\n남은 기회는 {}번 !!".format(t-count))
            time.sleep(0.5)
            if t-count == 3:
                if (t-count) != (len(c_word)-cor):
                    print("신중히 고르세요! 남은 기회가 많지 않아요")
                    time.sleep(0.5)
        if (len(c_word)-cor) != 0: # 알파벳을 다 맞췄으면 맞춰야 할 알파벳 수를 알려주는 것은 불필요
            print("맞춰야 할 알파벳 수는 {}개!".format(len(c_word)-cor))
            if (len(c_word)-cor) == (t-count):
                time.sleep(1)
                print("한번이라도 틀리면 실패에요... 신중하세요!@!@!@!")
        if t-count == 0: # 기회 소진시 
            if s == True: # 기회를 다 썼는데 알파벳도 다 맞췄으면 축하해주고 탈출
                print("\n\n알파벳을 모두 맞췄습니다 !@@! 축하해요~\n")
            break
        ########
        time.sleep(1)
        # 알파벳 입력 & 잘못된 입력을 받았을 경우
        print("\n어떤 알파벳을 고를건가요? -> ",end="")
        alp = sys.stdin.readline().rstrip()
        print()
        if alp.isdigit(): # True값을 반환하면 숫
            print("흠... 숫자가 아니라 알파벳을 입력하여야합니다ㅏㅏㅏㅏ")
            time.sleep(0.5)
            print("다시 입력하세요\n")
            time.sleep(0.5)
            continue # 알파벳이 아니면 밑의 코드들을 실행하지 않는다. -> 카운트가 늘어나지 않는다.
        elif len(alp) > 1:
            print("흠... 하나의 알파벳을 입력하여야합니다ㅏㅏㅏㅏ")
            time.sleep(0.5)
            print("다시 입력하세요\n")
            time.sleep(0.5)
            continue
        
        if alp not in c_word:
            print("ㅣㅜ_ㅜㅣ 틀렸어요 ㅠㅠ\n")
        else:
            if alp not in inplst:
                print("\.> _ <./ 정답이에요 @!!@!\n") 
                inplst.append(alp)
                for i in c_word: # 한 단어에 같은 알파벳이 여러개라면 맞춰야 할 알파벳 수도 그만큼 더 줄어든다.
                    if alp == i:
                        cor += 1
            else: # 이미 맞춘 알파벳을 다시 입력한다면
                print("이미 맞춘 알파벳이군요. 다른 알파벳을 입력해주세요.\n")
                print("남은 기회는 {}번!!".format(t-count))
                continue
        count += 1
        #####
        time.sleep(1)
        if (t-count) < (len(c_word)-cor): # 맞춰야 할 알파벳이 남은 기회보다 많아지면 조기종료
            break
        if (len(c_word)-cor) == 0: # 알파벳을 다 맞춰 더이상 맞출 알파벳이 없ㅇ면 아래 문장은 불필요하다.
            continue
    if s == False:
        print("\n아쉽네요 ㅠㅠ 다시 도전해주세요\n")

def main():
    print("난이도를 선택해보세요(쉬움 -> 1, 보통 -> 2, 어려움 -> 3) -> ",end="")
    try:
        diff = int(sys.stdin.readline())
        error = None
    except:
        diff = 0
        error = "valueError" 
    if diff > 3 or diff < 1: # diff 가 1,2,3 이 아닌 숫자 여도 다시 입력, 문자를 입력해도 다시 입력
        while True:
            if error == "valueError": # 문자를 입력했을 때
                print("\n숫자가 아닌 것 같아요 다시 입력해줄래요?\n")
                print("난이도를 선택해보세요(1단계-> 1, 2단계 -> 2, 3단계 -> 3) -> ",end="")
                error = None
            else: # 범위 밖의 숫자를 입력했을 때
                print("\n없는 난이도를 선택했네요. 다시 선택해주세요\n")
                print("난이도를 선택해보세요(1단계-> 1, 2단계 -> 2, 3단계 -> 3) -> ",end="")
            try:
                diff = int(sys.stdin.readline().rstrip())
            except:
                error = "valueError"

            if 1 <= diff <= 3: # 제대로 숫자를 입력 했다해도 없는 난이도를 선택하면 다시 무한반복이 시작된다.
                break
    if diff == 1:
        easy()
    elif diff == 2:
        normal()
    elif diff == 3:
        hard()
 
 # 실행
words = ["octopus","squirrel","kangaroo","gorilla","pineapple","mushroom","picachu"]
main()