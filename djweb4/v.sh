#!/bin bash
pig=`netstat -tunlp|grep :8000|awk -F'[ :]+' '{print $9}'|sed 's/\/python.*//g'`
`netstat -tunlp|grep :8000|kill $pig` 2>&1>/dev/null
