<?php
 /*capturo el celular del input desde el html*/
$celular = $_POST['celular'];
echo $celular
$msg = exec("sudo python enviar_msg.py'".$celular"'");
echo $msg;

header('Location:index.html');

?>