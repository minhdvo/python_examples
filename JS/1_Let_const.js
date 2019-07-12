/* Task
- Declare a constant variable, PI , and assign it the value Math.PI. You will not pass this challenge unless the variable is 
declared as a constant and named PI (uppercase).
- Read a number, r , denoting the radius of a circle from stdin.
- Use PI and r to calculate the area and perimeter of a circle having radius .
- Print area as the first line of output and print perimeter as the second line of output.

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

function main() {
    // Read input using 'readLine()' and print output using 'console.log()'.
    let radius = readLine();
    const PI = Math.PI;
    
    
    // Print the area of the circle:
    console.log(PI * radius ** 2);
    // Print the perimeter of the circle:
    console.log(2*PI * radius);

    try {    
        // Attempt to redefine the value of constant variable PI
        PI = 0;
        // Attempt to print the value of PI
        console.log(PI);
    } catch(error) {
        console.error("You correctly declared 'PI' as a constant.");
    }
}