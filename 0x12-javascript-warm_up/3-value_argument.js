#!/usr/bin/node

const getLength = (argv) => {
  let i = 0;
  for (let _ of argv) {
    _ = _ + '';
    i++;
  }
  return i;
};
const len = getLength(process.argv);
if (len <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
