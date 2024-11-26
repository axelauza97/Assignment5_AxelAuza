<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Input Form</title>
</head>
<body>
    <h2>Enter a List of Integers</h2>
    <form action="process.php" method="get">
        <label for="integers">Enter integers separated by commas:</label>
        <input type="text" id="integers" name="integers" required><br><br>
        <label for="threshold">Enter threshold:</label>
        <input type="text" id="threshold" name="threshold" required><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>