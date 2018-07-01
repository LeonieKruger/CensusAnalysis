 $(function() {
     $('#btnSaveDetails').click(function() {
                 $.ajax({
                     url: '/SaveDetails',
                     data: $('form').serialize(),
                     success: function(response) {
                         alert("Successfully Saved!");
                         console.log(response);
                     },
                     error: function(error) {
                         alert("Details Save Failed");
                         console.log(error);
                     }
                 });
                   alert("Successfully Uploaded Details!");

    });

 });