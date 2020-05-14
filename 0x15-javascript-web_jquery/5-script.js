$('#add_item').on('click', function (event) {
  $('ul.my_list').add('<li>Item</li>').appendTo('ul.my_list');
});
