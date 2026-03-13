const userChoices = ['rock', 'paper', 'scissors', 'bomb'];
const computerChoices = ['rock', 'paper', 'scissors']
let randomIndex;
randomIndex = Math.floor(Math.random() * userChoices.length);
const userChoice = userChoices[randomIndex];
console.log('User Choice ' + userChoice);
randomIndex = Math.floor(Math.random() * computerChoices.length);
const compChoice = computerChoices[randomIndex];
console.log('Computer Choice ' + compChoice);


// Play the game
function playGameRPS(userChoice, compChoice) {
  switch (true) {
    case userChoice === 'bomb':
      console.log('Winner is User');
      break;
    case (userChoice === 'rock' && compChoice === 'paper'):
      console.log('Winner is Computer');break;
    case (userChoice === 'paper' && compChoice === 'rock'):
      console.log('Winner is User');
      break;
    case (userChoice === 'rock' && compChoice === 'scissors'):
      console.log('Winner is User');
      break;
    case (userChoice === 'scissors' && compChoice === 'rock'):
      console.log('Winner is Computer');
      break;
    case (userChoice === 'paper' && compChoice === 'scissors'):
      console.log('Winner is Computer');
      break;
    case (userChoice === 'scissors' && compChoice === 'paper'):
      console.log('Winner is User');
      break;
    case (userChoice === compChoice):
      console.log('It\'s a draw');
      break;
    default:
      console.log("Something else....")
      break;
  }
}
playGameRPS(userChoice, compChoice);
