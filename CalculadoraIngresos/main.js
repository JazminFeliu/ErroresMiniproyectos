const pantalla = document.querySelector(".pantalla");
const botones = document.querySelectorAll(".btn");


const acciones = {
    c: () => pantalla.textContent = "0",
    borrar: () => pantalla.textContent = pantalla.textContent.length === 1 || pantalla.textContent === "Error"?"0":pantalla.textContent.slice(0,-1),
    igual: () => pantalla.textContent = pantalla.textContent === "Error" ? "Error":eval(pantalla.textContent),
    default: (botonApretado) => pantalla.textContent = pantalla.textContent === "0" || pantalla.textContent === "Error"? botonApretado : pantalla.textContent + botonApretado
};


botones.forEach(boton => {
    boton.addEventListener("click", () => {
        const botonApretado = boton.textContent;
        (acciones[boton.id] || acciones.default)(botonApretado);
    });
})

