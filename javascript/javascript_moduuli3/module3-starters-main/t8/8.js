'use strict';

let select = document.querySelector('#operation');
let p = document.querySelector('#result');

function calculator() {
    let num1 = document.querySelector('#num1').value;
    let num2 = document.querySelector('#num2').value;

    if (select.value === 'add') {
        p.innerHTML = (parseInt(num1) + parseInt(num2));
    } else if (select.value === 'sub') {
        p.innerHTML = (parseInt(num1) - parseInt(num2));
    } else if (select.value === 'multi') {
        p.innerHTML = (parseInt(num1) * parseInt(num2));
    } else if (select.value === 'div') {
        p.innerHTML = (parseInt(num1) / parseInt(num2));
    }
}

const calculate = document.querySelector('#start');
calculate.addEventListener('click', calculator);
