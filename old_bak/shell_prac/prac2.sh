#!/bin/bash

echo "x : "

read x

echo "y : "

read y

u=`expr $x \* $y`

let "v=$x + $y"

echo "x * y = $u"

echo "x + y = $v"
