def calculate_amino_acid_composition(sequence):
    
    sequence = sequence.upper()
    
    
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    
    total_length = len(sequence)
    
    composition = {}
    
    for aa in amino_acids:
        count = sequence.count(aa)
        percentage = (count / total_length) * 100 if total_length > 0 else 0
        composition[aa] = percentage
    
    return composition



protein_sequence = input("Enter protein sequence: ")


result = calculate_amino_acid_composition(protein_sequence)


print("\nAmino Acid Composition (%):")
for aa, percent in result.items():
    print(f"{aa}: {percent:.2f}%")
