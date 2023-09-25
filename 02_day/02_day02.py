def file_to_list(file_path):
    data_list = []

    with open(file_path, 'r') as file:
        for line in file:
            # Splitting each line by space and stripping to remove any
            # leading/trailing whitespace
            items = line.strip().split()
            if len(items) == 2:  # Check we have 2 items from the split
                data_list.append(tuple(items))

    return data_list


# Convert the file content to a list
rounds = file_to_list('strategy_input.txt')

opponent = "A for Rock, B for Paper, and C for Scissors"
me = "X for Rock, Y for Paper, and Z for Scissors."

win = [
    ('A', 'Y'),
    ('B', 'Z'),
    ('C', 'X'),
]
lost = [
    ('A', 'Z'),
    ('B', 'X'),
    ('C', 'Y'),
]
draw = [
    ('A', 'X'),
    ('B', 'Y'),
    ('C', 'Z'),
]
#  (1 for Rock, 2 for Paper, and 3 for Scissors)
shape_bonus = [('X', 1), ('Y', 2), ('Z', 3)]

score = 0
for game in rounds:
    print(f'Game: {game}')
    print(f'My shape: {game[1]}')
    for points in shape_bonus:
        if game[1] in points:
            score += points[1]
            print(f'My score {score} (+{points[1]} shape bonus)')
    if game in win:
        score += 6
        print(f'Win: {score}')
    if game in draw:
        score += 3
        print(f'Draw: {score}')
    # if game in lost:
    if game in lost:
        print(f'Lost: {score}')

print(score)

# part 2
# X means you need to lose, Y means you need to end the round in a draw,
# and Z means you need to win
