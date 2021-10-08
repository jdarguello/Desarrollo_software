angular.module('Checkout', [])
    .controller('control', function() {
        var c = this;   //Nombre del contenido
        c.productos = [
            {nombre:"Manzana", precio:1000},
            {nombre:"Pera", precio:1500},
            {nombre:"Fresa", precio:3000}
        ];

        //Variables de compra
        c.listaCompras = [];
        c.art = "";
        c.cant = 0;
        c.total = 0;

        //Retorno del diccionario del producto
        function proData(nombre) {
            for (var i=0; i< c.productos.length; i++) {
                if (c.productos[i].nombre == nombre) {
                    return c.productos[i];
                }
            }
        }

        //Función de adición al carrito
        c.addProd = function() {
            var artData = proData(c.art);
            console.log("Diccionario = ", artData.nombre);
            c.listaCompras.push([artData.nombre, c.cant, artData.precio, c.cant*artData.precio]);
            c.total += c.cant*artData.precio;
            c.art={};
            c.cant=0;
        };
    });