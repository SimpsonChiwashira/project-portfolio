<?php 
session_start();

// Check if the user is already logged in, if yes then redirect him to welcome page
if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
  header("location: admin/manage_users.php");
  exit;
}
require_once "config.php";
$username = $password="";
$username_err = $password_err = "";
 
// Processing form data when form is submitted
if($_SERVER["REQUEST_METHOD"] == "POST"){
 
    // Check if username is empty
    if(empty(trim($_POST["username"]))){
        $username_err = "Please enter email address.";
    } else{
        $username = trim($_POST["username"]);
    }
    
    // Check if password is empty
    if(empty(trim($_POST["password"]))){
        $password_err = "Please enter your password.";
    } else{
        $password = trim($_POST["password"]);
    }
    
    // Validate credentials
    if(empty($username_err) && empty($password_err)){
        // Prepare a select statement
        $sql = "SELECT id, username, passwordd FROM users WHERE username = ?";
        
        if($stmt = mysqli_prepare($db, $sql)){
            // Bind variables to the prepared statement as parameters
            mysqli_stmt_bind_param($stmt, "s", $param_username);
            
            // Set parameters
            $param_username = $username;
            
            // Attempt to execute the prepared statement
            if(mysqli_stmt_execute($stmt)){
                // Store result
                mysqli_stmt_store_result($stmt);
                
                // Check if username exists, if yes then verify password
                if(mysqli_stmt_num_rows($stmt) == 1){                    
                    // Bind result variables
                    mysqli_stmt_bind_result($stmt, $id, $username, $hashed_password);
                    if(mysqli_stmt_fetch($stmt)){
                        if(password_verify($password, $hashed_password)){
                            // Password is correct, so start a new session
                            session_start();
                            
                            
                            // Store data in session variables
                            $_SESSION["loggedin"] = true;
                            $_SESSION["id"] = $id;
                            $_SESSION["username"] = $username;                            
                            
                            // Redirect user to welcome page
                            header("location: admin/manage_users.php");
                        } else{
                            // Display an error message if password is not valid
                            $password_err = "The password you entered was not valid.";
                        }
                    }
                } else{
                    // Display an error message if username doesn't exist
                    $username_err = "No account found with that username.";
                }
            } else{
                echo "Oops! Something went wrong. Please try again later.";
            }
        }
        
        // Close statement
        mysqli_stmt_close($stmt);
    }
    
    // Close connection
    mysqli_close($db);
}
?>

    <head>
        <meta charset="utf-8">
    <title>Login</title>
    <link rel="stylesheet" type="text/css" href="login.css">
</head>
<body>
    <form id="frm" class="box"  method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
       <centre> <h1>Login</h1> </centre>
        <input type="email" name="username" value="<?php echo $username;?>" placeholder="ENTER USERNAME">
        <input type="password" name="password" value="<?php echo $password;?>"required  placeholder="ENTER PASSWORD">
        <input type="submit" name="" value="Sign-In" id="btn">
        <h4>Do you have an Account?<a href="register.php">Sign Up here</a><h4> 
      </form>  
       <!--
    <Center>
    <h1><b>Enter Your Login Details Here</b></h1>
      <hr>
    <form id="frm" method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
        <table>
        <tr>
        <td>E-Mail</td>
        <td><input type="email" name="email"value="<?php echo $email;?>"placeholder="123@example.com"required></td>
        </tr>
        <tr>
        <td>Password</td>
        <td><input type="password" name="password"value="<?php echo $password;?>"required></td>
         </tr>  

        </table>
        <input type="submit"value="Login"id="btn">
        <h4>Does not have an Account?<a href="registration.php">Sign Up here</a><h4>
    </form>-->
    </body>
</html>