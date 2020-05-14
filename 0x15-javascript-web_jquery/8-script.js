$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
  $.each(data.results, function (index, results) {
    $('ul#list_movies').append($('<li></li>').text(results.title));
  });
});
