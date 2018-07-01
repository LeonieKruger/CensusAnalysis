 $(function() {
     $('#btnSignUp').click(function() {
         alert("A");
         $.ajax({
             url: '/Authenticate',
             data: $('form').serialize(),
             success: function(response) {
                 alert("Successfully Registered!");
                 console.log(response);
             },
             error: function(error) {
                 alert("Registration Failed");
                 console.log(error);
             }
         });
           alert("Successfully Registered!");

     });
 });