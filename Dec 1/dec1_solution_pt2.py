PUZZLE_INPUT = "puzzle_input.txt"

if __name__ == "__main__":
    # Get the puzzle input into python
    with open(PUZZLE_INPUT, "r") as file:
        text = file.readlines()

    current_group = []
    max_sums = [0, 0, 0]
    total_num_lines = len(text)

    for line_num, line in enumerate(text):
        is_eof = line_num == total_num_lines - 1

        # Create a new group if newline
        if line == "\n" or is_eof:
            if is_eof:
                # No newline on the last line
                current_group.append(int(line))
            current_group_sum = sum(current_group)
            if any([current_group_sum > sum_ for sum_ in max_sums]):
                smallest_index = max_sums.index(min(max_sums))
                max_sums[smallest_index] = current_group_sum
            current_group = []
        else:
            # do not append newline character (it counts as one character)
            current_group.append(int(line[:-1]))

    print(f"The 3 elves with the most calories are carrying {sum(max_sums)} total")

