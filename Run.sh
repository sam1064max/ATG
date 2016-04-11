#!/usr/bin/env bash 

set -o errexit
set -o pipefail
set -o nounset

TEST_GENERATOR="klee"
PARSER="false"
DELETE="false"

while getopts 'o:p:d:' opt ; do
  case $opt in
    o) TEST_GENERATOR=$OPTARG ;;
    p) PARSER=$OPTARG ;;
	d) DELETE=$OPTARG ;;
  esac
done

if [ $# -lt 2 ]; then
  echo "Usage: $0 [options] klee_code c_code"
  echo "   -o     Use other test-cases generator (def: $TEST_GENERATOR)"
  echo "   -p     Use parser to make c code klee compatible (def: $PARSER)"
  echo "   -d     Delete the temp files after completion (def: $DELETE)"
  exit 1
fi

KLEE_CODE=$1
C_CODE=$2

if [ $TEST_GENERATOR != "klee" ]; then
  echo "$TEST_GENERATOR is currently not available. Please use <klee>"
  exit 1
fi

if [ $PARSER = "true" ]; then
  echo "klee code converter is currently under process. Please convert the code manually."
  exit 1
fi

mkdir -p log
clang -emit-llvm -g -c $KLEE_CODE -o temp.bc
klee --libc=uclibc --posix-runtime temp.bc > consol_output.txt
mv -t log/ consol_output.txt temp.bc

./klee2test.sh "klee-out-0/*.ktest" "cases"

./cases2xml.sh $C_CODE "cases/*" "xml"

python3 Reducer.py "xml/*" > output

cat output

if [ $DELETE = "true" ]; then
  rm -fr cases/ xml/ klee-*
fi

