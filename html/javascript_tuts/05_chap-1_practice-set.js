//1.  Create a variable of type string and add a number to it.
//2.  use typeof operator to find the dtatype of string in last question
//3.  Create a const object in js. Can you change it to hold a number later?
//4.  try to add a new key to the const object in problem 3. Were you able to it.
//5.  Write a js program to ceate a word meaning dictionary of 5 words

let x = "yash"
let y = 25
console.log(x+y)
// -------------------------------------------------------------

console.log(typeof(x+y))
// -------------------------------------------------------------

const pi1 = "constant value" //this is constant varibale
const pi2 = { //object datatype is "undefined"
    name: "yash",
    age:20,
    institute:"GNIOT"
}  //this is constant object

// pi2 = 25 //cannot change it to hold a number
// -------------------------------------------------------------

pi2["friend"] = "keton" // yes we can add or modify new key to const object
pi2["name"] = "parwal"

console.log(pi2)

// -------------------------------------------------------------

const dict = {
    arduno:"a programmable board",
    botnet:"collection of infected computer devices",
    cybersecurity:"security and safety of digital assets",
    doxing:"discovering  and publishing private or identifying information about a particular individual on the internet, typically with malicious intent",
    Exploit:"a piece of code or action that takes advantage of a vulnerability to hack the system"
}

console.log(dict.arduno) 
console.log(dict["arduno"])