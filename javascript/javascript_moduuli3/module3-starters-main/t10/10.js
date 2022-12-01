'use strict';

const form = document.querySelector('input[type="submit"]');
const first = document.querySelector('input[name="firstname"]');
const last = document.querySelector('input[name="lastname"]');

form.addEventListener('click', function (evt) {

    evt.preventDefault();

    document.querySelector('#target').innerHTML = `Your name is ${first.value} ${last.value}`;
});
