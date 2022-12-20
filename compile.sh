filename=$1
if [ -z "$filename" ]; then
	echo "Error: Needs filename input as argument"
	exit
fi
pdflatex -shell-escape "$filename"
rm *.aux *.out *.log
