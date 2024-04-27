W, B = str(input()), str(input())

pattern = "wbwbwwbwbwbw"
W_in_pattern = pattern.count("w")
B_in_pattern = pattern.count("b")

circle_needed = max(W // W_in_pattern, B // B_in_pattern)

extented_pattern = (pattern * circle_needed)[:W + B]
