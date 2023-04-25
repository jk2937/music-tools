echo $(basename "$0") "- Begin."
for file in nitrotracker-songs/*
do
	echo ""
	echo $(basename "$0") "- Executing: python xm_header.py \"$file\""
	echo ""
	python xm_header.py "$file"
done
echo ""
echo $(basename "$0") "- End."
