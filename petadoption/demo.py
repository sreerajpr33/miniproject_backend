my_dict = {}

# Check if the dictionary is empty
if not my_dict:
    # Add key '1' with a list of values
    my_dict['1'] = [123, 456, 789]
    print("Dictionary was empty. Added key '1' with values:", my_dict['1'])
else:
    print("Dictionary is not empty. Current contents:", my_dict)

# Print the final state of the dictionary
print("Final dictionary:", my_dict)