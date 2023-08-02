// call a property on an object
// a property is not a method, so it doesn't have ()
console.log('Daniel'.length);

// call a method on an object
console.log("hello there".toUpperCase());

// built-in Math object
console.log(Math.random()); // Prints a random number between 0 and 1 aka [0.0,1.0)

Math.random() * 50; // generate a random number between 0 and 50 aka [0.0,50.0)

console.log(Math.ceil(43.8)); // 44

console.log(Number.isInteger(2017)); // true

// you can use let/var to declare a variable without giving it a value
let price;
console.log(price); // Output: undefined
price = 350;
console.log(price); // Output: 350
price = 300;
console.log(price); // output: 300

// If you try to reassign a const variable, you’ll get a TypeError
// If you try to declare a const variable without a value, you’ll get a SyntaxError
const entree = "Enchiladas";

let levelUp = 10;
let powerLevel = 9001;
let multiplyMe = 32;
let quarterMe = 1152;
levelUp += 5; // 15
powerLevel -= 100; // 8901
multiplyMe *= 11; // 352
quarterMe /= 4; // 288

let gainedDollar = 3;
let lostDollar = 50;
gainedDollar++; // 4
lostDollar--; // 49

// string interpolation with template literal
let myName = "Daniel";
let myCity = "Dallas";
console.log(`My name is ${myName}. My favorite city is ${myCity}`);

// typeof variable
let newVariable = 'Playing around with typeof.';
console.log(typeof newVariable); // string
newVariable = 1;
console.log(typeof newVariable); // number

// falsy values
// 0
// Empty strings like "" or ''
// null which represent when there is no value at all
// undefined which represent when a declared variable lacks a value
// NaN, or Not a Number

// short circuit evaluation
let username = '';
let defaultName = username || 'Stranger';
console.log(defaultName); // Prints: Stranger

// ternary operator
let boolExample = true
boolExample ? console.log("var was true") : console.log('var was false');

// switch case
let athleteFinalPosition = 'first place';
 
switch (athleteFinalPosition) {
  case 'first place':
    console.log('You get the gold medal!');
    break;
  case 'second place':
    console.log('You get the silver medal!');
    break;
  case 'third place':
    console.log('You get the bronze medal!');
    break;
  default:
    console.log('No medal awarded.');
    break;
}
// note that if the break is not present then lower blocks will execute regardless of a match found in prior blocks

// ex of hoising: allowing function delcarations before the function is defined
greetWorld(); // Output: Hello, World!
 
function greetWorld() {
  console.log('Hello, World!');
}

/*
functions are 'first class' objects meaning they have properties and methods like .length, .name, .toString()

A higher-order function is a function that either accepts functions as parameters, returns a function, or both

callback functions are functions that get passed in as parameters callback functions. Callback functions get 
invoked during the execution of the higher-order function

When we invoke a higher-order function, and pass another function in as an argument, we don’t invoke the 
argument function. Invoking it would evaluate to passing in the return value of that function call. With 
callback functions, we pass in the function itself by typing the function name without the parentheses

*/

const higherOrderFunc = param => {
  param();
  return `I just invoked ${param.name} as a callback function!`
}
 
const anotherFunc = () => {
  return 'I\'m being invoked by the higher-order function!';
}
 
higherOrderFunc(anotherFunc);

// we can also define an anonymous function directly in the param namespace when invoking the higher order func
higherOrderFunc(() => {
for (let i = 0; i <= 10; i++){
  console.log(i);
}
});

// callback ex 3
const addTwo = num => {
  return num + 2;
}

const checkConsistentOutput = (func, val) => {
  const checkA = val + 2;
  const checkB = func(val);
  return checkA === checkB ? checkB : 'inconsistent results';
}

console.log(checkConsistentOutput(addTwo,8)); // 10

// function with default parameter
function greeting (name = 'stranger') {
  console.log(`Hello, ${name}!`)
}
 
greeting('Nick') // Output: Hello, Nick!
greeting() // Output: Hello, stranger!

// functions with no return value will return 'undefined'
function rectangleArea(width, height) {
  let area = width * height;
}
console.log(rectangleArea(5, 7)) // Prints undefined

// to capture the value, simply use the return keyword
function rectangleArea(width, height) {
  let area = width * height;
  return area;
}
console.log(rectangleArea(5, 7)) // Prints 35


// function expression (note: hoisting not allowed)
const plantNeedsWater = function(day) {
  if (day === 'Wednesday') {
    return true;
  } else {
    return false;
  }
};

// arrow functions
const plantNeedsWater2 = (day) => {
  if (day === 'Wednesday') {
    return true;
  } else {
    return false;
  }
};

// arrow function with one paramter does not need () around the param,
// also, if the body is one line, the {} can be removed and the line will be implicitly returned
const squareNum = num => num * num;

// ex with ternary
const plantNeedsWater3 = day => day === 'Wednesday' ? true : false;

// global local scope ex 1
const city = 'New York City'; // global scope
const logCitySkyline = () => {
  let skyscraper = 'Empire State Building'; // function level scope
  return 'The stars over the ' + skyscraper + ' in ' + city;
};

console.log(logCitySkyline()); // The stars over the Empire State Building in New York City

/* 
NaN: Not a number: As the name implies, it is used to denote that the value
     of an object is not a number. There are many ways that you can generate
     this error, one being invalid math opertaions such as 0/0 or sqrt(-1)

undefined: It means that the object does not have any value, therefore
           undefined. This occurs when you create a variable and don't
           assign a value to it.

null: It means that the object is empty and is not pointing to any memory
      address.
*/

// scope pollution
let num = 50;
const changeNum = () => {
	// let num = 75;
  num = 100;
  return num;
}
console.log(changeNum());
console.log(num);

// weird scope thing ex 1
console.log(x === undefined); // true
let x = 3;

const wtf = () => {
  x = 4;
  console.log('globally scoped x: ' + x);
  var x = 'local val';
}
console.log('global x: '+x); // 3
wtf(); // 4
console.log('global x: '+x); // 3

// lists ex 1 (note: indexing out of bounds returns undefined instead of an error)
const famousSayings = ['Fortune favors the brave.', 'A joke is a very serious thing.', 'Where there is love there is life.'];
const listItem = famousSayings[0];
console.log(listItem);
console.log(famousSayings[2]);
console.log(famousSayings[3]); // undefined

// const vs let arrays
let condiments = ['Ketchup', 'Mustard', 'Soy Sauce', 'Sriracha'];

const utensils = ['Fork', 'Knife', 'Chopsticks', 'Spork'];

condiments[0] = 'Mayo'; // can change elements of let array
console.log(condiments);

condiments = ['Mayo']; // can reasign the namespace to a new array
console.log(condiments);

utensils[3] = 'Spoon'; // can change elements const array
console.log(utensils);

utensils = ['Spoon']; // cannot reasign to a new array
console.log(utensils);

// array properties
const objectives = [1, 2, 3];
console.log(objectives.length); // 3
itemTracker.push(4,5);
console.log(objectives); // [1, 2, 3, 4, 5]
const removed = objectives.pop(); // 5
console.log(objectives); // [1, 2, 3, 4]
console.log(removed); // 5

// looping through arrays
const vacationSpots = ['Bali', 'Paris', 'Tulum'];
// Write your code below
for (let i = 0; i < vacationSpots.length; i++){
  console.log(`I would love to visit ${vacationSpots[i]}`);
}

// do while will perform the first do even if the while condition is false
const cupsOfSugarNeeded = 1;
let cupsAdded = 0;

do {
  cupsAdded += 1;
  console.log(cupsAdded);
} while (cupsAdded < cupsOfSugarNeeded);

// forEach
function printGrocery element => console.log(element);
grocery = [1,2,3];
grocery.forEach(printGrocery);

// .map -------------------------------------------------------------------------------
const animals = ['Hen', 'elephant', 'llama', 'leopard', 'ostrich', 'Whale', 'octopus', 'rabbit', 'lion', 'dog'];

// Create the secretMessage array below
const secretMessage = animals.map(number => {
  return number[0];
})

console.log(secretMessage.join(''));

const bigNumbers = [100, 200, 300, 400, 500];

// Create the smallNumbers array below
const smallNumbers = bigNumbers.map(i => i/100) // -------------------------------------