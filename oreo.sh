# Count species in data files
for filename in *.txt 
do 
	echo $filename; cut -d , -f2 $filename |grep -v Species | sort | uniq -c
done
