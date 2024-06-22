#QUESTION1

#The file containing the codons was opened and the first line was eliminated and read.
codons = open("codon-aa-list.txt", "r")
aa_temp = codons.readlines()[1:]


#codon list converted to desired format
aa_list = []; counter = 0;
for i in aa_temp:
    aa_list.append(i.split("\t")), #Created a list separated by spaces
    aa_list[counter][1] = aa_list[counter][1].replace("\n","") #Remove \n character from second element of each sublist
    counter +=1
codons.close() # Close the codons file


#codons and the amino acids they return were created in the dictionary data type
aadict={aa_list[i][0]: aa_list[i][1] for i in range(0,len(aa_list))} 


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



#with this function, a gene in the available sequence data was found and the amino acid sequence was obtained using the created amino acid dictionary.
def find_gene_amino_acids(rna_sequence,amino_acid_dict):
    start_codon = 'AUG'
    stop_codon = ['UAG','UAA','UGA']
    gene = ""
    for i in range(len(sequence)):
        if(start_codon==sequence[i:i+len(start_codon)]): #loop was used to find the start codon
            gene_start_position = i
            # Check in increments of 3 starting from the starting position and find the end point
            for j in range(gene_start_position,len(sequence),3): 
                if(sequence[j:j+len(start_codon)] in stop_codon):
                    gene += sequence[i:j+3] #The found gene sequence was assigned to the variable
                    break 
            break
    amino_acids = [aadict[gene[a:a+3]] for a in range(0, len(gene), 3)] #amino acid sequence was obtained
    return amino_acids, gene


result = find_gene_amino_acids(sequence,aadict)
amino_acid_sequence = ''.join(result[0]) #amino acid sequence information

#It was opened to be printed in a new file and the resulting amino acid sequence was printed into this file.
aa_Seq_file = open("aa_sequence.txt", "w")
aa_Seq_file.write(amino_acid_sequence)
aa_Seq_file.close() # close the opened new file
