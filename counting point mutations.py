strand1 = 'CAATACATTTAGTTATAATTTCTTTTCCTACCAGTTCCTCGCACTCCCTCGAACCGCTTCCTCGAGGCGCCTTGTTGCAGCGGAAAGCCATCAGCTTGCGGTTAAATGCCATGTTATCCTCTGCATATAAAATGTATGCACCTCACTTGGACATCCCCTCGCCGAAAATCGTTGACATCTCGTTATCGGACTACAAGTCATTTATGGGGCTGAGCGGCTCCCTCCCTTGGACCCTTTGGGGTCCGCTTCCGTGGTGCAAGCTTCTTCGCTGCATATCCTGACACCGCCGTGCTGGATATGCTAGTAAGGCCCACAGAATACCTGTTCTATTCCGCCCTCAAGCTTGTTTCCCCCAAATGATACCGGCCATTAATACCCTATCAAGCACTGATTGTCCAGGGCTTTTGTGGGCTCAGATCTGCCCAGGAACGAGTAGGAACAGCACCCGGAATTACTTCTTTGGGATTATGGGTGTGTTATCTCGACGTTGTTGATGTCGTCCACTTCCGGTACCTGCTCGTGGCTTAGGCTGAAGGGGACACCTCCAAGAACACGCCCTGGGCCAGGGACAAGAATTTTACTGAGACTGTGACATAGGCCGGCCTTAGAGTATTTCGCTGACCGGTAGTGATTATGCTGCGGCCGTTCTAAAATGTGGTTCTTCGGAATCAGTAGAGCGGGGTACCCTACTGTAGCACCGCAAATTGAATTATCTTAAAGAGCCACTACGCCCGAGGCGGCCGCTGTGATCTGCGCGTCGGTCATTGCTGGTGCACTTATGTGAGAAGAAGGTTGTAACGGGTCGATATCGCACGGCAAATTAGCCATCGCCGCATTTTCACGAGGAGTAAAAACGAACATTTTATACAAGCCGGAATGTAATGAACGACCTCGCGGTGTAGTGGCAGAGAATGT'
strand2 = 'CAAGTTAGGTATGGATATCTCCCTACCCTACTGCTCCGAGGTTGTCCCGTAAACTGGTATCGCGATTAGTTTGCTTGCATCGCTAAGCGGTAGGCGTGCTCCGTTTTTCAATTAAAAATAATATATTTGAAGCGAACGGCGCTCAATGGGCTCTCGGCTACGCGGCTCTGTCTTTCTGGCCGTGAGAAGATCTCGCGTCAAGATCGGTCAGGATTGCCTCACACCCTTTGCTTGGTAATAAGCCCGTTCCAAATGTAACTGTGTATCTGGGACAAGCGAGACCGGCGAGTTGTGCGGCGTATAGTAGGTCCTAGGGAAAACATGAGTGTTTCCGCCCACCAACCTGGTCCTCCGTATTCATCTGTTTAATTAACTTTTTAAACACGAGTATGTATGGTGGGATTTTGTCCGCGCCACTCAGTTGAACAACGAGCAGTGTCGCATTACGAGTTAACCTCTTTGACCTACTGGTAGTATAATGCCTGAAAAGTCTTTGGGGGTAGCTGCTCTTTGCAGCGCGGGGTTTCATCCGCTAACACTATAACAGAACACTGGCCGACTGCCAGTGTCATAATTTTTTCTGTGACCTCGTCAGCTTCGCGATTCAGGTTATTTCATTGGCGGGTACCTAGTATGCGGCGGCCTGTCAGAACTGATTTTGAACTCCCGGAGTGGAGGGCGCCTCTCTAGAAGGCCCACTTACATACATTCAGATCGAGATACGTGAACCCCGGAAACGGGAATTGTGATATTCCCGTCGGCTATTGCCTGCGTTCCTGTGACAGATACAAAAACGGATGTATCGAGGGCCAGCGACGAATTAAACGTCTGGAGAAGTGCAAGTATTAGGGATTCCTACGCTTCGGCATGGTCTCTAGGTAATGCCTCTCTGTGACCTGCAGTCGCGGTGACTTG'

def mut_count(strand1, strand2):
    count = 0
    i = 0
    for nucleotides in range(len(strand1)):
        if strand1[nucleotides] != strand2[i]:
            count += 1
        i += 1
    return count

print(mut_count(strand1, strand2))