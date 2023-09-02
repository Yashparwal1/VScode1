const prompt = require("prompt-sync")({sigint: true});
// let marks = {
//     "Comouter" : 90,
//     "Hindi" : 91,
//     "Maths" : 92,
//     "Sanscrit" : 93,
//     "English" : 94
// }

// for(let subject in marks){
//     console.log("Marks in "+ subject + " is " + marks[subject])
// }

// for(let i=0; i<Object.keys(marks).length;i++){
//     //Object.keys ==> gives all keys in an array form (or list form like in python then, .length ==> gives the length of the list // console.log(Object.keys(marks)); 
//     // console.log("Marks in "+ Object.keys(marks)[i] + " are " + Object.values(marks)[i]);
//     console.log("Marks in "+ Object.keys(marks)[i] + " are " + marks[Object.keys(marks)[i]]); //marks[key] = value
    
// }

// -------------------------------------------------------------------------------

// const correct = 10
// while (true){
//     num = prompt("Enter a number: ")
//     if (num == correct){
//         console.log("Now its Correct !!")
//         break
//     }
//     else{
//         console.log("enter again");
//     }
// }

// let i
// while(i != correct){
//     i = prompt("guess the no: ")
//     console.log("Wrong!! Enter again...");
// }
// console.log("Now its Correct !!")

// ---------------------------------------------------------------------

const mean = (a,b,c,d,e) => {
    return ((a+b+c+d+e)/5)
}

// values = prompt("Enter 5 numbers separated by comma(,): ").split(",")
// console.log(values);
console.log(mean(1,2,3,4,5))