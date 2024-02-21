const btnStart = document.getElementById('btnStart');
const btnStop = document.getElementById('btnStop');
const textArea = document.getElementById('textArea');

const reconocimientoVoz = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new reconocimientoVoz();

recognition.continuous = true;
recognition.lang = 'es-ES';
recognition.interimResult = false;

btnStart.addEventListener('click', () => {
    recognition.start();
});

btnStop.addEventListener('click', () => {
    recognition.abort();
});

recognition.onresult = (event) => {
    const texto = event.results[event.results.length - 1][0].transcript;
    console.log(texto);
    textArea.value = texto;
    leerTexto(texto);
}

function leerTexto(text) {
    const speech = new SpeechSynthesisUtterance(text);
    speech.volume = 1;
    speech.rate = 0.5;
    speech.pitch = 0.4;
    speech.lang = 'es-ES'

    window.speechSynthesis.speak(speech);
}
