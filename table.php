<?php
	$host="localhost";
	$user="root";
	$pass="";
	$db="nist";
	$conn=mysqli_connect("$host",$user,$pass,$db);


$f=$_POST['field'];
$v=$_POST['value'];



?>
<table width="40%" border="1">
	<tr>
		<td>name</td>
		<td>roll</td>
		<td>address</td>
		<td>contact</td>
	</tr>


<?php
	$sel="SELECT * FROM `student` WHERE `$f`='$v' ";
	$result=mysqli_query($conn,$sel);
	while($row=mysqli_fetch_assoc($result)){

		echo "<tr><td>".$row['name']."</td>
				<td> ".$row['roll']."</td>
				<td> ".$row['address']."</td>
				<td> ".$row['contact']."</td></tr>";


	}
?> 

</table>

<form method="POST">
	name of the field:<input type="text" name="field"><br><br>
	value of the record:<input type="text" name="value"><br><br>
	<input type="submit" name="sub">
	



</form>