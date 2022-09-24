filename=$1
if [ -z "$filename" ]; then
	echo "Error: Needs filename input as argument"
	exit
fi
pdflatex "$filename"
rm *.aux *.out *.log
