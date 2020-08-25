var rect = {
    perimeter: (x, y) => (2*(x+y)),
    area: (x, y) => (x*y)
};

function sovleRect(l, b) {
    console.log("Solving for rectangel with l = " + l + " and b = " + b);

    if (l <= 0 || b <= 0) {
        console.log("Rectangle dimensions should be greater than zero: l = " + l + ", and b = " + b);
    }
    else {
        console.log("The area of the rectangle is " + rect.area(l, b));
        console.log("The perimeter of the rectangle is " + rect.perimeter(l, b));
    }
}

sovleRect(2,4);
sovleRect(3,5);
sovleRect(0,5);
sovleRect(-3,5);