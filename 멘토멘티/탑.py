def main():
    # n 입력받기
    n = int(input())

    
    # tops 리스트 초기화 및 값 입력받기
    tops = []

    tops = list(map(int,(input().split())))

    
    flag = True
    A = 0
    B = 0
    ans = [0] * n  # C++에서 vector<int> ans(n)와 같은 역할
    ans[0] = 0

    while flag:
        if A == B:
            B += 1

        # B 증가시켜 tops[A]보다 작거나 같은 값을 찾음
        while B < n and tops[A] > tops[B]:
            B += 1

        # htop과 loc_top 초기화
        htop = tops[A + 1]
        loc_top = A

        # A+1부터 B-1까지 확인하며 가장 큰 값을 찾음
        for i in range(A + 1, B):
            if htop < tops[i]:
                htop = tops[i]
                loc_top = i
            if htop == tops[i]:
                ans[i] = A
            elif tops[i] < htop:
                ans[i] = loc_top

            if i == n - 1:
                flag = False
                break

        A = B
        if A == n:
            break

    # 결과 출력
    for i in range(n):
        print(ans[i], end=" ")

# 메인 함수 실행
if __name__ == "__main__":
    main()