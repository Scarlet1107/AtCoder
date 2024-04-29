Score_A = list(map(int, input().split()))
Score_B = list(map(int, input().split()))


needed_Score = sum(Score_A) - sum(Score_B) + 1
print(needed_Score)