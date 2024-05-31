cubed_palindrome_num = []

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def main():
    for i in range(1, 10**6):
        if is_palindrome(i**3):
            cubed_palindrome_num.append(i**3)
            
    N = int(input())
    for c in cubed_palindrome_num[::-1]:
        if c <= N:
            print(c)
            break

if __name__ == '__main__':
    main()