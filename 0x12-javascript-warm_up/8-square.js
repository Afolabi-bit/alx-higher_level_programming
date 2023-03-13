#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (size) {
  let j = 0;
  while (j < size) {
    let mystr = '';
    for (let i = 0; i < size; i++) {
      mystr += 'X';
    }
    console.log(mystr);
    j++;
  }
} else {
  console.log('Missing size');
}
