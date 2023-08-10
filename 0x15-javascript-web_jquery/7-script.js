const filePath = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';


$.ajax({
  url: filePath,
  method: 'GET',
  success: function (character) {
    $('#character').text(character.name)
  }
});
