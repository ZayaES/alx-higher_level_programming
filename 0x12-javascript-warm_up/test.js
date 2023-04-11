#!/usr/bin/node


console.log(process.argv[2]);
function numOfArg(){
	let i = 0;
	for (arg of process.argv) {
		i = i + 1;
	}
	return i;
}

const numArgs = numOfArg() - 2
console.log(numArgs)
