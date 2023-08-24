/* 
A fragment of code that produces a value is called an expression. Every value written literally is an expression. For eg. 77; , "yash parwal"

Arithmatic | Assignment | comparision | logical(&&, ||, !) | Bitwise 

*/
let a = 20, b=20
console.log("a+b =",a+b)
console.log("a/b =",a/b) //result is floating value
//all operators are same as C lang like **,++,--.

// comparision operator
// ==      -> equal to 
// !=      -> not equal to
// ===     -> equal value and equal type
// !==     -> not equal value or not equal type
// <,>,<=,>=
// ?       -> turnary operator

let c1 = 6
let c2 = "6"

console.log("c1 == c2",c1==c2) // true - because value is same
console.log("c1 == c2",c1!=c2) // false - because value is same
console.log("c1 == c2",c1===c2) // flase - because type is different even if the value is same
console.log("c1 == c2",c1!==c2) // true - becuase type is not equal even if the value is same

