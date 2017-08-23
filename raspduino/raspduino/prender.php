<?php
echo "<h2>Prendiendo LED</h2>";
$prende = exec('sudo python enciendeled.py');

echo $prende;



header('Location:index.html');

?>
