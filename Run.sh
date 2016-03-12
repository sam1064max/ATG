#!/bin/bash
mkdir -p $3
for f in $2;
do
	g++ -fprofile-arcs -ftest-coverage $1
	./a.out < $f > temp
	gcovr -r . --xml-pretty > "$3/$(basename $f).xml"
	rm -fr a.out model.gcda model.gcno temp
done

python Parser.py "$3/*" > output