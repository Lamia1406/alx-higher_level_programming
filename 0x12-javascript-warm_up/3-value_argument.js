#!/usr/bin/node

const getLength = (argv) => {
  let i = 0;
  for (const _ of argv) {
    i++;
  }
  return i;
};
const length = getLength(process.argv);
if (length <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
