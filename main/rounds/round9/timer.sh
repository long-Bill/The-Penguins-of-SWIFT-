

i=0

while [ $i -lt 5 ]; do # 2 ten-second intervals in 1 minute
  /root/user.sh & #run your command
  sleep 12
  i=$(( i + 1 ))
done

