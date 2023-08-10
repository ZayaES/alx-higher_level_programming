const togHead = $('#toggle_header');
const header = $('header');
togHead.click(function () {
  header.toggleClass(['green', 'red']);
});
