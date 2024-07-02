def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    coin_types = int(lines[0].strip())
    coins = []
    for line in lines[1:-1]:
        value, count = map(int, line.strip().split())
        coins.append((value, count))
    N = int(lines[-1].strip())
    
    return coin_types, coins, N

def calculate_coins(coin_types, coins, N):
    coins.sort(reverse=True, key=lambda x: x[0])
    
    remaining_amount = N
    result = []
    
    for value, count in coins:
        if remaining_amount == 0:
            break
        num_of_coins = min(remaining_amount // value, count)
        result.append((value, num_of_coins))
        remaining_amount -= value * num_of_coins
    
    if remaining_amount > 0:
        print("Cannot make exact change with given coins.")
        return None
    
    return result

def main():
    filename = 'Ex08Q2input.txt'
    coin_types, coins, N = read_input_file(filename)
    
    result = calculate_coins(coin_types, coins, N)
    
    if result:
        print(f"To pay {N} cents, you need the following coins:")
        for value, num in result:
            print(f"{value}-cent coin: {num} piece(s)")
    else:
        print("It's not possible to make the exact payment with the given coins.")

if __name__ == "__main__":
    main()
