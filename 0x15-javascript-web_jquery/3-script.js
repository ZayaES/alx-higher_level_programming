const clickRed = $('#red_header'); // selects the red_header id

clickRed.click(function () {
  $('header').addClass('red');
});
