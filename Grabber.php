<?php
session_start();
require_once("twitteroauth/twitteroauth/twitteroauth.php"); //Path to twitteroauth library you downloaded in step 3

$twitteruser = "twitterusername"; //user name you want to reference
$notweets = 30; //how many tweets you want to retrieve
$consumerkey = "BQRfMJOhdiARaRBwlOpo78ktp"; //Noted keys from step 2
$consumersecret = "RxF8PngRe44jVMQDUdunfTy9KLRCqbp9NKFYX3fuHFkx2MvsHX"; //Noted keys from step 2
$accesstoken = "2498510321-AC9ycNnMzoug1iniU544RvceQkRNQxOS25qdaTr"; //Noted keys from step 2
$accesstokensecret = "5odRjLJdgntK0mffliAbIARphkqDyPrJ0UjqeUMI9bmo7"; //Noted keys from step 2

function getConnectionWithAccessToken($cons_key, $cons_secret, $oauth_token, $oauth_token_secret) {
  $connection = new TwitterOAuth($cons_key, $cons_secret, $oauth_token, $oauth_token_secret);
  return $connection;
}

$connection = getConnectionWithAccessToken($consumerkey, $consumersecret, $accesstoken, $accesstokensecret);

$tweets = $connection->get("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=".$twitteruser."&count=".$notweets);

echo json_encode($tweets);
echo $tweets; //testing remove for production   
?>