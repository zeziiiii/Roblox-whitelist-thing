<?php
if (isset($_GET['key'])) {
    $key = $_GET['key'];
    file_put_contents('keys.txt', $key . "\n", FILE_APPEND);
    echo "Working";
} elseif (isset($_GET['accesskey'])) {
    $accessKey = $_GET['accesskey'];
    $keys = file('keys.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    if (in_array($accessKey, $keys)) {
        echo "Working";
    } else {
        echo "No valid haha";
    }
} else {
    echo "No valid haha";
}
?>