/* In this challenge, we practice using JavaScript classes. 

Task
Create a Polygon class that has the following properties:
- A constructor that takes an array of integer values describing the lengths of the polygon's sides.
- A perimeter() method that returns the polygon's perimeter.
Locked code in the editor tests the Polygon constructor and the perimeter method.
Note: The perimeter method must be lowercase and spelled correctly.

Code */

class Polygon {
    constructor(arr) {
        this.sides = arr
    }

    perimeter() {
        return this.sides.reduce((acc, val) => acc + val)
    }
}

const rectangle = new Polygon([10, 20, 10, 20]);
const square = new Polygon([10, 10, 10, 10]);
const pentagon = new Polygon([10, 20, 30, 40, 43]);

console.log(rectangle.perimeter());
console.log(square.perimeter());
console.log(pentagon.perimeter());
