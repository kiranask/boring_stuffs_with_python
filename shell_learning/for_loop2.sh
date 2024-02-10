FILE='text.txt'
for name in $(cat $FILE)
do
  echo $name
done