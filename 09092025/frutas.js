const frutas = [];

const fruta = prompt("Feria de las frutas: Que fruta quiere agregar al carrito?");

frutas.push(fruta);

while (confirm("Quieres agregar otra fruta ?")){
    const fruta = prompt("Que otra fruta quieres agregar?");
    frutas.push(fruta);
}


console.log("Usted compro");
for (let fruta of frutas){
    console.log(fruta);
}
