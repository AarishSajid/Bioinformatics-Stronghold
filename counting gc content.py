from Bio import SeqIO

biggest_seq = None
most_gcc = 0

for given_seqs in SeqIO.parse("result.fasta", "fasta"):
    sequence = str(given_seqs.seq) 
    sequence_id = given_seqs.id
    gc_content = (sequence.count("C") + sequence.count("G")) / len(sequence) * 100
    if gc_content > most_gcc:
        biggest_seq = sequence_id
        most_gcc = gc_content

print(biggest_seq)
print(most_gcc)