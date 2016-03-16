<?php
require_once('TwitterAPIExchange.php');

//put here your credentials
$settings = array(
    'oauth_access_token' => "",
    'oauth_access_token_secret' => "",
    'consumer_key' => "",
    'consumer_secret' => ""
);

$url = 'https://api.twitter.com/1.1/statuses/user_timeline.json';
$getfield = '?screen_name=AamAadmiParty&count=200';
$requestMethod = 'GET';


$count=0;

$twitter = new TwitterAPIExchange($settings);
$api_response= $twitter->setGetfield($getfield)
    ->buildOauth($url, $requestMethod)
    ->performRequest();
 $response = json_decode($api_response,true);
//echo $api_response;

$max_id=0;
foreach ($response as $key => $value) {  
echo $value['text']."<br>";
$max_id=$value['id'];
$count=$count+1;
}

//echo $max_id;

for($i=0;$i<15;$i++){

$url = 'https://api.twitter.com/1.1/statuses/user_timeline.json';
$getfield = '?screen_name=AamAadmiParty&max_id='.$max_id.'&count=200';
$requestMethod = 'GET';

$twitter = new TwitterAPIExchange($settings);
$api_response= $twitter->setGetfield($getfield)
    ->buildOauth($url, $requestMethod)
    ->performRequest();
 $response = json_decode($api_response,true);
//echo $api_response;

foreach ($response as $key => $value) {  
echo $value['text']."<br>";
$max_id=$value['id'];
$count=$count+1;
}

}




?>
