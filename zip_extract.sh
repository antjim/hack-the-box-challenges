#!/bin/bash

index=0
param=$1

unzip_all(){
	zipfile="$1"
	let "index++"
	echo $index

	next_zip="$(unzip -Z1 "$zipfile" | head -n1)"
	if echo "$next_zip" | grep "\.zip"; then
		unzip -P "${next_zip%%.*}" "$zipfile"
		rm -r "$zipfile"
		unzip_all "$next_zip"
	fi
}

unzip_all $param