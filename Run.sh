#!/bin/bash
clang -emit-llvm -g -c $1 -o temp.bc
klee --libc=uclibc --posix-runtime temp.bc > temp
rm -fr temp temp.bc

./klee2test.sh "klee-out-0/*.ktest" "cases"

./cases2xml.sh $2 "cases/*" "xml"

python3 Reducer.py "xml/*" > output

#rm -fr output klee-last klee-out-* xml/ cases/
