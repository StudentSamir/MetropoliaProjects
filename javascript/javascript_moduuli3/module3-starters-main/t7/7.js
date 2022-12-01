'use strict'

const trigger = document.querySelector('#trigger');
const kuva = document.querySelector('#target');

trigger.addEventListener('mouseover', function event(evt){
    kuva.src = 'img/picB.jpg'

});
trigger.addEventListener('mouseout', function event(evt){
    kuva.src = 'img/picA.jpg'
});
