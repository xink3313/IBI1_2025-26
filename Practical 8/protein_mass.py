# protein_mass.py
# A script to calculate the total mass of a protein sequence

# 1. Dictionary storing the mass of each amino acid residue based on the provided table
amino_acid_masses = {
    'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05, 'V': 99.07,
    'T': 101.05, 'C': 103.01, 'I': 113.08, 'L': 113.08, 'N': 114.04,
    'D': 115.03, 'Q': 128.06, 'K': 128.09, 'E': 129.04, 'M': 131.04,
    'H': 137.06, 'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
}

# 2. Define the function to predict protein mass
def calculate_protein_mass(sequence):
    total_mass = 0.0
    # Ensure the sequence is uppercase to match the dictionary keys
    sequence = sequence.upper() 

    # Iterate through each amino acid in the sequence
    for aa in sequence:
        if aa in amino_acid_masses:
            total_mass += amino_acid_masses[aa]
        else:
            # Return an error message if an invalid amino acid is found
            return f"Error: '{aa}' is not a valid amino acid symbol."
            
    # The 'return' keyword sends the final calculated mass back
    return total_mass

# 3. Example function calls as required by the assessment
print("--- Protein Mass Predictor Test ---")

# Valid sequence test
sample_seq = "ACDEF"
result = calculate_protein_mass(sample_seq)
print(f"The total mass of sequence '{sample_seq}' is: {result} amu")

# Invalid sequence test (contains 'X' which is not in the table)
invalid_seq = "ACDXG"
error_result = calculate_protein_mass(invalid_seq)
print(error_result)