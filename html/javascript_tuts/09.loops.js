/* 
Types of loops:
    for loop
    for in loop
    for of loop
    while loop
    do while loop

*/
const prompt = require("prompt-sync")({sigint: true});

// for (let i = 0; i < 5; i++) {
//     console.log(i);
// }

// let sum = 0
// let n = Number.parseInt(prompt("Enter the value of n: "))
// for (let i = 0; i <= n; i++) {
//     sum += i
// }
// console.log("Sum of 1st", n , "natural numbers is:", sum);

let children = {
    a : 90,
    b : 91,
    c : 92,
    d : 93
}
for (let key in children) {
    console.log("Marks of",key,"is",children[key])
}

// for (let key of children){ //children isn not iterable -- in for-of loop the given object should be iterable
//     console.log("Marks of",key,"is",children[key]);
// }

// arr = ['h','a','r','r','y']
// // arr = [1,2,3,4,5]
// for (let key of arr){ // for (let i of "yash") or for (let i of [1,2,3,4,5])
//     console.log(key);
// }

// while (condition) {
    
// }

// do {
    
// } while (condition);