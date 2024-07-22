up = {123: [1, 'boxer', 1, 'dog', 'ekm'], 223: [2, 'kitty', 2, 'cat', 'ekm']}

def print_others(up, skip_key):
    for key,values in up.items():
        if key == skip_key:
            continue
        # print(f" {key} :{value}")
        print()
        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("userphone", "pet id", "pet name", "age", "type", "place"))
        print('_' * 75)
        user_pets = up[key]
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(key, user_pets[0], user_pets[1], user_pets[2], user_pets[3], user_pets[4]))
        print()

# Example usage
skip_key = 123
print_others(up, skip_key)