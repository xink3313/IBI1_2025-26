# Practical 7: Stop Codon Usage

input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"
stop_codons = ["TAA", "TAG", "TGA"]

# Dictionary to store the fasta sequences: {'>GeneName': 'SEQUENCE'}
sequences = {}
current_gene = ""

print("Reading the FASTA file. This might take a few seconds...")

# 1. Read the fasta file and concatenate multi-line sequences
with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            # Extract only the gene name (the first word after '>')
            current_gene = line.split()[0] 
            sequences[current_gene] = ""
        else:
            # Add sequence data to the current gene
            sequences[current_gene] += line

print("Processing genes to find in-frame stop codons...")

# 2. Process sequences and write to the output file
with open(output_file, "w") as out_f:
    for gene, seq in sequences.items():
        found_stops = set() # Using a set to avoid duplicate stop codons
        
        # Search for the start codon 'ATG'
        for i in range(len(seq) - 2):
            if seq[i:i+3] == "ATG":
                # Check all in-frame codons after 'ATG'
                for j in range(i + 3, len(seq) - 2, 3):
                    codon = seq[j:j+3]
                    if codon in stop_codons:
                        found_stops.add(codon)
                        break # Stop translation after the first in-frame stop codon
        
        # 3. If the gene has at least one in-frame stop codon, write it to the new file
        if found_stops:
            # Format the found stop codons as a comma-separated string
            stops_str = ", ".join(sorted(list(found_stops)))
            
            # Write the new header containing only gene name and stop codons
            out_f.write(f"{gene}; {stops_str}\n")
            
            # Write the actual gene sequence
            out_f.write(seq + "\n")

print(f"Done! Results have been saved to '{output_file}'.")