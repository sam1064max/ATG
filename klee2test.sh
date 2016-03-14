#!/bin/bash
mkdir -p $2
for f in $1;
do
	grep -Eo --text 'program.*[a-zA-Z0-9]+' $f | grep -Eo --text '[a-zA-Z0-9]+$' >  "$2/$(basename $f)"
done