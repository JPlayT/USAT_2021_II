function validar(){

    var contador=0;


    for (let index = 0; index < 10; index++) {

        var identificacion= "campo"+index;

        if (document.getElementById(identificacion).value=="") {
            contador=contador+1;
        }
    }

    
    if (contador>0) {

        alert("LLene completamente los datos por favor.");
        
    }else{
        alert("Registrado Satisfactoriamente");
        limpiar();
        
    }

}

function limpiar(){

    for (let index = 0; index < 10; index++) {

        var identificacion= "campo"+index;
        var objeto = document.getElementById(identificacion);
        objeto.value="";
    }

}

