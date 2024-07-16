dna = open('rosalind/data.txt').read()
compliment = ''

for nucleotide in dna[::-1]:
    if nucleotide == 'A':
        nucleotide = 'T'
    elif nucleotide == 'T':
        nucleotide = 'A'
    elif nucleotide == 'C':
        nucleotide = 'G'
    elif nucleotide == 'G':
        nucleotide = 'C'
    compliment += nucleotide

print(compliment)
    