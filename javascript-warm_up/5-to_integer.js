#!/usr/bin/node
/* 5. An Integer
Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
    If the argument can’t be converted to an integer, print “Not a number”
    You must use console.log(...) to print all output
    You are not allowed to use var
    You are not allowed to use try/catch
 */

    const checkArg = process.argv[2];

    // Use Number() to check if arg can convert to a number and convert it
    const argToInt = Number(checkArg);
    if (!isNaN(argToInt)) {
      console.log(`My number: ${argToInt}`);
    } else {
      console.log('Not a number');
    }