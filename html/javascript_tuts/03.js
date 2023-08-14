var a = 25
var b = "yash" //var is global scoped
var c = null
var d = undefined
{
    let b = 'this' //let is block scoped
    console.log(b)
}
console.log(b)

const author = "yash"
// let author = 5 //cannot be recreated not updated
author = 5 //typeerror: Assignment to constant variable
console.log(author)