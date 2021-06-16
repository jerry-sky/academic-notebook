
<footer>

<p class="visitors">Visitors so far: <?php

$VISITOR_DBA_FILE = 'visitors.dba';
$VISITOR_KEY = 'visitors';

// get the IP of the user
$ip = $_SERVER['REMOTE_ADDR'];

// open a new database session
$dba = dba_open($VISITOR_DBA_FILE, 'c');
// get the current number of visitors
$currentVisitors = intval(dba_fetch($VISITOR_KEY, $dba));

// check if the IP haven’t already visited this page (or over a day ago)
if (!dba_exists($ip, $dba) || intval(dba_fetch($ip, $dba)) < time()) {
    // refresh (or set a new) timer
    dba_delete($ip, $dba);
    $tmp = time() + (24 * 60 * 60);
    dba_insert($ip, $tmp, $dba);

    // record the visit
    $currentVisitors += 1;
    dba_delete($VISITOR_KEY, $dba);
    dba_insert($VISITOR_KEY, $currentVisitors, $dba);
    dba_close($dba);
}

echo $currentVisitors;

?>
</p>

</footer>
