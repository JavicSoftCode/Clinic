document.addEventListener("DOMContentLoaded", () => {
    const cloud = document.getElementById("cloud");
    const barraLateral = document.querySelector(".barra-lateral");
    const spans = document.querySelectorAll("span");
    const palanca = document.querySelector(".switch");
    const circulo = document.querySelector(".circulo");
    const menu = document.querySelector(".menu");
    const main = document.querySelector("main");

    function toggleMiniBarraLateral() {
        barraLateral.classList.toggle("mini-barra-lateral");
        main.classList.toggle("min-main");
        spans.forEach(span => {
            span.classList.toggle("oculto");
        });
    }

    menu.addEventListener("click", () => {
        barraLateral.classList.toggle("max-barra-lateral");
        if (barraLateral.classList.contains("max-barra-lateral")) {
            menu.children[0].style.display = "none";
            menu.children[1].style.display = "block";
        } else {
            menu.children[0].style.display = "block";
            menu.children[1].style.display = "none";
        }
        if (window.innerWidth <= 320) {
            toggleMiniBarraLateral();
        }
    });

    palanca.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");
        circulo.classList.toggle("prendido");
    });

    cloud.addEventListener("click", toggleMiniBarraLateral);
});

document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.getElementById('Canvasimg');
    const context = canvas.getContext('2d');
    const imagenBase64 = localStorage.getItem('imagenDefondo');

    if (imagenBase64) {
        // Si la imagen está en localStorage, cargarla desde allí
        const img = new Image();
        img.onload = function () {
            context.drawImage(img, 0, 0, canvas.width, canvas.height);
        };
        img.src = imagenBase64;
    } else {
        // Si la imagen no está en localStorage, cargarla desde el servidor
        const img = new Image();
        img.onload = function () {
            context.drawImage(img, 0, 0, canvas.width, canvas.height);
            // Convertir la imagen a Base64 y guardarla en localStorage
            const dataURL = canvas.toDataURL('image/png');
            localStorage.setItem('imagenDefondo', dataURL);
        };
        img.src = 'public/clinic/img-dashboard-clinic.jpg'; // Ruta de la imagen de fondo
    }


    const canvass = document.getElementById('CanvasIMG');
    const contextt = canvass.getContext('2d');
    const imagenBase644 = localStorage.getItem('imagenDeFondo');

    if (imagenBase644) {
        // Si la imagen está en localStorage, cargarla desde allí
        const img = new Image();
        img.onload = function () {
            contextt.drawImage(img, 0, 0, canvass.width, canvass.height);
        };
        img.src = imagenBase644;
    } else {
        // Si la imagen no está en localStorage, cargarla desde el servidor
        const img = new Image();
        img.onload = function () {
            contextt.drawImage(img, 0, 0, canvass.width, canvass.height);
            // Convertir la imagen a Base64 y guardarla en localStorage
            const dataURL = canvass.toDataURL('image/png');
            localStorage.setItem('imagenDeFondo', dataURL);
        };
        img.src = 'public/clinic/img-dashboard-clinic.jpg'; // Ruta de la imagen de fondo
    }
});