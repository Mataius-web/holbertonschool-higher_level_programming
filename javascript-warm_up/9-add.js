#!/usr/bin/node


function add(a, b) {
  const firstNumber = parseInt(a);
  const secNumber = parseInt(b);
  if (isNaN(firstNumber) || isNaN(secNumber)) {
    console.log('NaN');
  } else {
    console.log(firstNumber + secNumber);
  }
}

add(parseInt(process.argv[2]), parseInt(process.argv[3]));