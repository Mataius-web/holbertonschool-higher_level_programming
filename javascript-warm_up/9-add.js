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
