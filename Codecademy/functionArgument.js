const addTwo = (num) => {
  return num + 2;
};

const checkConsistentOutput = (func, val) => {
  const checkA = val + 2;
  const checkB = func(val);
  if (checkA === checkB) {
    return checkB;
  } else {
    return "inconsistent results";
  }
};

console.log(checkConsistentOutput(addTwo, 2));
