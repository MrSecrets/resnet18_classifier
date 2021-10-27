document.addEventListener('DOMContentLoaded', function(){
    document.getElementById("imageForm").onclick=function(){
        
        img.onchange = evt => {
            const [file] = img.files
            $('#resultField').val('YOLO');
            if (file) {
              blah.src = URL.createObjectURL(file)
            }
          }
               
        $.ajax(
                {
                    url : '/add_image' ,
                    method : 'POST' ,
                    data : new FormData(imageForm) ,
                    processData: false,
                    contentType: false,
                    success: function(json){
                        alert(json);
                        $('#imageForm').val('');
                        console.log(json);
                        // $('#resultField').val(''); 
                        $('#resultField').replaceWith("Classifier Online");
                    },
                    
                    error: function(){
                        alert('Classification failed')},
                }
            )

    }

    document.getElementById("showImages").onclick=function(){
        $.ajax(
            {
                url : '/get_images' ,
                method : 'GET' ,
                success : function(data){
                    imageField=document.querySelector("#imageField")
                        for(let i=0;i<data.image_urls.length;i++){
                            imageField.appendChild(CreateImage(data.image_urls[i]))
                        }
                }

            }
        )
        
    }
    function CreateImage(src)
    {
        let img = document.createElement("img")
        img.src =src
        img.className="imageSize"
        return img
    }
   
})


