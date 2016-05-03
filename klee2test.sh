#!/bin/bash
mkdir -p $2
for f in $1;
do
	#ktest-tool --write-ints $f | tail -1 | grep data | cut -d ':' -f 3 | cut -d '\' -f 1 | rev |  cut -d "'" -f 1 | rev | grep -Eo --text '[a-zA-Z0-9]+' > "$2/$(basename $f .ktest)" 
	grep -Eo --text 'program.*[a-zA-Z0-9]+' $f | grep -Eo --text '[a-zA-Z0-9]+$' >  "$2/$(basename $f .ktest)"
done
