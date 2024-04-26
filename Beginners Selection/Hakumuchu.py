def main():
    S = str(input())
    
    while(len(S) >= 0):
        if(S == ""):
            print("YES")
            return
        if(S[0:7] == "dreamer" and S[7:9] != "as"):
            S = S[7:]
            # print("S: ", S)
        elif(S[0:6] == "eraser"):
            S = S[6:]
            # print("S: ", S)
        elif(S[0:5] == "dream" or S[0:5] == "erase"):
            S = S[5:]
            # print("S: ", S)
        else: 
            print("NO")
            return
       
    
    
    
if __name__ == '__main__':
    main()