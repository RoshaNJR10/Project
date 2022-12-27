<?php
	$host="localhost";
	$user="root";
	$pass="";
	$db="nist";
	$conn=mysqli_connect($host,$user,$pass,$db);
?>
	<table width="40%" border="1">
	<tr>
		<td>name</td>
		<td>roll</td>
		<td>address</td>
		<td>contact</td>
	</tr>
	<tr>
		
<?php
	

	$access="SELECT * FROM `student";
	$result=mysqli_query($conn,$access);
	while ($row=mysqli_fetch_assoc($result)) {
			echo "<td>".$row['name']."</td>
			<td>".$row['roll']."</td>
			<td>".$row['address']."</td>
			<td>".$row['contact']."</td>
		
	</tr>";
		}


	
	?>


</table>