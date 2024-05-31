def find_majority(S):
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if(S[i] == S[j]):
                # print("マジョリティーは", S[i])
                return S[i]
            
def main():
    S = input()
    S = list(S)
    majority = find_majority(S)
    for i in range(len(S)):
        if(S[i] != majority):
            print(i+1)
            exit()
    
if __name__ == '__main__':
    main()