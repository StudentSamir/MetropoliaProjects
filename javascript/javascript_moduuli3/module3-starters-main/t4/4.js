'use strict';

const students = [
    {
        name: 'John',
        id: '2345768',
    },
    {
        name: 'Paul',
        id: '2134657',
    },
    {
        name: 'Jones',
        id: '5423679',
    },
];


const list = document.querySelector('#target');

for (let student of students) {
    const option = document.createElement('option');
    option.innerHTML = student.name;
    option.setAttribute('value', student.id);
    list.appendChild(option);
}
