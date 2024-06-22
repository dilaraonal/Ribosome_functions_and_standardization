#QUESTION3

# Import the NumPy library with the name 'np'
import numpy as np
# Define a function to standardize expression values
def standardize_expression(expression_values):
    # Calculate the mean and standard deviation of the expression values 
    mean_values = np.mean(expression_values)
    std = np.std(expression_values)
    
    #Standardize the expression values based on the calculated mean and standard deviation
    standardized_values = [(i - mean_values) / std for i in expression_values]
    return standardized_values


# Define a function to read_gene_expression_data from a file_path
def read_gene_expression_file():
    # Create an empty list to store gene expression data
    gene_expression = []
    # Open the file in read mode
    expression_file = open("gene_expression.txt","r")
    
    # Read the header line of the file, strip the spaces in the line and split the characters in the line.
    header = expression_file.readline().strip().split('\t')
    # Repeat the same for remaining lines in the file
    for line in expression_file:
        splited_data = line.strip().split('\t')
        gene_names = splited_data[0]# Extract the gene name from the first column   
        # Convert the remaining parts to the list of floating-point numbers representing gene expression values
        expression_values = list(map(float, splited_data[1:]))
        # Append a tuple containing gene name, expression values, and header to the gene_expression list
        gene_expression.append((gene_names, expression_values, header[1:]))  
    
    expression_file.close()
    return gene_expression


# Define a function to write standardized gene expression data to a file 
def write_standardized_expression_file(standardized_data):
   # Open the file in write mode
    std_gene_expression = open("std_gene_expression.txt", "w")
    # A header line containing the gene name and standardized sample values is created in the file.
    std_gene_expression.write('\t'.join(["Gene"] + ['\t' + i for i in standardized_data[0][2]]) + '\n')
    # The name of each gene and the standardized gene expression values are combined and written to the file
    for gene_names, gene_values, _ in standardized_data:
        #The function made at the beginning was called and used on the obtained gene values
        standardized_values = standardize_expression(gene_values)
        std_gene_expression.write('\t'.join([gene_names] + list(map(str, standardized_values))) + '\n')
    std_gene_expression.close()


# Read the gene expression datas from input_file_path and keeps it in gene_expression_data list
gene_expression_data = read_gene_expression_file()


# Standardize and write the data to the output file
write_standardized_expression_file(gene_expression_data)


