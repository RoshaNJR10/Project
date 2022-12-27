<?php
	$host="localhost";
	$user="root";
	$pass="";
	$db="nist";
	$conn=mysqli_connect($host,$user,$pass,$db);

	$n=$_POST['name'];
	$r=$_POST['roll'];
	$a=$_POST['address'];
	$c=$_POST['contact'];
	$u=$_POST['user'];
	$p=$_POST['pass'];

	$in="INSERT INTO `student` (`id`, `name`, `roll`, `address`, `contact`, `username`, `password`) VALUES (NULL, '$n', '$r', '$a', '$c', '$u', '$p')";
	$result=mysqli_query($conn,$in);
	if($result)
		echo "inserted successfully";
	else
		echo "check your error";

	echo "hello,".$n;
	echo "<br>welcome to our new class";

?>
<table width="40%" border="1">
	<tr>
		<td>S.N</td>
		<td>name</td>
		<td>roll</td>
		<td>address</td>
		<td>contact</td>
	</tr>
	<tr>
		<td>1</td>
		<td><?php echo $n ;?></td>
		<td><?php echo $r;?></td>
		<td><?php echo $a;?></td>
		<td><?php echo $c;?></td>
	</tr>


</table>