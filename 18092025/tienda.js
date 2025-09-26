var productos = [
    { nombre: 'Camisa', precio: 300 },
    { nombre: 'Pantalón', precio: 500 },
    { nombre: 'Zapatos', precio: 800 },
    { nombre: 'Sombrero', precio: 200 }
];

var carrito = [];
var opcion;

do {
    opcion = parseInt(prompt(
        "Seleccione un producto para agregar al carrito:\n" +
        "1. Camisa - $300\n" +
        "2. Pantalón - $500\n" +
        "3. Zapatos - $800\n" +
        "4. Sombrero - $200\n" +
        "5. Ver Carrito y Total\n" +
        "6. Salir"
    ));

    if (opcion >= 1 && opcion <= 4) {
        let producto = productos[opcion - 1]; // restamos 1 porque los arrays empiezan en 0
        carrito.push(producto);
        alert(producto.nombre + " agregado al carrito.");
    } 
    else if (opcion === 5) {
        if (carrito.length === 0) {
            alert("El carrito está vacío.");
        } else {
            let total = carrito.reduce((suma, p) => suma + p.precio, 0);
            let lista = carrito.map(p => "- " + p.nombre + " $" + p.precio).join("\n");
            alert("Carrito:\n" + lista + "\n\nTotal: $" + total);
        }
    }

} while (opcion !== 6);

alert("Gracias por usar el sistema de carrito.");

