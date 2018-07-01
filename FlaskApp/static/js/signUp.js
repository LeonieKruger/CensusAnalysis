 $(function() {
     $('#btnSignUp').click(function() {
         alert("A");
         $.ajax({
             url: '/Authenticate',
             data: {Name:"leonie",UserName:"leonie",Password:"leonie"},
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