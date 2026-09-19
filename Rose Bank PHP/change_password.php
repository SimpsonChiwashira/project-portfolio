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
        $old_pass="";
        $user=$_SESSION['email'];
        $sql = "SELECT passwordd FROM customer_users WHERE email= '$user'";

        if($result = mysqli_query($db, $sql)){

        	if(mysqli_num_rows($result)>0){
		

		        while($row = mysqli_fetch_assoc($result)){
		
                    $old_pass = $row['passwordd'];

                    
	}
    mysqli_free_result($result);
}
}
?> 
        <!-- Page Content  -->
      <div id="content" class="p-4 p-md-5 pt-5">
        <h2 class="mb-4">Change Password </h2>

	<form method="Post" action="change_password.php">
		<table>
			<tr>
				<td><b>Enter Old Password</b></td>
				<td><input type="password" name="old_password" placeholder="Old Password" required></td>
			</tr>
			<tr>
				<td><b>Enter New Password</b></td>
				<td><input type="password" name="new_password" placeholder="New Password" required></td>
			</tr>
			<tr>
				<td><b>Confirm New Password</b></td>
				<td><input type="password" name="confirm_password" placeholder="Confirm Password" required></td>
			</tr>
			<tr>
				<td></td>
				<td><input type="submit" name="submit" value="Change Password"></td>
			</tr>
		</table>
	</form>   
        <?php 
          require_once "server1.php";
          $old_password = $new_password = $confirm_password = $old_harshed = $new_harsh = "";
          if(isset($_POST['submit'])){
            $old_password = mysqli_real_escape_string($db, $_POST['old_password']);
            $new_password = mysqli_real_escape_string($db, $_POST['new_password']);
            $confirm_password = mysqli_real_escape_string($db, $_POST['confirm_password']);
          }  
            $old_harshed = password_hash($old_password, PASSWORD_DEFAULT);
            $new_harsh = password_hash($new_password, PASSWORD_DEFAULT);

          
            
            if($old_harshed !== $old_pass){

           //   echo "<p>PASSWORDS DO NOT MATCH WITH THE OLD ONE</p>";

            }
            if ($new_password !== $confirm_password){
              
             // echo "<p> OLD AND NEW PASSWORD DO NOT MATCH</p>";

            }
              $nquery = "UPDATE customer_users SET passwordd='$new_harsh' WHERE email='$user'";

              $que = mysqli_query($db, $nquery) or die(mysqli_error($db));
        
             //   echo "<p> NEW passowrd has been updated </p>";

      ?>
      </div>
		</div>

    <script src="js/jquery.min.js"></script>
    <script src="js/popper.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/main.js"></script>
  </body>
</html>