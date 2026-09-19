<html>
<body>
Hello this is an email test!
</body>
</html>
<?php 
$to = $subject = $message = "";
;

$to = "taperabrian0142@gmail.com";
$subject = "Account Created";
$message = "Dear Mr Chiwashira. Your Account has been activated and the details of the are as follows: Login ID: , Password: "; 

mail($to, $subject, $message)
?>
