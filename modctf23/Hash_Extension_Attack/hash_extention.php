<?php
$payload = urldecode($_GET['payload']);
$hash = urldecode($_GET['hash']);

hash('md5',$secret); #5ebe2294ecd0e0f08eab7690d2a6ee69, secret length 6.

if (false !== strpos($payload,"admin") && hash('md5',$secret.$payload) == $hash){
	echo "same hash!!\n";
	# flag is $hash:$payload.
}else{
	echo "wrong hash!!\n";
}
?>
