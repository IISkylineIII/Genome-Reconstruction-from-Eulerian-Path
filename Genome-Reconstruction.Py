def reconstruct_genome(eulerian_path):
    k = len(eulerian_path[0]) // 2  # Determine k from the length of the first (k,d)-mer
    genome = eulerian_path[0][:k - 1]  # Initialize the genome with the first k-1 symbols

    for kmer in eulerian_path:
        genome += kmer[k - 1:]  # Add the last symbol of each (k,d)-mer to the genome

    return genome

eulerian_path = ["AG|AG", "GC|GC", "CA|CT", "AG|TG", "GC|GC", "CT|CT", "TG|TG", "GC|GC", "CT|CA"]

reconstructed_genome = reconstruct_genome(eulerian_path)

print("Reconstructed Genome:", reconstructed_genome)
