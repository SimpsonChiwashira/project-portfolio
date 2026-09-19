<?php
// Initialize the session
session_start();
 
// Check if the user is logged in, if not then redirect him to login page
if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
    header("location: clientlogin.php");
    exit;
}
?>
<!doctype html>
<html lang="en">
  <head>
  	<title>Rose Bank Customer Portal</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900" rel="stylesheet">
		
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
		<link rel="stylesheet" href="css/style.css">
  </head>
  <body>
		
		<div class="wrapper d-flex align-items-stretch">
			<nav id="sidebar">
				<div class="custom-menu">
					<button type="button" id="sidebarCollapse" class="btn btn-primary">
	          <i class="fa fa-bars"></i>
	          <span class="sr-only">Toggle Menu</span>
	        </button>
        </div>
	  		<h1><a href="clienthome.php" class="logo">Rose Bank</a></h1>
        <ul class="list-unstyled components mb-5">
          <li class="active">
            <a href="clienthome.php"><span class="fa fa-home mr-3"></span> Home</a>
          </li>
          <li>
              <a href="profile.php"><span class="fa fa-user mr-3"></span> Profile</a>
          </li>
          <li>
            <a href="current_balance.php"><span class="fa fa-sticky-note mr-3"></span> Current Balance</a>
          </li>
          <li>
            <a href="appointment.php"><span class="fa fa-sticky-note mr-3"></span> Book Appointment</a>
          </li>
          <li>
            <a href="change_password.php"><span class="fa fa-paper-plane mr-3"></span> Change Password</a>
          </li>
          <li>
            <a href="logout.php"><span class="fa fa-paper-plane mr-3"></span> Logout</a>
          </li>
        </ul>    
    	</nav>
        <?php
        require_once "server1.php";
        $name = $surname = $idnumber = $address = $number = "";
        $user=$_SESSION['email'];
        $sql = "SELECT first_name, last_name, idnum, full_address, mobile_number  FROM customer_users WHERE email= '$user'";

        if($result = mysqli_query($db, $sql)){

        	if(mysqli_num_rows($result)>0){
		

		        while($row = mysqli_fetch_assoc($result)){
		
                    $name = $row['first_name'];
                    $surname = $row['last_name'];
                    $idnumber = $row['idnum'];
                    $address = $row['full_address'];
                    $number = $row['mobile_number'];

                    
	}
    mysqli_free_result($result);
}
}
?> 
        <!-- Page Content  -->
      <div id="content" class="p-4 p-md-5 pt-5">
        <h2 class="mb-4">Your Profile </h2>
  <style>
	#leftbox{ float:left;
		    	  width:25%;
			      height: 280px;
			    }
	#rightbox{  float: left;
			        width: 55%;
			        height: 280px;
			      }			
</style>

<div id="boxes">
<div id="leftbox">
	<img src="user.png" width="150" height="150">
        	
</div>

<div id="rightbox">
	<form>
		<table>
			<tr>
				<td><b>First Name(s):</b></td>
				<td><?php echo "$name"; ?></td>
			</tr>
			<tr>
				<td><b>Last Name(s):</b></td>
				<td><?php echo "$surname"; ?></td>
			</tr>
			<tr>
				<td><b>Passport/ID:</b></td>
				<td><?php echo "$idnumber"; ?></td>
			</tr>
			<tr>
				<td><b>E-mail:</b></td>
				<td><?php echo "$user"; ?></td>
			</tr>
			<tr>
				<td><b>Home Address:</b></td>
				<td><?php echo "$address"; ?></td>
			</tr>
			<tr>
				<td><b>Mobile Number:</b></td>
				<td><?php echo "$number"; ?></td>
			</tr>
			<tr>
				<td></td>
				<td><p><b>For any updates or changes notify the bank </b><a href="#">+90 533 867 3247</a></p></td>
			</tr>
		</table>
	</form>
</div>
</div>

      </div>
		</div>

    <script src="js/jquery.min.js"></script>
    <script src="js/popper.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/main.js"></script>
  </body>
</html>