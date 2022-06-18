<?php
$name = $_POST['name'];
$email = $_POST['email'];
$phone = $_POST['phone'];
$message =$_POST['message'];

$formcontent=" From: $name \n Email: $email \n Phone: $phone  \n  Message: $message";
$recipient = "hello@shopfins.com";
$subject = "Get In Touch";
$mailheader = "From: $email \r\n";
mail($recipient, $subject, $formcontent, $mailheader) or die("Error!");
echo "Thank you for submitting form, our executive will get in touch with you shortly." . "<br>" . "<a href='index.html' style='text-decoration:none;color:#ff0099;'> Return Home</a>";


?>



