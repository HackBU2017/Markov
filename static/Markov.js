function display() {
  var twitterHandle = document.getElementById("TwitterHandle").value;
  if(twitterHandle.size >0) {
    document.getElementById("demo").innerHTML = "Searching for " + twitterHandle;
    document.getElementById("form").style.display = 'none';
  } else {
    document.getElementById("demo").innerHTML = "Thinking...";
  }
}

function changeImage() {
  if (document.getElementById("blurred").src == "https://filiph.github.io/markov/images/blurred.jpg")
       {
           document.getElementById("blurred").src = "https://img.clipartfest.com/6810cd52246d25fe6c222b287a6e2f5e_clip-art-of-2d-and-3d-box-shapes-black-and-rectangle-clipart_618-361.jpeg";
       }
       else
       {
           document.getElementById("blurred").src = "https://filiph.github.io/markov/images/blurred.jpg";
       }
   }

  function newImage() {
    if (document.getElementById("centered").src == "https://filiph.github.io/markov/images/ajax-loader.gif")
         {
             document.getElementById("centered").src = "https://upload.wikimedia.org/wikipedia/commons/5/54/Blank_Canvas_on_Transparent_Background.png";
         }
         else
         {
             document.getElementById("centered").src = "https://filiph.github.io/markov/images/ajax-loader.gif";
         }
  }
