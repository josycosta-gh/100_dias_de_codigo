let box = documento.querySelector('.box');
let input = documento.querySelector('input');

input.addEventListener('input', () => {
    box.style.borderRadius = input.value;
    box.style.background = input.value;
})