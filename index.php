<?php
$file = 'keys.txt';

if (isset($_GET['key'])) {
    $key = $_GET['key'];
    file_put_contents($file, $key . "\n", FILE_APPEND);
    echo "Access token stored successfully!";
} elseif (isset($_GET['accesskey'])) {
    $accessKey = $_GET['accesskey'];
    $keys = file($file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    if (in_array($accessKey, $keys)) {
        echo "Working";
    } else {
        echo "Access token is missing or invalid";
    }
} else {
    echo "Access token is missing or invalid";
}
?>
