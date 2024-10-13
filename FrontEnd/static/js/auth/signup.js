const canvas = document.getElementById('Canvas');
const ctx = canvas.getContext('2d');
const btnCamera = document.getElementById('btnCamera');
const btnTakePhoto = document.getElementById('btnTakePhoto');
const btnClearCanvas = document.getElementById('btnClearCanvas');

let videoStream = null;
let videoElement = null;

// Mostrar imagen predeterminada
window.onload = function () {
    const defaultImageUrl = "{{ default_image_url }}";
    const image = new Image();
    image.src = defaultImageUrl;
    image.onload = function () {
        drawImageToCanvas(image);
    }
};

// Subir imagen y mostrarla en el canvas
document.getElementById('{{ form.image.id_for_label }}').addEventListener('change', function (event) {
    const file = event.target.files[0];
    if (!file) return; // Asegurarse de que hay un archivo

    const reader = new FileReader();
    reader.onload = function () {
        const image = new Image();
        image.src = reader.result;
        image.onload = function () {
            drawImageToCanvas(image);
        }
    };
    reader.readAsDataURL(file);
});

// Función para dibujar imagen en el canvas
function drawImageToCanvas(image) {
    canvas.width = 180;
    canvas.height = 180;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const scale = Math.min(canvas.width / image.width, canvas.height / image.height);
    const x = (canvas.width / 2) - (image.width / 2) * scale;
    const y = (canvas.height / 2) - (image.height / 2) * scale;
    ctx.drawImage(image, x, y, image.width * scale, image.height * scale);
    btnClearCanvas.style.display = 'block';
}

// Activar cámara
btnCamera.addEventListener('click', async () => {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        videoStream = await navigator.mediaDevices.getUserMedia({video: true});
        videoElement = document.createElement('video');
        videoElement.srcObject = videoStream;
         videoElement.play();
        videoElement.onloadedmetadata = function () {
            canvas.width = 180;
            canvas.height = 180;
            updateCanvas();
            btnTakePhoto.style.display = 'block';
        };
    }
});

function updateCanvas() {
    if (videoElement && videoElement.srcObject) {
        ctx.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
        requestAnimationFrame(updateCanvas);
    }
}

// Tomar foto y mostrarla en el canvas
btnTakePhoto.addEventListener('click', () => {
    ctx.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
    btnTakePhoto.style.display = 'none';
    btnClearCanvas.style.display = 'block';
    if (videoStream) {
        videoStream.getTracks().forEach(track => track.stop());
        videoStream = null;
        videoElement.srcObject = null;
    }
});

// Limpiar el canvas
btnClearCanvas.addEventListener('click', () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    btnClearCanvas.style.display = 'none';
    // Restablecer el input para que permita volver a subir la misma imagen
    document.getElementById('{{ form.image.id_for_label }}').value = '';
});