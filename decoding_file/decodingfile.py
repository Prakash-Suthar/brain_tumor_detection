def decode(message_file):
    # Read the content of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()
    # Create a dictionary from the lines
    word_dict = {int(line.split()[0]): line.split()[1].strip() for line in lines}
    
    sorted_keys = sorted(word_dict.keys())
    # Create a pyramid and store the last diagonal values
    pyramid = []
    result_last_diagonal = []
    current_index = 0
    for i in range(1, max(sorted_keys) + 1):
        row = []
        
        for j in range(i):
            current_index += 1
            word = word_dict.get(current_index)
            if word is not None:
                row.append(current_index)
        
        if row:
            result_last_diagonal.append(row[-1])
            pyramid.append(row)
    for i in pyramid:
        print(i)
    sentence = []
    for key in result_last_diagonal:
        value = word_dict.get(key)
        if value is not None:
            sentence.append(value)
    decode_string = ' '.join(sentence)
    print(decode_string)
    return decode_string

# Example usage:
message_file_path = r"C:\Users\praka\Downloads\coding_qual_input.txt"
decode_string = decode(message_file_path)
