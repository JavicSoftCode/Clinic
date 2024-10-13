// document.addEventListener('DOMContentLoaded', function () {
//     const canvas = document.getElementById('CanvasIMG');
//     const context = canvas.getContext('2d');
//     const imagenBase64 = localStorage.getItem('imagenDeFondo');
//
//     if (imagenBase64) {
//         // Si la imagen está en localStorage, cargarla desde allí
//         const img = new Image();
//         img.onload = function () {
//             context.drawImage(img, 0, 0, canvas.width, canvas.height);
//         };
//         img.src = imagenBase64;
//     } else {
//         // Si la imagen no está en localStorage, cargarla desde el servidor
//         const img = new Image();
//         img.onload = function () {
//             context.drawImage(img, 0, 0, canvas.width, canvas.height);
//             // Convertir la imagen a Base64 y guardarla en localStorage
//             const dataURL = canvas.toDataURL('image/png');
//             localStorage.setItem('imagenDeFondo', dataURL);
//         };
//         img.src = 'public/clinic/img-dashboard-clinic.jpg'; // Ruta de la imagen de fondo
//     }
// });