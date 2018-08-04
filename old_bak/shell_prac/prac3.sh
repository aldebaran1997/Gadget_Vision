#!/bin/bash

echo "What is test? : "

read test

if [ "$test" -gt 10 ]; then
	echo "test > 10"
elif [ "$test"  -lt 10 ]; then
	echo "test < 10"
else
	echo "test = 10"
fi

echo "Waht is Answer? : "

read ans

[ "$ans" == "GodSY" ] && echo "Exactly!!"
[ "$ans" == "GodSY" ] || { echo "You are wrong :p"; echo "Try Again"; }


