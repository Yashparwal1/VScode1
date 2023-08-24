/* A function in Js is a block of code which is used to perform a particular task. When a task is performed multiple times in the code, we use function to write code for it one time and execute several time whenever required by calling that function.

It also helps when some changes are to be required in a piece of code which is written several time, so it would be difficult to do changes at all places. But if function is used, it would be required to do changes in that function only. 

*/

function OnePlusAvg(x,y){
    return (1 + (x+y)/2)
}
const test = (x,y) => { //this is called arror function
    return (1 + (x+y)/2)
}

const hello = () => {
    console.log("this one is for printing")
    return "this one is for returning"
}
let a = 1
let b = 2
let c = 3

// console.log(OnePlusAvg(a,b))
// console.log(OnePlusAvg(b,c))
// console.log(OnePlusAvg(a,c))
test()
console.log(hello())