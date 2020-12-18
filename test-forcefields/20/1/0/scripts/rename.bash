for file in step*;
do
    pairname=$( basename $file | awk -F'.' '{print $3}' )
    echo "${pairname}.txt"
    mv $file "$pairname.txt"
done
