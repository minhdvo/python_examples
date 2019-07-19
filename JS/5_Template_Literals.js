/* Template Literals
In this challenge, we practice using JavaScript Template Literals. 

Task
The code in the editor has a tagged template literal that passes the area and perimeter of a rectangle to a tag function named sides. 
Recall that the first argument of a tag function is an array of string literals from the template, and the subsequent values are the 
template's respective expression values.

Complete the function in the editor so that it does the following:
- Finds the initial values of s1 and s2 by plugging the area and perimeter values into the formula.
where A is the rectangle's area and P is its perimeter.
- Creates an array consisting of s1 and s2 and sorts it in ascending order.
- Returns the sorted array.

Code */
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Determine the original side lengths and return an array:
 * - The first element is the length of the shorter side
 * - The second element is the length of the longer side
 * 
 * Parameter(s):
 * literals: The tagged template literal's array of strings.
 * expressions: The tagged template literal's array of expression values (i.e., [area, perimeter]).
 */
function sides(literals, ...expressions) {
    const [a, p] = expressions;
    
    const root = Math.sqrt((p * p) - (16 * a))
    const s1 = (p + root) / 4;
    const s2 = (p - root) / 4;
    
    return ([s2, s1]);
}


function main() {
    let s1 = +(readLine());
    let s2 = +(readLine());
    
    [s1, s2] = [s1, s2].sort();
    
    const [x, y] = sides`The area is: ${s1 * s2}.\nThe perimeter is: ${2 * (s1 + s2)}.`;
    
    console.log((s1 === x) ? s1 : -1);
    console.log((s2 === y) ? s2 : -1);
}
