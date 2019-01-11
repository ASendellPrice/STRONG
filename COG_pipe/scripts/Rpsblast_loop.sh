#!/bin/bash
# just a small script to run rpsblast on parralell on all ".faa" file of a folder, used for embarassingly trivial paralelisation.

TEMP_FOLDER=$1
THREAD_CNT=$2
DB=$3

function launch_rpsblast {
    file=$1
    base=${file%.faa}
    DB=$2
    Output=$base"_Rpsblast.tsv"
    rpsblast+ -outfmt '6 qseqid sseqid evalue pident length slen qlen' -evalue 0.00001 -query $file -db $DB -out $Output
    return 0
}


List_files=$( ls $TEMP_FOLDER/*.faa )

export -f launch_rpsblast
echo $List_files | tr -s " " "\n" | xargs -n 1 -P $THREAD_CNT -I {} bash -c 'launch_rpsblast "$@"' _ {} $DB


cat $TEMP_FOLDER/*_Rpsblast.tsv > $TEMP_FOLDER/Complete_Rpsblast_cogs.tsv







