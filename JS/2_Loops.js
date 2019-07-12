// Loops
// In this challenge, we practice looping over the characters of string.

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
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    var x = '';
    const n = s.length;
    for (var i = 0; i < n; ++i){
        if ('aeiou'.includes(s[i])) {
            console.log(s[i]);
        } else {
            x = x + s[i] + '\n';
        }
         
    }
    console.log(x.trim());
    
}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}
