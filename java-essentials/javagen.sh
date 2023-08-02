

# script for generating java class scaffolds
# inputs: className dataType attrName1 dataType attrName2 etc...

# outputs: class declaration, class attributes, constructor, main method, instance



# check that there's at least a filename provided else abort
if [ $# -lt 1 ]
then
  echo Incorrect number of arguments. Requires at least 1.
  exit 1
fi


# if a file with the same name exists then abort
filename=$1.java
if [ -e "$filename" ]
then
  echo The file \"$1\" already exists. Process aborted.
  exit 1
fi

# create file
touch $filename

# append class scope
echo public class $1{ >> $filename

for input in "$@"
do
  echo $input
done
