function display() {
  var twitterHandle = document.getElementById("TwitterHandle").value;
  if(twitterHandle != null) {
    document.getElementById("demo").innerHTML = "Searching for " + twitterHandle;
    document.getElementById("form").style.display = 'none';
  } else {
    document.getElementById("demo").innerHTML = "oh ok";
  }
}
