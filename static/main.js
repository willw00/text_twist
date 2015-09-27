$(document).ready(function() {
  console.log("ready!");

  // on form submission ...
  $('#new').on('submit', function() {
    console.log("the form has beeen submitted");
    console.log(valueOne, valueTwo)
    $.ajax({
      type: "POST",
      url: "/",
      success: function(results) {
        console.log(results.subs);
        $('#results').html(results.total)
        $('input').val('')
      },
      error: function(error) {
        console.log(error)
      }
    });
  });

});