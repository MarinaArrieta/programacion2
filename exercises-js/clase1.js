const input = [1, 2, 3, 4, 5];

const output = input.map((num) => {
    const squared = Math.pow(num, 2);
    console.log(squared);
    return squared;
});

const input2 = [1, -4, 12, 0, -3, 29, -150];
const result = input2.filter((num) => num > 0).reduce((acc, num) => acc + num, 0);
console.log('Result: ', result);

const input3 = [12, 46, 32, 64];
input3.sort((a, b) => a - b);

const result1 = input3.reduce(
    (accumulator, currentValue, index, array) => {
        accumulator.mean += currentValue / array.length;

        if (array.length % 2 === 0) {
            if (index === array.length / 2 - 1) {
                accumulator.median += currentValue;
            } else if (index === array.length / 2) {
                accumulator.median += currentValue;
                accumulator.median /= 2;
            }
        } else {
            if (index === (array.length - 1) / 2) {
                accumulator.median = currentValue;
            }
        }

        return accumulator;
    },
    { mean: 0, median: 0 },
);

console.log(result1);

const input4 = "George Raymond Richard Martin";
const result2 = input4.split(" ").map((word) => word[0].toUpperCase()).join("");
console.log('Result 1: ', result2);

const input5 = "George Raymond Richard Martin";
const result3 = input4.match(/\b\w/g).join("").toUpperCase();
console.log('Result 2: ', result3);

const input6 = [
    {
        name: "John",
        age: 13,
    },
    {
        name: "Mark",
        age: 56,
    },
    {
        name: "Rachel",
        age: 45,
    },
    {
        name: "Nate",
        age: 67,
    },
    {
        name: "Jennifer",
        age: 65,
    },
];

const min = Math.min(...input6.map((person) => person.age));
console.log("Min: ", min);
const max = Math.max(...input6.map((person) => person.age));
console.log("Max: ", max);
console.log("deference: ", max - min);

const ages = input6.map((person) => person.age);
const result4 = [Math.min(...ages), Math.max(...ages), Math.max(...ages) - Math.min(...ages)];
console.log("Result 4: ", result4);