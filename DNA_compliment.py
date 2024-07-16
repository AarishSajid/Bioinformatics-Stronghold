dna = open('rosalind/data.txt').read()
#opening dataset given by rosalind
compliment = ''
#empty string to append changed nucleotides onto

for nucleotide in dna[::-1]:
#for loop running in reverse 
    if nucleotide == 'A':
        nucleotide = 'T'
    elif nucleotide == 'T':
        nucleotide = 'A'
    elif nucleotide == 'C':
        nucleotide = 'G'
    elif nucleotide == 'G':
        nucleotide = 'C'
#changes to nucleotides 
    compliment += nucleotide
#apppend to string 

print(compliment)
#and ur done
    
