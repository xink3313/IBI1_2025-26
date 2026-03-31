# Practical 7: Open Reading Frames (ORF)

# The given mRNA sequence
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

# Define the start codon and a list of stop codons
start_codon = 'AUG'
stop_codons = ['UAA', 'UAG', 'UGA']

# Variable to keep track of the longest ORF found so far
longest_orf = ""

# Iterate through the sequence to find all potential start codons
# len(seq) - 2 ensures there are at least 3 characters left to form a valid codon
for i in range(len(seq) - 2):
    
    # Check if the current 3 nucleotides match the start codon ('AUG')
    if seq[i:i+3] == start_codon:
        
        # Once a start codon is found, look for an in-frame stop codon (steps of 3)
        for j in range(i + 3, len(seq) - 2, 3):
            codon = seq[j:j+3]
            
            # Check if the current in-frame codon is one of the stop codons
            if codon in stop_codons:
                
                # Extract the complete ORF string including start and stop codons
                current_orf = seq[i:j+3]
                
                # Update longest_orf if the newly found ORF is strictly longer
                if len(current_orf) > len(longest_orf):
                    longest_orf = current_orf
                
                # Break the inner loop because translation stops at the FIRST in-frame stop codon
                break 

# Print the final results as required by the assessment guidelines
print(f"The longest ORF is: {longest_orf}")
print(f"The length of the longest ORF is: {len(longest_orf)} nucleotides")