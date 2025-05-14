# Genome-Reconstruction-from-Eulerian-Path

# Description
This Python script reconstructs a genome sequence from a given Eulerian path of (k,d)-mers. By combining overlapping k-mers from paired reads, it rebuilds the original genome sequence.

# Usage
Example
```

def reconstruct_genome(eulerian_path):
    k = len(eulerian_path[0]) // 2  # Determine k from the length of the first (k,d)-mer
    genome = eulerian_path[0][:k - 1]  # Initialize the genome with the first k-1 symbols

    for kmer in eulerian_path:
        genome += kmer[k - 1:]  # Add the last symbol of each (k,d)-mer to the genome

    return genome

# Given Eulerian path
eulerian_path = ["AG|AG", "GC|GC", "CA|CT", "AG|TG", "GC|GC", "CT|CT", "TG|TG", "GC|GC", "CT|CA"]

# Reconstruct the genome
reconstructed_genome = reconstruct_genome(eulerian_path)

# Print the result
print("Reconstructed Genome:", reconstructed_genome)
```
Output

Reconstructed Genome: AG|AGC|GCA|CTG|TGC|GCT|CTG|TGC|GCT|CA

# Function Descriptions
* reconstruct_genome(eulerian_path): Takes a list of (k,d)-mers from an Eulerian path and reconstructs the original genome sequence by overlapping k-mers.

# Applications
* Genome assembly from paired-end sequencing data.
* Bioinformatics education for sequence reconstruction techniques.
* Supporting steps in De Bruijn graph-based genome assembly pipelines.

# License
This project is licensed under the MIT License.










