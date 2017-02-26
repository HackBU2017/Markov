function display() {
  var twitterHandle = prompt("Enter a Twitter Handle");
  if(twitterHandle != null) {
    document.getElementById("demo").innerHTML = "Searching for " + twitterHandle;
    document.getElementById("startbttn").style.display = 'none';
    document.getElementById("ready").style.display = 'block';
  } else {
    document.getElementById("demo").innerHTML = "oh ok";
  }
}
