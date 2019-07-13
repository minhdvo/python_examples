/* Arrays
In this challenge, we learn about Arrays. 

Task
Complete the getSecondLargest function in the editor below. It has one parameter: an array, nums , of n numbers. 
The function must find and return the second largest number in nums.

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
   Return the second largest number in the array.
   @param {Number[]} nums - An array of numbers.
   @return {Number} The second largest number in the array.
*/
function getSecondLargest(nums) {
    let largest = nums[0];
    let secondLargest = nums[0];

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > largest) {
            secondLargest = largest;
            largest = nums[i];
            continue;
        }

        if ((nums[i] > secondLargest) && (nums[i] < largest)) {
            secondLargest = nums[i];
        }
    }

    return secondLargest;
}


function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);
    
    console.log(getSecondLargest(nums));
}
