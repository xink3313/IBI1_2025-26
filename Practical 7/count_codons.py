# Practical 7: Codon frequency
import matplotlib.pyplot as plt

input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
valid_stops = ["TAA", "TAG", "TGA"]

# 1. Ask the user for input
target_stop = input("Enter a stop codon (TAA, TAG, or TGA): ").upper()

if target_stop not in valid_stops:
    print("Invalid input. Please run the script again and enter TAA, TAG, or TGA.")
    exit()

# 2. Read the FASTA file
sequences = {}
current_gene = ""
print("Reading sequence data...")
with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            current_gene = line.split()[0]
            sequences[current_gene] = ""
        else:
            sequences[current_gene] += line

codon_counts = {}

print("Analyzing ORFs and counting upstream codons...")
# 3. Find the longest ORF ending with the target stop codon for each gene
for gene, seq in sequences.items():
    longest_orf_codons = []
    
    for i in range(len(seq) - 2):
        if seq[i:i+3] == "ATG":
            current_orf_codons = []
            for j in range(i + 3, len(seq) - 2, 3):
                codon = seq[j:j+3]
                
                # If we hit the target stop codon
                if codon == target_stop:
                    # Update if this ORF is the longest one we've found for this gene
                    if len(current_orf_codons) > len(longest_orf_codons):
                        longest_orf_codons = current_orf_codons
                    break
                # If we hit a DIFFERENT stop codon first, this ORF is invalid for our target
                elif codon in valid_stops:
                    break
                else:
                    # Store the upstream codon
                    current_orf_codons.append(codon)
                    
    # 4. Add the codons from the longest valid ORF of this gene to the global counts
    for c in longest_orf_codons:
        if c in codon_counts:
            codon_counts[c] += 1
        else:
            codon_counts[c] = 1

# 5. Generate and save the pie chart
if codon_counts:
    # Sort the codons by frequency in descending order
    sorted_counts = sorted(codon_counts.items(), key=lambda x: x[1], reverse=True)
    
    # To make the pie chart readable, we only label the top 10 codons
    # and group the rest into an 'Others' category.
    top_codons = sorted_counts[:10]
    other_count = sum(item[1] for item in sorted_counts[10:])
    
    labels = [item[0] for item in top_codons]
    sizes = [item[1] for item in top_codons]
    if other_count > 0:
        labels.append("Others")
        sizes.append(other_count)
        
    plt.figure(figsize=(10, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f"Codon Usage Upstream of {target_stop}")
    
    # Save the chart to a file instead of just showing it
    output_image = f"codon_distribution_{target_stop}.png"
    plt.savefig(output_image)
    print(f"Success! The pie chart has been saved as '{output_image}'.")
else:
    print(f"No valid ORFs found ending with {target_stop}.")