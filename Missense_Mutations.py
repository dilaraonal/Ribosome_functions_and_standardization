#QUESTION2

from Ribosome_Function import find_gene_amino_acids, aadict

#The available sequence data was read from the file and brought to the desired format by performing the necessary operations.
seqs = open("seq.txt", "r")
raw_seq = ""
sequence = ""
for line in seqs.readlines():
    raw_seq += line.strip() # Cleaned up by removing spaces at the beginning and end of the string
for i in raw_seq:
    if i.isalpha(): #Numerical expressions were extracted
        sequence += i.upper() #letters were converted to uppercase.
seqs.close() #opened file is closed
point_mutation = "r.53G>C"

#define a function to find mutation is missense or not
def missense_mutation (sequence,aadict,point_mutation):
    pre_mutation = find_gene_amino_acids(sequence,aadict) #The function prepared in question 1 is called
    #The function output included the amino acid sequence and the gene found and these outputs were thrown into variables.
    aa_sequence = pre_mutation[0]
    gene = pre_mutation[1]
    #The numerical expression(position information) in the given point mutation was obtained
    numbers = ''.join(filter(str.isdigit, point_mutation))
    position = int(numbers)
    
    
    mut_base = point_mutation[-1] #The base that will replace the existing base according to the information given in the mutation
    #Reaching the desired position and changing it easily has been converted into a list.
    l_gene = list(gene) 
    l_gene[position-1] = mut_base #Since the index starts at 0, 1 was added to reach the desired position.
    mutated_sequence =''.join(map(str,l_gene)) #The sequence with the mutation was obtained
    mut_aa = [aadict[mutated_sequence[a:a+3]] for a in range(0, len(mutated_sequence), 3)] #amino acid sequence of the mutated sequence was extracted
    
    
    # Mutation information was provided in the desired format
    ORF = int(position/3) # Since 3 bases represent one amino acid, the position was divided into 3 to reach the amino acid.
    print("Mutation Information:")
    print(f"r.{position}{gene[position-1]}>{mutated_sequence[position-1]}")
    
    #If the mutation made a change in the amino acid sequence, this was stated, but if there was no change, it was described as a missense mutation.
    if aa_sequence[ORF] != mut_aa[ORF]: 
        print(f"p.{aa_sequence[ORF]}{ORF+1}{mut_aa[ORF]}")
    else:
        print("Missense Mutation")
    
missense_mutation(sequence, aadict, point_mutation)