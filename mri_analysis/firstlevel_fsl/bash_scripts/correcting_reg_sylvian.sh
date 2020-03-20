#!/bin/bash
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>Feat_correcting_reg_2_log.out 2>&1

cd /Users/qigroup/mnt/sylvian/blast/data/derivatives/fsl/firstlevelanalysis

rlist=$(cat /Users/qigroup/mnt/sylvian/blast/data/derivatives/fsl/firstlevelanalysis/feat_automated_scripts/run.list.txt)
flist=$(cat /Users/qigroup/mnt/sylvian/blast/data/derivatives/fsl/firstlevelanalysis/feat_automated_scripts/child.subject.list.txt)

for run in $rlist
 do
	for subject in $flist;
		do
			cp correcting_reg sub-blastc${subject}/${run}.feat;
			cd sub-blastc${subject}/${run}.feat;
			sh correcting_reg;
			cd /Users/qigroup/mnt/sylvian/blast/data/derivatives/fsl/firstlevelanalysis;
	done
done
