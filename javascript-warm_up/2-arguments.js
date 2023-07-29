#!/usr/bin/node
/* Write a script that prints a message depending
of the number of arguments passed: */

// get the num of args passed to the script
// subtract first two: exec and filename(node file.js)
const numArgs = process.argv.length - 2;

// check num of args and pass message

if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}