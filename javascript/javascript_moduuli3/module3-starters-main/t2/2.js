'use strict';

let list = document.querySelector('#target');

let list1 = document.createElement('li');
list1.innerHTML = 'First item'
list.appendChild(list1);

let list2 = document.createElement('li');
list2.innerHTML = 'Second item'
list2.setAttribute('class', 'my-item');
list.appendChild(list2);

let list3 = document.createElement('li');
list3.innerHTML = 'Third item'
list.appendChild(list3);
