 $(function() {
     $('#btnSignUp').click(function() {
         alert("A");
         $.ajax({
             url: '/Authenticate',
             data: $('form').serialize(),
             success: function(response) {
                 console.log(response);
             },
             error: function(error) {
                 console.log(error);
             }
         });
         alert("B");
     });
 });