"use strict"

// 
// Calculate quadratic equation solutions 
// x^2 + (-10^t - 1)x + 10^t = 0
//

let main = () => {

//  
// Use Readline to get input value 
// Considering test environment, use static settled variable t
//

    const t = 17
    
	let a = 1
	let b = -1 * Math.pow(10, t) - 1
	let c = Math.pow(10, t)

	let x1 = (-1 * b + Math.sqrt(b * b - 4 * a * c)) / 2 / a
	let x2 = (-1 * b - Math.sqrt(b * b - 4 * a * c)) / 2 / a

    console.log(`Solution x1 = ${x1}`)
	console.log(`Solution x2 = ${x2}`)

//
// Note 
// Surprisingly found x2 equals 0 only when t is above 17 but not 11 in javascript
//

}

main()

//
// Arthor: Jiongchi Yu
// Date: 2020.3.18
//
