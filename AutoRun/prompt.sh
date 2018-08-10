#!/bin/bash

function prompt()
{
	echo "<Menu>"
	echo "1) Detector"
	echo "2) Exit"
	echo "3) ShutDown"

	Keypress=3

	read -t 15 Keypress

	case "$Keypress" in
	1) return 1;;
	2) return 2;;
	3) return 3;;
	"") return 3;;
	esac

	return 0
}

prompt

RETURN="$?"
sleep 5

case "$RETURN" in
1) ./Detector.sh;;
2) exit 0;;
3)
echo "Will be Shutdown in 5s"
sleep 5 
shutdown now;;
0) exit 0;;
esac

