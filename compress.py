from typing import List
def compress(chars: List[str]) -> int:
    current_char = chars[0]
    count = 0
    read_index = 0
    write_index = 0

    for i in range(len(chars)):
        if chars[read_index] == current_char:
            count += 1
            read_index += 1
        else:
            chars[write_index] = current_char
            write_index += 1
            if count > 1:
                digit_count = str(count)
                for digit in digit_count:
                    chars[write_index] = digit
                    write_index += 1
            current_char = chars[read_index]
            count = 0

    # Handle the last group
    chars[write_index] = current_char
    write_index += 1
    if count > 1:
        digit_count = str(count)
        for digit in digit_count:
            chars[write_index] = digit
            write_index += 1

    return write_index  # Return the new length

# Example usage:
def main():
    chars = ["a", "a", "b", "b", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"]
    result = compress(chars)
    print(result)  # Output: 6
    print(chars[:result])  # Output: ['a', '2', 'b', '2', 'c', '10']

main()
