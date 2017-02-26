function display() {
  var twitterHandle = document.getElementById("TwitterHandle").value;
  //console.log(twitterHandle);
  // $.post("/", data={"something":"something else",
  //             "twitter_handle": twitterHandle
  //       }, function(data) {
  //     console.log("pst worked");
  // });
  if(twitterHandle.size >0) {
    document.getElementById("demo").innerHTML = "Searching for " + twitterHandle;
    document.getElementById("form").style.display = 'none';
  } else {
    document.getElementById("demo").innerHTML = "oh ok";
  }

}
