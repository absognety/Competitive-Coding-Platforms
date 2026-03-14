let getSleepHours = (day) => {
  switch (day) {
    case "Monday":
      return 4.9;
      break;
    case "Tuesday":
      return 4.35;
      break;
    case "Wednesday":
      return 4.27;
      break;
    case "Thursday":
      return 5.2;
      break;
    case "Friday":
      return 4.76;
      break;
    case "Saturday":
      return 3.5;
      break;
    case "Sunday":
      return 6.5;
      break;
  }
};

let getActualSleepHours = () =>
  getSleepHours("Monday") +
  getSleepHours("Tuesday") +
  getSleepHours("Wednesday") +
  getSleepHours("Thursday") +
  getSleepHours("Friday") +
  getSleepHours("Saturday") +
  getSleepHours("Sunday");

let getIdealSleepHours = () => {
  let idealHours;
  idealHours = 5;
  return idealHours * 7;
};

console.log(getActualSleepHours());
console.log(getIdealSleepHours());

let calculateSleepDebt = () => {
  let actualSleepHours = getActualSleepHours();
  let idealSleepHours = getIdealSleepHours();
  console.log(actualSleepHours);
  console.log(idealSleepHours);
  if (actualSleepHours === idealSleepHours) {
    return "User got the perfect amount of sleep";
  } else if (actualSleepHours > idealSleepHours) {
    return (
      'User got more sleep than needed, has an excess of ' +
      (actualSleepHours -
      idealSleepHours)
    );
  } else if (actualSleepHours < idealSleepHours) {
    return (
      'User should get some rest and is short by ' +
      (idealSleepHours -
      actualSleepHours)
    );
  } else {
    return 'Nothing';
  }
};

console.log(calculateSleepDebt());
