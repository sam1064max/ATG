#!/bin/bash
g++ -fprofile-arcs -ftest-coverage $1
./a.out < $2
gcovr -r . 
gcovr -r . --branches
rm -fr a.out model.gcda model.gcno
