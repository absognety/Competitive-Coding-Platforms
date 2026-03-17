const robot = {
  model: '1E78V2',
  energyLevel: 100,
  provideInfo: function() {
    return (`I am ${this.model} and my current energy level is ${this.energyLevel}.`)
  }
};
console.log(robot.provideInfo());
