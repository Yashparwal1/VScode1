let marks = {
    "Comouter" : 90,
    "Hindi" : 91,
    "Maths" : 92,
    "Sanscrit" : 93,
    "English" : 94
}

// for(let subject in student){
//     console.log("Marks in "+ subject + " is " + student[subject])
// }

for(let i=0; i<Object.keys(marks).length;i++){
    //Object.keys ==> gives all keys in an array form (or list form like in python then, .length ==> gives the length of the list // console.log(Object.keys(marks)); 
    // console.log("Marks in "+ Object.keys(marks)[i] + " are " + Object.values(marks)[i]);
    console.log("Marks in "+ Object.keys(marks)[i] + " are " + marks[Object.keys(marks)[i]]); //marks[key] = value
    
}
