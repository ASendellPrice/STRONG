#!/usr/bin/env python

import argparse,os
from Bio.SeqIO.FastaIO import SimpleFastaParser
from collections import defaultdict

def  main(fasta_file,bin_composition,set_bins,output):
	if set_bins :
		Dico_contigs_bin={line.rstrip().split(",")[0]:line.rstrip().split(",")[1] for line in open(bin_composition) if line.rstrip().split(",")[1] in set_bins}
	else :
		Dico_contigs_bin={line.rstrip().split(",")[0]:line.rstrip().split(",")[1] for line in open(bin_composition)}
	Dico_bin_Handle={}
	for bins in set(Dico_contigs_bin.values()) :
		Dico_bin_Handle[bins]=open(output+"/Bin_"+bins+"."+fasta_file.split(".")[-1],"w")
	for contig_id,seq in SimpleFastaParser(open(fasta_file)) :
		contig_id2=contig_id.split()[0]
		if contig_id2 in Dico_contigs_bin :
			Dico_bin_Handle[Dico_contigs_bin[contig_id2]].write(">"+contig_id+"\n"+seq+"\n")
	for handle in Dico_bin_Handle.values() :
		handle.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fasta_file", help="fasta file containing sequences binned")  
    parser.add_argument("bin_composition", help="csv file giving bin composition, output of concoct, first column=contig id, second is bin number")
    parser.add_argument("path_output", help="specify the place you want all these bin folder to be put")
    parser.add_argument("-l", nargs='+',help="restrict to a list of specifics bins ")
    args = parser.parse_args()
    fasta_file=args.fasta_file
    bin_composition=args.bin_composition
    path_output=args.path_output
    set_bins=set([])
    if args.l :
        set_bins=set(args.l)
    main(fasta_file,bin_composition,set_bins,path_output)






