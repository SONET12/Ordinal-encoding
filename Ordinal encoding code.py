# Reads sequence records from a file in FASTA format, iterates through the records, and prints out the sequence and its length for each record

from Bio import SeqIO
import numpy as np
import re
from sklearn.preprocessing import LabelEncoder

def string_to_array(sequence_string):
 sequence_string = sequence_string.lower()
 sequence_string = re.sub('[^actg]', 'n', sequence_string)
 sequence_string = np.array(list(sequence_string))
 return sequence_string

def ordinal_encoder(my_array):
 integer_encoded = Label_Encoder.transform(my_array)
 float_encoded = integer_encoded.astype(float)
 float_encoded[float_encoded == 0] = 0.00
 float_encoded[float_encoded == 1] = 0.25
 float_encoded[float_encoded == 2] = 0.50
 float_encoded[float_encoded == 3] = 0.75
 float_encoded[float_encoded == 4] = 1.00
 return float_encoded

Label_Encoder = LabelEncoder()
Label_Encoder.fit(np.array(['a', 'c', 't', 'g','n']))

with open('encoded_sequence.txt', 'w') as outfile:
    for sequence in SeqIO.parse("file format", "fasta"):
        sequence_string = str(sequence.seq)
        encoded_sequence = ordinal_encoder(string_to_array(sequence_string))
        outfile.write(f'>{sequence.id}\n')
        outfile.write(f'{sequence_string}\n')
        outfile.write(f'{encoded_sequence}\n')
 









 

 