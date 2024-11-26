<?php
    if ($_SERVER["REQUEST_METHOD"] == "GET") {
        $integers = escapeshellarg($_GET['integers']);
        $threshold = escapeshellarg($_GET['threshold']);
        
        // Execute Python script with passed arguments
        $command = escapeshellcmd("python3 /var/www/html/bitwise_operations.py $integers $threshold");
        $output = shell_exec($command);
        
        // Display Python script output
        echo $output;
    }
?>