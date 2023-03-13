#!/usr/bin/node

const args = process.argv.slice(2, process.argv.length);
const ints = args.map(Number).filter(num => Number.isInteger(num));

if (ints.length < 1) {
  console.log(0);
} else if (ints.length < 2) {
  console.log(1);
} else {
  const secondLargest = ints.sort((a, b) => b - a)[1];
  console.log(secondLargest);
}
