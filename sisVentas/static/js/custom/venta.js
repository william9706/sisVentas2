$('#bt_add').on("click", ()=>{
    agregar();
});

let cont=0;
let total_ingreso=0;
let subtotal=[];
$("#guardar").hide();

function agregar(){
    idarticulo=$("#id_form-0-articulos").val();
    articulo=$("#id_form-0-articulos option:selected").text();
    cantidad= parseInt($("#id_form-0-cantidad").val());
    descuento= parseInt($("#id_form-0-descuento").val());
    precio_venta= parseFloat($("#id_form-0-precio_venta").val());
    if (idarticulo !="" && cantidad!="" && cantidad > 0 && precio_venta!=""){
        subtotal[cont]=(cantidad*precio_venta-descuento);
        total_ingreso += subtotal[cont];
        var fila = '<tr class="selected" id="fila' + cont + '">' +
        '<td><button type="button" class="btn btn-warning" onclick="eliminar(' + cont + ');">X</button></td>' +
        '<td><input type="hidden" name="articulos" value="' + idarticulo + '">' + articulo + '</td>' +
        '<td><input type="number" name="cantidad" value="' + cantidad + '"></td>' +
        '<td><input type="number" name="precio_venta" value="' + precio_venta + '"></td>' +
        '<td><input type="number" name="descuento" value="' + descuento + '"></td>' +
        '<td>' + subtotal[cont] + '</td>' +
        '</tr>';

        cont++;
        limpiar();
        $("#total").html("COP/. " + total_ingreso);
        evaluar();
        $('#detalles').append(fila);
    }else{

        alert("Error al ingresar el detalle de venta, revise los datos del articulo");
    }
}

function limpiar(){
   $("#id_form-0-cantidad").val("");
   $("#id_form-0-precio_venta").val("");

}
function evaluar(){
    if (total_ingreso > 0) {
        $("#guardar").show();

    } else {
        $("#guardar").hide();

    }
}

function eliminar(index){
    total_ingreso-=subtotal[index];
    $("#total").html("COP/." +total_ingreso);
    $("#fila" + index).remove();
    evaluar();
}

let arrServicio = new Array();
arrServicio = ['', 'Articulos', 'Cantidad', 'PrecioVenta'];

$('#formulario-ingreso').submit(function (e) {
    validarJson('detalles', 'selected', arrServicio);
});

/**
 * 
 * @param {*} table
 * @param {*} nameClass
 * @param {*} arrHeader
 * Función que permite construir JSON cuando se envíen los detalles del ingreso en el request.
 */
let validarJson = (table, nameClass, arrHeader) => {
    var $table = $(`table[id='${table}']`),
        rows = [],
        header = arrHeader;
    $table.find(`tr[class='${nameClass}']`).each(function (i) {
        var row = {};
        $(this).find("td").each(function (index) {
            var key = header[index]
            row[key] = $(this).find('input').val();
            
        });
        rows.push(row);
    });
    document.getElementById('id_detalle_ventas').value = JSON.stringify(rows);    
}