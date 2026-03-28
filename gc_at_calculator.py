def calculate_gc_at(sequence):
    
    sequence = sequence.upper()
    

    total_length = len(sequence)
    

    g_count = sequence.count('G')
    c_count = sequence.count('C')
    a_count = sequence.count('A')
    t_count = sequence.count('T')

    gc_content = ((g_count + c_count) / total_length) * 100
    at_content = ((a_count + t_count) / total_length) * 100
    
    return gc_content, at_content

dna_sequence = input("Enter DNA sequence: ")


gc, at = calculate_gc_at(dna_sequence)


print(f"GC Content: {gc:.2f}%")
print(f"AT Content: {at:.2f}%")
