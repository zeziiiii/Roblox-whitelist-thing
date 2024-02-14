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
        echo "No work";
    }
} elseif (isset($_GET['keydelete'])) {
    $keyToDelete = $_GET['keydelete'];
    $keys = file('keys.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $updatedKeys = array_diff($keys, [$keyToDelete]);
    file_put_contents('keys.txt', implode("\n", $updatedKeys));
    echo "Working";
} else {
    echo "No work";
}
?>
