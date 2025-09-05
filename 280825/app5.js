let num1 = parseInt(prompt("ingresa el numero A"));
let num2 = parseInt(prompt("ingresa el numero B"));
let num3 = parseInt(prompt("ingresa el numero C"));

// Numero mas grande
if ((num1 > num2) && (num1>num3)){
    console.log("el numero A es el mas grande "+ num1)
}
else{
    if ((num2 > num1) && (num2>num3)){
    console.log("el numero B es el mas grande "+ num2)
}
    else{
        if ((num3 > num1) && (num3>num1)){
            console.log ("el numero mas grande es C " + num3)
        }
    
    else {
        console.log("no hay numero mas grande")
    }
}
}
// Numero mas pequenio
if ((num1 < num2) && (num1<num3)){
    console.log("el numero A es el mas pequenio "+ num1)
}
else{
    if ((num2 < num1) && (num2<num3)){
    console.log("el numero B es el mas pequenio "+ num2)
}
    else{
        if ((num3 < num1) && (num3<num1)){
            console.log ("el numero mas pequenio es C " + num3)
        }
        else {
            console.log("no hay numero pequenio")
        }
    }
}

// Numeros iguales 

if (num1 == num2 == num3) {
    console.log("los numeros A B C son iguales "+ num1 + num2 + num3)
}
else{
    
    if (num1 == num2){
    console.log("el numero A y B son iguales")
    }
    else {
        if (num3 == num2) {
            console.log ("el numero B  C son iguales " + num3 + num2 )
        }
        else { 
            if (num1 == num3 ) {
                console.log("el A y C son iguales " + num1 + num3 )
        }
        else {
            console.log("no hay numeros iguales")
        }
        }
    }
    

}
