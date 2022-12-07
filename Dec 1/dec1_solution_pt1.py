PUZZLE_INPUT = "puzzle_input.txt"

if __name__ == "__main__":
    # Get the puzzle input into python
    with open(PUZZLE_INPUT, "r") as file:
        text = file.readlines()

    current_group = []
    max_sum = 0
    total_num_lines = len(text)

    for line_num, line in enumerate(text):
        is_eof = line_num == total_num_lines - 1

        # Create a new group if newline
        if line == "\n" or is_eof:
            if is_eof:
                # No newline on the last line
                current_group.append(int(line))
            current_group_sum = sum(current_group)
            if current_group_sum > max_sum:
                max_sum = current_group_sum
            current_group = []
        else:
            # do not append newline character (it counts as one character)
            current_group.append(int(line[:-1]))

    print(f"The elf with the most calories is carrying {max_sum}")
