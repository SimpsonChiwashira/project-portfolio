<!doctype html>
<html lang="en">
  <head>
  	<title>Rose Bank Teller Portal</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900" rel="stylesheet">
		
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
		<link rel="stylesheet" href="css/style.css">
  </head>
  <body>
		
		<div class="wrapper d-flex align-items-stretch">
			<nav id="sidebar">
				<div class="p-4 pt-5">
		  		<a href="#" class="img logo rounded-circle mb-5" style="background-image: url(images/user.png);"></a>
	        <ul class="list-unstyled components mb-5">
	          <li class="active">
	            <a href="#homeSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">Home</a>
	            <ul class="collapse list-unstyled" id="homeSubmenu">
                <li>
                    <a href="manage_users.php">Manage users</a>
                </li>
                <li>
                    <a href="manage_customer/index.php">Manage Customers</a>
                </li>
                <li>
                    <a href="customercare.php">Customer Enquiries</a>
                </li>
	            </ul>
	          </li>
	          <li>
	              <a href="about.php">About</a>
	          </li>
	          <li>
              <a href="#pageSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">Customers</a>
              <ul class="collapse list-unstyled" id="pageSubmenu">
                <li>
                    <a href="appoint.php">Appointments</a>
                </li>
                <li>
                    <a href="clientreg.php">Add New customers</a>
                </li>
                <li>
                    <a href="remove.php">Delete Customers</a>
                </li>
              </ul>
	          </li>
	          <li>
              <a href="customercare.php">Customer Care</a>
	          </li>
	          <li>
              <a href="logout.php">Logout</a>
	          </li>
	        </ul>

	        <div class="footer">
	        	<p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
						  Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | <i class="icon-heart" aria-hidden="true"></i> by <a href="" target="_blank">Rose Bank</a>
						  <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
	        </div>

	      </div>
    	</nav>

        <!-- Page Content  -->
      <div id="content" class="p-4 p-md-5">

        <nav class="navbar navbar-expand-lg navbar-light bg-light">
          <div class="container-fluid">

            <button type="button" id="sidebarCollapse" class="btn btn-primary">
              <i class="fa fa-bars"></i>
              <span class="sr-only">Toggle Menu</span>
            </button>
            <button class="btn btn-dark d-inline-block d-lg-none ml-auto" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <i class="fa fa-bars"></i>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="nav navbar-nav ml-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="adminhome.php">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="about.php">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="customercare.php">Customer Care</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="logout.php">Logout</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <h2 class="mb-4">Remove Appointment</h2>
        <form action= "appremove.php"method="post">
           <input type="email" name="email" placeholder="Username or Email Registered by user" required>
           <input type="submit" name="submit" value="Search">
        </form><br>
        <?php
require_once "server1.php";
//Deposit
// this query allows me to select information in the database and search for it to be abole to continue with the transaction
$email = "";
if(isset($_POST['submit'])){
$email = mysqli_real_escape_string($db, $_POST['email']);
}

$sql = "SELECT branch, transaction_type,id_number, first_name, last_name,full_address, mobile_number, email, time_stamp FROM appointment WHERE email='$email' LIMIT 1";

if($result = mysqli_query($db, $sql)){

	if(mysqli_num_rows($result)>0){
		echo "<table border>";	
			echo "<tr>";
			echo "<th>First Name</th>";
			echo "<th>Last Name</th>";
			echo "<th>E-mail</th>";
            echo "<th>Transaction Type</th>";
            echo "<th>Branch</th>";
            echo "<th>ID Number</th>";
            echo "<th>Mobile Number</th>";
            echo "<th>Full Address</th>";
            echo "<th>Appointment Date/Time</th>";
			echo "</tr>";

		while($row = mysqli_fetch_assoc($result)){
			echo "<tr>";
			echo "<td>".$row['first_name']."</td>";
			echo "<td>".$row['last_name']."</td>";
			echo "<td>".$row['email']."</td>";
            echo "<td>".$row['transaction_type']."</td>";
            echo "<td>".$row['branch']."</td>";
            echo "<td>".$row['id_number']."</td>";
            echo "<td>".$row['mobile_number']."</td>";
            echo "<td>".$row['full_address']."</td>";
            echo "<td>".$row['time_stamp']."</td>";
			echo "</tr>";
              }

        echo "</table>";	
    }
    mysqli_free_result($result);
}
?>    
        
                <button border><a href="appdelete.php">Delete Appointment</a></button>

        </div>
		</div>

    <script src="js/jquery.min.js"></script>
    <script src="js/popper.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/main.js"></script>
  </body>
</html>    


