<!DOCTYPE html>
<html>
<head>
    <title>Appointment Registration</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="appointment.css">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">


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
    <Center>
        <p>Please enter details required. Please make sure the information entered is <b>correct</b> and we will get back to you at our soonest. Thank you.</p>
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
                    <td>*Transaction Type</td>
                    <td>
                    <select name="trans_type">
                        <option>*Transaction Type</option>
                        <option value="teller">Teller Transaction</option>
                        <option value="retail">Retail Transaction</option>
                        <option value="western union">Western Union</option>
                        <option vlaue="customer">Customer Service</option>
                    </select>
                    </td>        
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
                    <td><input type="email"name="email"required></td><br>
                </tr>
                <tr>
                    <td></td>
                    <td><input type="submit" value="Submit" name="submit"></td>
                </tr>
            </div>
            </table><br>
                  
        </form>
           <!-- <h4>Wish to go back to the home page?Click <a href="index.php"><b><i>here</i></b></a></h4> -->
</body>
        
</html>

<?php
require_once "server1.php";
require_once "errors.php";
// REGISTER USER
$branch = $trans_type = $idnum = $fname = $lname = $address = $mnumber = $email = "";
$errors = array();
if(isset($_POST['submit'])){
// receive all input values from the form
$branch = mysqli_real_escape_string($db, $_POST['branch']);
$trans_type = mysqli_real_escape_string($db, $_POST['trans_type']);
$idnum = mysqli_real_escape_string($db, $_POST['idnum']);
$fname = mysqli_real_escape_string($db, $_POST['fname']);
$lname = mysqli_real_escape_string($db, $_POST['lname']);
$address = mysqli_real_escape_string($db, $_POST['address']);
$mnumber = mysqli_real_escape_string($db, $_POST['mnumber']);
$email = mysqli_real_escape_string($db, $_POST['email']);}
// form validation: ensure that the form is correctly filled ...
// by adding (array_push()) corresponding error unto $errors array
if (!isset($_POST["branch"])) { array_push($errors, "Branch is required"); }
if (!isset($_POST["trans_type"])) { array_push($errors, "Transaction type is required"); }
if (empty($idnum)) { array_push($errors, "Identification or Passport number is required"); }
if (empty($fname)) { array_push($errors, "First name is required"); }
if (empty($lname)) { array_push($errors, "Last name is required"); }
if (empty($address)) { array_push($errors, "Physical Address is required"); }
if (empty($mnumber)) { array_push($errors, "Mobile number is required"); }
if (empty($email)) { array_push($errors, "Email is required"); }

// first check the database to make sure
// a user already requested for an appointment

$user_check_query = "SELECT * FROM appointment WHERE email='$email' LIMIT 1";
$result = mysqli_query($db, $user_check_query);
$user = mysqli_fetch_assoc($result);
if ($user) { // if user exists
if ($user['email'] === $email) {
array_push($errors, "email already requested for an appointment");
}
}
// Finally, register user if there are no errors in the form
if (count($errors) == 0) {

$query = "INSERT INTO appointment(branch, transaction_type, id_number, first_name, last_name, full_address, mobile_number, email)
VALUES('$branch', '$trans_type', '$idnum', '$fname', '$lname', '$address', '$mnumber', '$email')";
mysqli_query($db, $query);
$_SESSION['email'] = $email;
$_SESSION['success'] = "You are now logged in";
//header('location: submission.php');
}

?>