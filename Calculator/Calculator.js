const campo1 = document.querySelector('#campo1');
const campo2 = document.querySelector('#campo2');
const seletor = document.querySelector('#operacao');
let resposta = document.querySelector('#resposta');

seletor.addEventListener("change", calcular);
campo1.addEventListener("keyup", calcular);
campo2.addEventListener("keyup", calcular);

function calcular() {
    if (campo1.value !== '' && campo2.value !== '') {
        const valor1 = parseInt(campo1.value);
        const valor2 = parseInt(campo2.value);

        if (isNaN(valor1) || isNaN(valor2)) {
            resposta.innerHTML = 'Por favor, insira um número válido';
            return;
        }

        const operacao = seletor.value;
        if (operacao === '+')
            resposta.innerHTML = valor1 + valor2;
        if (operacao === '-')
            resposta.innerHTML = valor1 - valor2;
        if (operacao === '*')
            resposta.innerHTML = valor1 * valor2;
        if (operacao === '/')
            resposta.innerHTML = valor1 / valor2;
    } else {
        resposta.innerHTML = '';
    }
}