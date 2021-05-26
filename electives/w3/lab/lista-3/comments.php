<link rel="stylesheet" href="css/comments.css" />

<div class="comments">

<p class="header">Comments</p>

<p class="cookies-notice">Please be advised: if you want to comment on this site, you have to login.
    This action involves storing cookies on your device. By signing up, logging in, or commenting
    you’re agreeing to storing and using cookies on your device.</p>

<div class="list">
<?php

include_once "random-string.php";

$SESSIONS_DBA_FILE = "sessions.dba";
$USERS_DBA_FILE = "users.dba";

$COOKIE_KEY_NAME = "session-cookie";
// check if the user is logged in
$cookieKey = $_COOKIE[$COOKIE_KEY_NAME];

$loggedIn = false;
$username = "";
$userStatus = "";

if ($cookieKey) {
    // find the cookie in the sessions file
    $dba = dba_open($SESSIONS_DBA_FILE, "c");
    if (dba_exists($cookieKey, $dba)) {
        // get the associated user
        list($username, $expiry) = explode(":", dba_fetch($cookieKey, $dba), 2);
        $expiry = intval($expiry);
        if ($expiry < time()) {
            $userStatus = "session expired";
            dba_delete($cookieKey, $dba);
        } else {
            $loggedIn = true;
            // refresh the session
            $expiry = time() + 5 * 60;
            dba_replace($cookieKey, $username . ":" . $expiry, $dba);
            setcookie($COOKIE_KEY_NAME, $cookieKey, [
                "expires" => $expiry,
                "path" => "/",
                "httponly" => true
            ]);
        }
    }
    dba_close($dba);
}

// check if the user wants to log in
$u = $_POST["username"];
$p = $_POST["password"];
$t = $_GET["t"];

if ($t) {

    $dba = dba_open($USERS_DBA_FILE, "c");

    if ($t == "login" ) {
        if (dba_exists($u, $dba)) {
            // get the user from the database
            $passwordHash = dba_fetch($u, $dba);
            if (password_verify($p, $passwordHash)) {
                $username = $u;
                $loggedIn = true;

                # generate a random token for this session
                $token = randomString();
                // session expiry is equal to five minutes
                $expiry = time() + 5 * 60;
                # send a cookie to the client
                setcookie($COOKIE_KEY_NAME, $token, [
                    "expires" => $expiry,
                    "path" => "/",
                    "httponly" => true
                ]);
                # save the token in the session database
                dba_close($dba);
                $dba = dba_open($SESSIONS_DBA_FILE, "c");
                dba_insert($token, $username . ":" . $expiry, $dba);
                dba_close($dba);
            } else {
                $userStatus = "invalid password";
            }
        } else {
            $userStatus = "user not found";
        }
    } elseif ($t == "signup") {
        // first, check if user does already exist
        if (!dba_exists($u, $dba)) {
            // sanitise username
            if (preg_match("/[A-z0-9]{4,}/", $u, $matches)) {
                $username = $matches[0];
                // store user’s password
                $passwordHash = password_hash($p, PASSWORD_DEFAULT);
                dba_insert($username, $passwordHash, $dba);
                $userStatus = "signup success";
                dba_close($dba);
            } else {
                $userStatus = "invalid username";
            }
        } else {
            $userStatus = "already exists";
        }
    } else if ($t == "logout" && $loggedIn) {
        dba_close($dba);
        // destroy session
        $dba = dba_open($SESSIONS_DBA_FILE, "c");
        dba_delete($cookieKey, $dba);
        dba_close($dba);
        setcookie($COOKIE_KEY_NAME, null);
        $loggedIn = false;
        $username = "";
        $userStatus = "logout";
    } elseif ($t == "delete-account" && $loggedIn) {
        // overwrite the saved password hash so the user can’t log in
        dba_replace($username, "wrong hash", $dba);
        dba_close($dba);
        // destroy session
        $dba = dba_open($SESSIONS_DBA_FILE, "c");
        dba_delete($cookieKey, $dba);
        dba_close($dba);
        setcookie($COOKIE_KEY_NAME, null);
        $loggedIn = false;
        $username = "";
        $userStatus = "account deleted";
    }

}


$COMMENTS_DBA_FILE = $page . ".dba";
$dba = dba_open($COMMENTS_DBA_FILE, "c");

if ($loggedIn) {
    // if there was a message attached try to add it to the database
    $message = $_POST["message"];
    if ($message != "") {

        // generate a unique key
        $key = time();
        while (dba_exists($key, $dba)) {
            $key = $key + randomString(1);
        }

        // save the comment
        dba_insert($key, $username . ":" . $message, $dba);

    }
}

// now print out all the comments that are in the database
$key = dba_firstkey($dba);
while ($key) {
    list($messageUsername, $messageContents) = explode(":", dba_fetch($key, $dba), 2);
    echo "<div class=message>";
    echo "<p class=username>" . $messageUsername . " says:</p>";
    echo "<p class=contents>" . htmlspecialchars($messageContents) . "</p>";
    echo "</div>";
    $key = dba_nextkey($dba);
}

dba_close($dba);

?>
</div> <!-- div.comments > div.list -->

<?php if ($loggedIn) : ?>
<form class="add-comment" method="post" action="?t=comment">
    <p>Post a comment</p>
    <p class="logged-in-as">(logged in as <?php echo $username ?>)</p>
    <textarea name="message"></textarea>
    <button type="submit">Submit</button>
</form>
<form action="?t=delete-account" method="post">
    <button type="submit" class="delete-account">delete account</button>
</form>
<form action="?t=logout" method="post">
    <button type="submit" class="logout">log out</button>
</form>
<?php endif; ?>

<?php if ($userStatus == "signup success") : ?>
<p class="user-status">Sign up successful. You can now log in.</p>
<?php endif; ?>

<?php if ($userStatus == "already exists") : ?>
<p class="user-status">Sign up unsuccessful. There is already a user with that username.</p>
<?php endif; ?>

<?php if ($userStatus == "invalid username") : ?>
<p class="user-status">Sign up unsuccessful. Invalid username. Your username has to be between 4 and 64 characters long and contain only alphanumeric characters.</p>
<?php endif; ?>

<?php if ($userStatus == "session expired") : ?>
<p class="user-status">Sign up unsuccessful. There is already a user with that username.</p>
<?php endif; ?>

<?php if ($userStatus == "user not found") : ?>
<p class="user-status">Invalid credentials.</p>
<?php endif; ?>

<?php if ($userStatus == "invalid password") : ?>
<p class="user-status">Invalid password.</p>
<?php endif; ?>

<?php if ($userStatus == "account deleted") : ?>
<p class="user-status">Account successfully deleted.</p>
<?php endif; ?>

<?php if ($userStatus == "logout") : ?>
<p class="user-status">You have logged out.</p>
<?php endif; ?>

<?php if (!$loggedIn) : ?>
<form class="login" method="post" action="?t=login">
    <p>Log in</p>
    <input type="text" name="username" placeholder="username" />
    <input type="password" name="password" placeholder="password" />
    <button type="submit">Submit</button>
</form>
<form class="signup" method="post" action="?t=signup">
    <p>Sign up for a new account</p>
    <input type="text" name="username" placeholder="username" />
    <input type="password" name="password" placeholder="password" />
    <button type="submit">Submit</button>
</form>
<?php endif; ?>

</div> <!-- div.comments -->
