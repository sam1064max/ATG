#!/bin/bash
for f in test/*;
do
	g++ -fprofile-arcs -ftest-coverage $1
	./a.out < $f
	gcovr -r . --xml-pretty > "xml/$f.xml"
	rm -fr a.out model.gcda model.gcno
done
