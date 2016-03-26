#!/bin/bash
clang -emit-llvm -g -c $1 -o temp.bc
klee --libc=uclibc --posix-runtime -output-dir=$3 temp.bc

for f in "$3/*";
do
	grep -Eo --text 'program.*[a-zA-Z0-9]+' $f | grep -Eo --text '[a-zA-Z0-9]+$' >  "$4/$(basename $f)"
done


mkdir -p $5
for f in $4;
do
	g++ -fprofile-arcs -ftest-coverage $2
	./a.out < $f > temp
	gcovr -r . --xml > "$5/$(basename $f).xml"
	rm -fr a.out model.gcda model.gcno temp
done

python2.7 Parser.py "$5/*" > output
