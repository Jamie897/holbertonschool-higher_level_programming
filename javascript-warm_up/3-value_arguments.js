#!/usr/bin/node
/* Write a script that prints the first argument passed to it:
    If no arguments are passed to the script, print “No argument”
    You must use console.log(...) to print all output
    You are not allowed to use var
    You are not allowed to use length */

// get the first arg passed to the script and print the arg
// start at argv[2]: exec argv[0] and filename argv[1]:(node file.js)
const arg = process.argv[2];

if (arg) {
  console.log(arg);
} else {
  console.log('No argument');
}