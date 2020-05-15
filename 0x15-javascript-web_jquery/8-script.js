$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      for (const el of data.results) {
        const item = '<li>' + el.title + '</li>';
        $('UL#list_movies').append(item);
      }
    }
  });
});
