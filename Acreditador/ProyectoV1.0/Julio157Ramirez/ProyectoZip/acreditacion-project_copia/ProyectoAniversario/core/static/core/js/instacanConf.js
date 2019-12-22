$(document).ready(function(){

    function setValueInput(value){
        var str = "registrocivil";
        if (value.search(str) !== -1) {
            var str1 = value.split("=")[1];
            var str2 = str1.split("&")[0];

            document.getElementById("inputSearch").value = str2;
        }else{
           document.getElementById("inputSearch").value = value;
        }
        document.getElementById("p1").innerHTML = value;
    }

    function closeScanner(){
        Instascan.Camera.getCameras().then(function (cameras) {
            if (cameras.length > 0) {
                scanner.stop();
            } else {
                console.error('Error al apagar la camara');
            }
        }).catch(function (e) {
            console.error(e);
        });
    };

    //Variables
    var qrLector = document.getElementById('btn_qr');
    var qrLectorClose = document.getElementById('btn_qr_close');
    var selectCameras = document.getElementById('exampleFormControlSelect1');


    //Configuracion del Scanner
    let scanner = new Instascan.Scanner({
        video: document.getElementById('preview'),
        mirror: false
    });


    //Funcion para llenar el ComboBox con las camaras disp.
    Instascan.Camera.getCameras().then(function (cameras) {
        if (cameras.length > 0) {
            for(i in cameras){
                selectCameras.innerHTML += '<option value="'+ i +'">' + cameras[i].name + '</option>';
                console.log(i);
                console.log(cameras[i].id);
                console.log(cameras[i].name);
            };
        } else {
            selectCameras.innerHTML = '<option disabled selected> No se encuentran camaras </option>';
            console.error('No cameras found.');
        }
    }).catch(function (e) {
        camerasButtons.innerHTML = '<a class="dropdown-item disabled" href="#">Error al cargar camara</a>'
        console.error(e);
    });


    //Al iniciar setear por defecto la camara 0
    qrLector.addEventListener('click', function () {
        //Modificar esta funciona con la eleccion provenientes del Input tipos SELECT
        Instascan.Camera.getCameras().then(function (cameras) {
            if (cameras.length > 0) {
                scanner.start(cameras[$("#exampleFormControlSelect1").val()]);
            } else {
                console.error('No cameras found.');
            }
        }).catch(function (e) {
            camerasButtons.innerHTML = '<a class="dropdown-item disabled" href="#">Error al cargar camara</a>'
            console.error(e);
        });

        scanner.addListener('scan', function (content) {
            setValueInput(content);
            document.getElementById("p1").innerHTML = content;
            console.log(content);
            qrLectorClose.click();
        });
    });

    //Al cambiar el ComboBox cambiar la camara si esta disponible
    $("#exampleFormControlSelect1").change(function(){
        Instascan.Camera.getCameras().then(function (cameras) {
            if (cameras.length > 0) {
                scanner.start(cameras[$("#exampleFormControlSelect1").val()]);
            } else {
                console.error('No cameras found.');
            }
        }).catch(function (e) {
            camerasButtons.innerHTML = '<a class="dropdown-item disabled" href="#">Error al cargar camara</a>'
            console.error(e);
        });

        scanner.addListener('scan', function (content) {
            setValueInput(content);
            document.getElementById("p1").innerHTML = content;
            console.log(content);
            qrLectorClose.click();
        });
    });


    //Al cerrar la camara la detiene - Optimizacion de procesador
    qrLectorClose.addEventListener('click', function () {
        closeScanner()
    });

});

