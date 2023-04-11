#!/usr/bin/node

function argMes() {
	let i = -2;
	for (const arg of process.argv) {
		i = i + 1;
	}
	if (i === 0) {
		console.log('No argument');
	} else if (i === 1) {
		console.log('Argument found');
	} else {
		console.log('Arguments found');
	}
}

argMes();
