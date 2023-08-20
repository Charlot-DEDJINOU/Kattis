def flatten(matrix):
    return [number for row in matrix for number in row]

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def reverse(matrix):
    return list(map(lambda row: row[::-1], matrix))

def merge_left(matrix):
    def merge_and_shift_left(row):
        current_index = 0
        while current_index < len(row) and row[current_index] == 0:
            current_index += 1
        next_index = current_index + 1
        while next_index < len(row) and row[next_index] == 0:
            next_index += 1
        
        if next_index == len(row):
            row[0] = row[current_index]
            if current_index != 0:
                row[current_index] = 0
            return row
        elif current_index == len(row):
            return row
        else:
            if row[current_index] == row[next_index]:
                row[current_index] *= 2
                row[next_index] = 0
                t = row[current_index]
                next_merge = merge_and_shift_left(row[next_index+1:] + [0] * next_index)
                return [t] + next_merge
            else:
                if current_index != next_index - 1:
                    row[current_index+1] = row[next_index]
                    row[next_index] = 0
                    next_index = current_index + 1
                t = row[current_index]
                next_merge = merge_and_shift_left(row[next_index:] + [0] * (current_index))
                return [t] + next_merge
    
    new_matrix = []
    for row in matrix:
        elements = [element for element in row]
        result = merge_and_shift_left(elements)
        new_matrix.append(result)
    
    return new_matrix

def merge_right(matrix):
    merged_state = merge_left(reverse(matrix))
    return reverse(merged_state)

def merge_up(matrix):
    merged_state = merge_left(transpose(matrix))
    return transpose(merged_state)

def merge_down(matrix):
    merged_state = merge_right(transpose(matrix))
    return transpose(merged_state)

# Main function
game_matrix = []
for _ in range(4):
    game_matrix.append(list(map(int, input().split())))
move_direction = int(input())

if move_direction == 0:
    for row in merge_left(game_matrix):
        print(" ".join(list(map(str, row))))
elif move_direction == 1:
    for row in merge_up(game_matrix):
        print(" ".join(list(map(str, row))))
elif move_direction == 2:
    for row in merge_right(game_matrix):
        print(" ".join(list(map(str, row))))
else:
    for row in merge_down(game_matrix):
        print(" ".join(list(map(str, row))))