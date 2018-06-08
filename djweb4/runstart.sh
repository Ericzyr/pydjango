#!/bin/bash

fun1(){
#for((i=0;i<1;i++))
#do
`python3 manage.py runserver` 2>&1>/dev/null
#sleep 1
#done
}

fun2(){
sleep 5
`python3 start.py` 2>&1>/dev/null
sleep 1
}

fun3(){
sleep 10
pig=`netstat -tunlp|grep :8000|awk -F'[ :]+' '{print $9}'|sed 's/\/python.*//g'`
`netstat -tunlp|grep :8000|kill $pig` 2>&1>/dev/null
}

fun1 &
fun2 &
fun3 &
wait

