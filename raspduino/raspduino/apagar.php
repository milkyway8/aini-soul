<?php
echo "<h2>Apagando LED</h2>";
$apaga = exec('sudo python apagaled.py');

echo $apaga;


header('Location:index.html');

?>
