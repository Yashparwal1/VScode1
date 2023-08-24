// if , if..else , if..else if..else , switch case statements
const prompt = require("prompt-sync")({sigint: true});

// let a = prompt("Enter a no: ") // like scanf or input
// console.log(typeof(a)) // prompt will always take input as string

// a = Number.parseInt() //typecasting into int
// console.log(typeof(a)) 

// if (a<0){
//     alert("this is invalid age") //will give popup in browser
// }
// else if (a>0){
//     alert("this is a valid age")
// }
// else {
//     alert("Age is 0")
// }

day = Number.parseInt(prompt("Enter day number: "))
switch (day) {
    case 1:
        console.log("Monday")
        break;
    case 2:
        console.log("Tuesday")
        break;
    case 3:
        console.log("Wednesday")
        break;
    case 4:
        console.log("Thursday")
        break;
    case 5:
        console.log("Friday")
        break;
    case 6:
        console.log("Saturday")
        break;
    case 7:
        console.log("Sunday")
        break;
    default:
        console.log("Enter correct day number between 1 to 7");
        break;
}

age = Number.parseInt(prompt("Enter your age: "))
console.log("you can", age > 18 ? "Drive":"not drive");