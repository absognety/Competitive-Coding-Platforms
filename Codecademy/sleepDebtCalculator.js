let getSleepHours = (day) => {
  switch (day) {
    case "Monday":
      return 4.9;
    case "Tuesday":
      return 4.35;
    case "Wednesday":
      return 4.27;
    case "Thursday":
      return 5.2;
    case "Friday":
      return 4.76;
    case "Saturday":
      return 3.5;
    case "Sunday":
      return 6.5;
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
  }
};

console.log(calculateSleepDebt());
