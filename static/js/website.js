function readURL(input) {
    if (input.files && input.files[0]) {
  
      var reader = new FileReader();
  
      reader.onload = function(e) {
        $('.image-upload-wrap').hide();
  
        $('.file-upload-image').attr('src', e.target.result);
        $('.file-upload-content').show();
  
        $('.image-title').html(input.files[0].name);
      };
      
      reader.readAsDataURL(input.files[0]);
      alert("oops");
      console.log(reader.result);
      var lol = input.files[0];
      var b64 = reader.result.split("base64,")[1];
      
      $.ajax({
        url : 'image2classify/',
        type: 'POST',
        data: b64,
        contentType: false,
        processData: false,
        cache: false,
        success: function(){alert('it works');
      console.log(input.files[0].name)},
        error: function(){alert("Nah");
        console.log(b64)},
      });
    } else {
      removeUpload();
    }
  }
  
function removeUpload() {
    $('.file-upload-input').replaceWith($('.file-upload-input').clone());
    $('.file-upload-content').hide();
    $('.image-upload-wrap').show();
  }
  $('.image-upload-wrap').bind('dragover', function () {
          $('.image-upload-wrap').addClass('image-dropping');
      });
      $('.image-upload-wrap').bind('dragleave', function () {
          $('.image-upload-wrap').removeClass('image-dropping');
  });
  
  function imageloader(callBack){
    var input = $('#photo');
    var file = input.prop('files')[0];
    var reader = new FileReader();
    reader.onload = function(){
        callBack(reader.result);
    
     };
    reader.readAsDataURL(file);
    
    $('#edit_form').submit(function (eve) {
        eve.preventDefault();
        var form = $.toJSON($(this).serializeArray());
        imageloader(function(image){
            var image_data = $.toJSON(image);
            sender(form,image_data);
        });
    });
  }