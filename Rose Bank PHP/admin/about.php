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
          <style>
              #leftbox{ float:left;
                        width:25%;
                        height:280px;
                      }
              #rightbox{ float:left;
                         width:60%;
                         height:280px; 
                      }
          </style>
        <div id="boxes"> 
        <h2 class="mb-4">About Rose Bank</h2>
        <div id="leftbox">
        <img src="juanita.jpeg" width="220" height="250">
        <h3>Meet Our Director</h3>
        <p>Juanita Jidai Mamza</p>
        <p>Email: mamzajuanita@rosebank.com</p>
        </div>
        <div id="rightbox"> 
        <p>Rose Bank is one of the new modern banks ever made. With low interest rates on loans it has gone to be one of the most widely used bank by the customers. It is a bank you can highly rely on because we offer the best services for all indivduals at out disposal. Get in touch with us at our nearest branch and start banking with us</p>
        <p></p>
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