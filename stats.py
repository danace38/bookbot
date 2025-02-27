#This function will count occurence of each word from the text file
def get_num_words(input):

    x = input.split()
    count = len(x)
    
    return count

def count_char(text):

    convert_text = text.lower()

    counter = {}

    for i in convert_text:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    return counter  


#Helper function for the sort_count()
def helper(dict):
    char = list(dict.keys())[0]

    return dict[char]


def sort_count(dict):

    result = []

    for char, count in dict.items():
        result.append({char: count})
    
    result.sort(reverse=True, key=helper)
    return result


# Testing code - outside of any function
if __name__ == "__main__":  # This ensures code only runs when file is executed directly
    # Test with a small dictionary
    test_dict = {
        'a': 10,
        'b': 5,
        'c': 15,
        'd': 3
    }
    
    # Call your function
    sorted_list = sort_count(test_dict)
    
    # Print the result to verify
    print(sorted_list)
    # Should output: [{'c': 15}, {'a': 10}, {'b': 5}, {'d': 3}]
