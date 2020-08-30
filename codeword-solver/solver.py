import itertools

blank = "■"
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
known = {}
board = []
words = []
unknown = []
min_length = 3
max_length = 7
board_num = 1
needed_words = 5

def check_row(row):
    rl = len(row)
    word = ""
    for i in range(0, rl):
        letter = row[i]
        if letter == blank:
            word = ""
            continue
        word += letter
        if len(word) >= min_length and len(word) <= max_length:
            if i + 1 == rl or (i + 1 < rl and row[i+1] == blank):
                if word in words:
                    return True
    return False

# get all possible words
wordstxt = open("words.txt", "r")
words = wordstxt.readlines()
for i in range(0, len(words)):
    words[i] = words[i][:-1]
wordstxt.close()

# setup board and known alphabet
boardfile = open("board" + str(board_num) + ".txt", "r")
for line in boardfile:
    if known == {}:
        # get known letters and their numbers
        knowns = line.split(",")
        for i in range(0, len(knowns), 2):
            known[knowns[i]] = int(knowns[i + 1])
        continue
    # get row
    row = []
    for i in range(0, len(line), 2):
        num = line[i:i + 2]
        if num[0:1] == "0":
            # single digit, remove first zero
            num = num[1:2]
        elif num == "\n":
            # newline, ignore
            continue
        row.append(int(num))
    board.append(row)
boardfile.close()

# prepare alphabet
for letter in alphabet:
    if letter in known.keys():
        continue
    unknown.append(letter)

# assemble board, check for words, output if vaiable solution
possibles = list(itertools.permutations(unknown))
for i in range(0, len(possibles)):
    # get ordered numbers from all possibilities
    ordered = list(possibles[i])
    # map unknown letters to numbers
    mapped = {}
    ni = 0
    for n in range(1, 27):
        if n in known.values():
            continue
        mapped[ordered[ni]] = n
        ni += 1
    # make board key (finally)
    stitched = {**known, **mapped}
    board_key = {}
    for k, v in stitched.items():
        # make things below easier
        board_key[v] = k
    # fill in board
    solved = []
    for row in board:
        r = []
        for num in row:
            r.append(blank if num == 0 else board_key[num])
        solved.append(r)
    # check for valid words
    matches = 0
    for row in solved:
        # only rows for now
        if check_row(row):
            matches += 1
    # output if enough found
    if matches >= needed_words:
        for row in solved:
            out = ""
            for letter in row:
                out += letter + " "
            print(out)
        print("\n")

# all done
print("Complete")
