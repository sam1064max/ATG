mkdir -p $3
for f in $2;
do
	g++ -fprofile-arcs -ftest-coverage $1
	./a.out < $f > temp
	gcovr -r . --xml > "xml/$(basename $f).xml"
	rm -fr a.out *.gc* temp
done

