import os
# 입출력 파일은 1.txt, 2.txt, 3.txt ..형식으로

#파일 경로
base_folder = os.path.dirname(os.path.abspath(__file__))
Input_folder = os.path.join(base_folder, 'Input')
Output_folder = os.path.join(base_folder, 'Output')

#목록 모두 불러와서 정렬 1.txt , 2.txt ...
Input_files = sorted(os.listdir(Input_folder))
#Output_files = sorted(os.listdir(Output_folder))


# 입력받고 정답 출력 확인
for file in Input_files:
    input_path = os.path.join(Input_folder, file)
    output_path = os.path.join(Output_folder, file)
    with open(input_path,'r') as f:
        a,b,c = map(int,f.read().strip().split())
        print("입력:",a,b,c)
    
    # 답 코드
    money = 0
    if a == b == c:
        money = 10000 + a * 1000
    elif a == b or a == c:
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + b * 100
    else:
        money = max(a, b, c) * 100
    print("내가 푼 출력: ", money)

    with open(output_path,'r') as f:
        a = f.read().strip()
        print("정답출력",a)

    print()