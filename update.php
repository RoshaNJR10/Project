<form method="POST" action="#">
	identify field:<input type="text" name="ifield"><br><br>
	identify value:<input type="text" name="ivalue"><br><br>
	field to be change:<input type="text" name="cfield"><br><br>
	new value:<input type="text" name="cvalue"><br><br>
	<input type="submit" name="update" value="update">

</form>
<?php
if(isset($_POST['update'])){
	include('connection.php');
	$if=$_POST['ifield'];
	$iv=$_POST['ivalue'];
	$cf=$_POST['cfield'];
	
	$cv=$_POST['cvalue'];

	$up="UPDATE `student` SET `$cf`='$cv' WHERE `$if`='$iv'";

	$res=mysqli_query($conn,$up);
	if ($res) {
		echo "<script>alert('update success');</script>";
	}
}

?>