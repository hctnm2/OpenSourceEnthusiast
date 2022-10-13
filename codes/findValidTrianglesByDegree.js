// Question: Given three angles of a triange, your function should return if it is a scalen, isosceles, equilateral triangle or not a triangle at all.

const triangle = (angleOne, angleTwo, angleThree) => {
  if (angleOne + angleTwo + angleThree === 180) {
    console.log("It's a triangle.")
    if (angleOne !== angleTwo && angleOne !== angleThree) {
      console.log("It's a scalen triangle.")
    } else if (angleOne === angleTwo && angleOne === angleThree) {
      console.log("It's an equilateral triangle.")
    } else if (
      (angleOne === angleTwo && angleOne === angleThree) ||
      angleOne === angleTwo ||
      angleTwo === angleThree ||
      angleOne === angleThree
    ) {
      console.log("It's and isosceles triangle.")
    }
  } else console.log("It's not a triangle.")
}

// triangle(59, 61, 60); //(Scalen)
// triangle(60, 60, 60); //(Equilateral)
// triangle(45, 45, 90); //(Equilateral)
