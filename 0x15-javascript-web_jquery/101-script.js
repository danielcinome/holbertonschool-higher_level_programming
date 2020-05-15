document.addEventListener('DOMContentLoaded', function () {
  $('#add_item').on('click', function (eventAdd) {
    $('ul.my_list').add('<li>Item</li>').appendTo('ul.my_list');
  });
  $('#remove_item').on('click', function (eventRemove) {
    $('ul li:last-child').remove();
  });
  $('#clear_list').on('click', function (eventRemove) {
    $('ul.my_list').empty();
  });
});
