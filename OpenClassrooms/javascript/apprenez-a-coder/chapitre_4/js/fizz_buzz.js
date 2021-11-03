for (i=1;i<100;i++){
    while ((i%5===0) && (i%3===0) && i<100){
        console.log("FizzBuzz")
        i++
    }
    while (i%3===0 && i<100){
        console.log("Fizz")
        i++
    }
    while ((i%5)===0 && (i%3)!==0 && i<=100){
        console.log("Buzz")
        i++
    }
    if (i<=100){
    console.log(i) 
    }
}
