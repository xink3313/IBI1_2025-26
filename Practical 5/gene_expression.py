import matplotlib.pyplot as plt

gene_data = {
    'TP53':12.4,
    'EGFR':15.1,
    'BRCA1': 8.2,
    'PTEN': 5.3,
    'ESR1': 10.7
}
gene_data['MYC']= 11.6
print("Uodated Gene Dictionary:", gene_data)

genes = list(gene_data.keys())
values = list(gene_data.values())
plt.bar(genes, values)
plt.xlabel('Gene Name')
plt.ylabel('Expression Level')
plt.title('Gene Expression Levels')
plt.show()

gene_of_interest = 'TP53' 

if gene_of_interest in gene_data:
    print(f"Expression level of {gene_of_interest}: {gene_data[gene_of_interest]}") 
else:
    print(f"Error: The gene '{gene_of_interest}' is not in the dataset.") 