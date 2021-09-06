function alerta(){
    window.alert("Hola!!!")
}

function saludar(){
    var nombre = document.getElementById("texto").value;
    alert("Buenos Días "+nombre);
}

function cerrar(){
    window.close();
}

function saludo(){
    var saludo = document.getElementById("txt1").value;
    var mensaje = "Buen días: "+saludo;
    var caja = document.getElementById("divsaludo");
    caja.innerHTML=mensaje;

}