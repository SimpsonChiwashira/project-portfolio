<!doctype html>
<html lang="en">
  <head>
  	<title>Rose Bank Teller Portal</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900" rel="stylesheet">
		
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
		<link rel="stylesheet" href="css/style.css">
        <style> 
        input[type=submit]{
    display: inline-block;
    background: yellow;
    padding: 0px 50px;
    color: black;
    font-family: "Roboto", sans-serif;
    font-size: 12px;
    font-weight: 500;
    line-height: 48px;
    border: 1px solid #60bc0f;
    border-radius: 0px;
    outline: none !important;
    box-shadow: none !important;
    text-align: center;
    text-transform: uppercase;
    cursor: pointer;
    transition: all 300ms linear 0s;}
</style>  
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
        <Center>
        <p>Please enter details required. Please make sure the information entered is <b>correct</b></p>
        <p><i>*required field</i><p>
        <form  method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
            <table>
            <div class="w3-panel w3-border w3-round-large">
                <tr>
                    <td>*Branch</td>
                    <td>
                    <select name="branch">
                        <option>*Select Branch</option>
                        <option value="norton">Norton, Twinlakes Park</option>
                        <option value="avonlea">Avonlea, Harare</option>
                        <option value="belvedere">Belvedere, Harare</option>
                        <option value="borrowdale">Borrowdale, Harare</option>
                        <option value="rhodesville">Rhodesville, Mutare</option>
                        <option value="gwabalanda">Gwabalanda, Bulawayo</option>
                        <option value="selous">Selous, Chegutu</option>
                        <option value="jameson">Jameson, Kadoma</option>
                        <option value="masvingo">Kyle, Masvingo</option>
                    </select>
                    </td>        
                </tr>
                <tr>
                    <td>*Account Type</td>
                    <td>
                    <select name="acc_type">
                        <option>*Account Type</option>
                        <option value="savings">Savings Account</option>
                        <option value="nostro">Nostro Account</option>
                        <option value="visa">Visa Account</option>
                        <option vlaue="mastercard">Mastercard Account</option>
                    </select>
                    </td>        
                </tr>
                <tr>
                    <td><i>*Account Number</i></td>
                    <td><input type="number"name="acc_num"required></td>
                </tr>
                <tr>
                    <td><i>*Amount Deposited ($)</i></td>
                    <td><input type="number"name="balance"required></td>
                </tr>
                            
                <tr>
                    <td><i>*ID/Passport Number</i></td>
                    <td><input type="text"name="idnum"required></td>
                </tr>
                <tr>
                    <td><i>*First Name(s)</i></td>
                    <td><input type="text"name="fname"required></td>
                </tr>
                <tr>
                    <td><i>*Last Name</i></td>
                    <td><input type="text"name="lname"required></td>
                </tr>
                <tr>
                    <td><i>*Full Address</i></td>
                    <td><input type="text"name="address"required></td>
                </tr>
                <tr>
                    <td><i>*Mobile Number</i></td>
                    <td><input type="text"name="mnumber"required></td>
                </tr>
                <tr>
                    <td><i>*Email</i></td>
                    <td><input type="email"name="email"required></td>
                </tr>
                <tr>
                    <td><i>*Password</i></td>
                    <td><input type="password"name="password_1"required></td>
                </tr>
                <tr>
                    <td><i>*Confirm Password</i></td>
                    <td><input type="password"name="password_2"required></td><br>
                </tr>
                <tr>
                    <td></td>
                    <td><input type="submit" value="Submit" name="submit"></td>
                </tr>
            </div>
            </table><br>         
        </form>
    </div>
		</div>

    <script src="js/jquery.min.js"></script>
    <script src="js/popper.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/main.js"></script>
  </body>
</html>

<?php
require_once "server1.php";
require_once "errors.php";
// REGISTER USER
$branch = $acc_type = $acc_num = $balance = $idnum = $fname = $lname = $address = $mnumber = $email = $password_1 = $password_2 = "";
$errors = array();
$to = $subject = $message ="";
if(isset($_POST['submit'])){
// receive all input values from the form
$branch = mysqli_real_escape_string($db, $_POST['branch']);
$acc_type = mysqli_real_escape_string($db, $_POST['acc_type']);
$acc_num = mysqli_real_escape_string($db, $_POST['acc_num']);
$balance = mysqli_real_escape_string($db, $_POST['balance']);
$idnum = mysqli_real_escape_string($db, $_POST['idnum']);
$fname = mysqli_real_escape_string($db, $_POST['fname']);
$lname = mysqli_real_escape_string($db, $_POST['lname']);
$address = mysqli_real_escape_string($db, $_POST['address']);
$mnumber = mysqli_real_escape_string($db, $_POST['mnumber']);
$email = mysqli_real_escape_string($db, $_POST['email']);
$password_1 = mysqli_real_escape_string($db, $_POST['password_1']);
$password_2 = mysqli_real_escape_string($db, $_POST['password_2']);}
// form validation: ensure that the form is correctly filled ...
// by adding (array_push()) corresponding error unto $errors array
if (!isset($_POST["branch"])) { array_push($errors, "Branch is required"); }
if (!isset($_POST["acc_type"])) { array_push($errors, "Account type is required"); }
if (empty($acc_num)) { array_push($errors, "Account number is required"); }
if (empty($balance)) { array_push($errors, "Balance is required"); }
if (empty($idnum)) { array_push($errors, "Identification or Passport number is required"); }
if (empty($fname)) { array_push($errors, "First name is required"); }
if (empty($lname)) { array_push($errors, "Last name is required"); }
if (empty($address)) { array_push($errors, "Physical Address is required"); }
if (empty($mnumber)) { array_push($errors, "Mobile number is required"); }
if (empty($email)) { array_push($errors, "Email is required"); }
if (empty($password_1)) { array_push($errors, "Password is required"); }
if (empty($password_2)) { array_push($errors, "Password confirmation is required"); }
if ($password_1 != $password_2) {
array_push($errors, "The two passwords do not match");
}
//if(strlen($_POST['password_1']) < 6){array_push($errors, "Password must have at least 6 characters"); }
// first check the database to make sure
// a user does not already exist with the same username and/or email
$user_check_query = "SELECT * FROM customer_users WHERE idnum ='$idnum' OR email='$email' LIMIT 1";
$result = mysqli_query($db, $user_check_query);
$user = mysqli_fetch_assoc($result);
if ($user) { // if user exists
if ($user['idnum'] === $idnum) {
array_push($errors, "user already exists");
}
if ($user['email'] === $email) {
array_push($errors, "email already exists");
}
}
// Finally, register user if there are no errors in the form
if (count($errors) == 0) {
$password = password_hash($password_1, PASSWORD_DEFAULT); //Harsh the password before saving in the database

$query = "INSERT INTO customer_users(branch, account_type, account_number, balance, idnum, first_name, last_name, full_address, mobile_number, email, passwordd)
VALUES('$branch', '$acc_type', '$acc_num', '$balance', '$idnum', '$fname', '$lname', '$address', '$mnumber', '$email', '$password')";
mysqli_query($db, $query);

$to = "$email";
$subject = "Account Created";
$message = "Dear Mr/Mrs $fname $lname. Your Account has been activated and the details of the are as follows: Login ID: $email , Password: $password_1"; 
mail($to, $subject, $message);

$_SESSION['idnum'] = $idnum;
$_SESSION['success'] = "You are now logged in";
//header('location: submission.php');
}

?>