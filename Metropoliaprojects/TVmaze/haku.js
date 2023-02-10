'use strict';
const lomake = document.querySelector('form');
const apiURL = 'https://api.tvmaze.com/search/shows';

async function fetchJson(url, options = {}) {
    const vastaus = await fetch(url, options);
    if (!vastaus.ok) {
        throw new Error(vastaus.statusText);
    }
    return await vastaus.json();
}

lomake.addEventListener('submit', async function (evt) {
    try {
        evt.preventDefault();
        const hakusana = document.querySelector('#query').value;
        const sarjat = await fetchJson(apiURL + '?q=' + hakusana);
        console.log(sarjat);
    } catch (e) {
        console.error(e.message);
    }
});









const list = document.querySelector('#action');

  for (let i = 0; i < vastaus.length; i++) {

    const article = document.createElement('article');
    list.appendChild(article);

    const article_title = document.createElement('h2');
    article.appendChild(article_title);

    const article_image = document.createElement('img');
    article.appendChild(article_image)

    const article_link = document.createElement('a');
    article.appendChild(article_link)

    const article_summary = document.createElement('p');
    article.appendChild(article_summary);

    const article_genres = document.createElement('p');
    article.appendChild(article_genres);

      }

  'use strict';

const lomake = document.querySelector('form');
const apiURL = 'https://api.tvmaze.com/search/shows';

const section = document.querySelector('#results');
const defaultMenu = document.querySelector('#default');

async function fetchJson(url, options = {}) {
    const response = await fetch(url, options);
    if (!response.ok) {
        throw new Error(response.statusText);
    }
    return await response.json();
}

lomake.addEventListener('submit', async function (evt) {
    try {
        evt.preventDefault();
        const keyword = document.querySelector('#query').value;
        const series = await fetchJson(apiURL + '?q=' + keyword);
       defaultMenu.remove();

   while (section.lastChild) {
     section.lastChild.remove();
   }


   if (series.length === 0) {
     const noResults = document.createElement('p');
     noResults.classList.add('section');
     noResults.innerHTML = 'No search results found.';
     section.appendChild(noResults);
   }


   for (let show = 0; show < series.length; show++) {

     const article = document.createElement('article');
     section.appendChild(article);

     const link = article.appendChild(document.createElement('a'));

     const header = document.createElement('header');
     article.appendChild(header);

     const figure = document.createElement('figure');
     article.appendChild(figure);

     const image = document.createElement('img');
     figure.appendChild(image);

     const summary = document.createElement('summary');
     figure.appendChild(summary);

     const genres = document.createElement('p');
     article.appendChild(genres)


     article.classList.add('card');
     header.innerText = series[show]['show']['name'];
     summary.innerHTML = series[show]['show']['summary'];

     if (series[show]['show']['image'] != null) {
       image.src = series[show]['show']['image']['medium'];
       image.classList.add('img');
     } else {
       image.src = 'https://via.placeholder.com/210x295/9c9c9c/FFFFFF?text=No+image+found';
       image.classList.add('img');
     }

    for (let i = 0; i < series[show]['show']['genres'].length; i++) {
       if ((i + 1) !== series[show]['show']['genres'].length) {
         genres.innerText += series[show]['show']['genres'][i] + ' | ';
       } else {
         genres.innerText += series[show]['show']['genres'][i];
       }
     }

     //link.setAttribute('target', '_blank');
     //link.innerText = series[show]['show']['url'];
     //link.href = series[show]['show']['url'];

     //iframe.src = series[show]['show']['url'];
     //iframe.classList.add('iframe');

   }
 } catch (e) {
   console.error(e.message);
 }
});








'use strict';

const lomake = document.querySelector('form');
const apiURL = 'https://api.tvmaze.com/search/shows';

const section = document.querySelector('#results');
const defaultMenu = document.querySelector('#default');

async function fetchJson(url, options = {}) {
    const response = await fetch(url, options);
    if (!response.ok) {
        throw new Error(response.statusText);
    }
    return await response.json();
}

lomake.addEventListener('submit', async function (evt) {
    try {
        evt.preventDefault();
        const keyword = document.querySelector('#query').value;
        const series = await fetchJson(apiURL + '?q=' + keyword);
       defaultMenu.remove();

   while (section.lastChild) {
     section.lastChild.remove();
   }


     if (series.length === 0) {
     const noResults = document.createElement('p');
     noResults.classList.add('section');
     noResults.innerHTML = 'No search results found.';
     section.appendChild(noResults);
   }


   for (let show = 0; show < series.length; show++) {

     const article = document.createElement('article');
     section.appendChild(article);

     const header = document.createElement('header');
     article.appendChild(header);

     const figure = document.createElement('figure');
     article.appendChild(figure);

     const image = document.createElement('img');
     figure.appendChild(image);

     const summary = document.createElement('summary');
     figure.appendChild(summary);

     const link = article.appendChild(document.createElement('a'));
     link.setAttribute('target', '_blank');
     link.innerText = series[show]['show']['url'];
     link.href = series[show]['show']['url'];

     const genres = document.createElement('p');
     article.appendChild(genres)


     article.classList.add('card');
     header.innerText = series[show]['show']['name'];
     summary.innerHTML = series[show]['show']['summary'];

     if (series[show]['show']['image'] != null) {
       image.src = series[show]['show']['image']['medium'];
       image.classList.add('img');
     } else {
       image.src = 'https://via.placeholder.com/210x295/9c9c9c/FFFFFF?text=No+image+found';
       image.classList.add('img');
     }

    for (let i = 0; i < series[show]['show']['genres'].length; i++) {
       if ((i + 1) !== series[show]['show']['genres'].length) {
         genres.innerText += series[show]['show']['genres'][i] + ' | ';
       } else {
         genres.innerText += series[show]['show']['genres'][i];
       }
     }

   }

 } catch (e) {
   console.error(e.message);
 }
});
