let num = 100;
let str = "JavaScript";
let isStudent = true;
let notDefined;
let emptyValue = null;
let person = { name: "Amit", age: 21 };
let numbers = [10, 20, 30];

console.log(num, typeof num);
console.log(str, typeof str);
console.log(isStudent, typeof isStudent);
console.log(notDefined, typeof notDefined);
console.log(emptyValue, typeof emptyValue);
console.log(person, typeof person);
console.log(numbers, typeof numbers);

let a = 20;
let b = 5;

console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);
console.log(a % b);

let fullName = "Shriprasad Patil";

console.log(fullName.length);
console.log(fullName.toUpperCase());
console.log(fullName.toLowerCase());
console.log(fullName[0]);

function greet() {
    console.log("Hello, Welcome to JavaScript!");
}
greet();

function add(x, y) {
    let sum = x + y;
    console.log(sum);
    return sum;
}
add(15, 25);

function isEven(num) {
    return num % 2 === 0;
}

console.log(isEven(10));
console.log(isEven(7));

const square = (num) => num * num;

console.log(square(4));
console.log(square(9));

function calculateArea(radius = 1) {
    return Math.PI * radius * radius;
}

console.log(calculateArea());
console.log(calculateArea(5));
