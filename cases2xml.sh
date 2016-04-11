mkdir -p $3
for f in $2;
do
	g++ -fprofile-arcs -ftest-coverage $1
	./a.out < $f > log/gcovr_consol_output.log
	gcovr -r . --xml > "xml/$(basename $f).xml"
	mv -t log/ a.out *.gc*
done

