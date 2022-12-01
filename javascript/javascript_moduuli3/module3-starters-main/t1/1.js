'use strict';

let list1;
list1 = ['First Item'];

let list2;
list2 = ['Second Item'];

let list3;
list3 = ['Third Item'];


document.querySelector('#target').innerHTML += `<li> ${list1}</li>`;


document.querySelector('#target').innerHTML += `<li> ${list2}</li>`;

document.querySelector('#target').innerHTML += `<li> ${list3}</li>`;
