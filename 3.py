def count_occurrences(INPUT, QUERY):
    result = []
    input_counts = {word: INPUT.count(word) for word in set(INPUT)}
    
    for word in QUERY:
        result.append(input_counts.get(word, 0)) 
    
    return result

INPUT = ['xc', 'dz', 'bbb', 'dz']
QUERY = ['bbb', 'ac', 'dz']

output = count_occurrences(INPUT, QUERY)
print(output)
