<!DOCTYPE html>
<html lang="en-GB">

<head>

    <title>Unix stuff</title>

    <?php
        include 'default-head.php'
    ?>

</head>

<body>

    <?php
        include 'navbar.php'
    ?>

    <header>
        <h1>Unix stuff</h1>
    </header>

    <main>

        <h2>My main OS</h2>
        <p>I am very much interested in Unix-like operating systems. I use Linux Mint with i3wm (and some utilities
            borrowed from the Cinnamon DE) on daily basis. I love using Linux OSes because <em>they just work</em>.</p>
        <p>Linux is modularised which basically means that you can modify only part of the system.
            For example, even though I am using Linux Mint Cinnamon, I can also use other DEs or WMs like i3wm.
            You can swap out whatever you don’t like for something you do like.
        </p>
        <p>Apart from that, I am also interested in configuring the Linux experience.
            That’s why my <code>config</code> directory in my Personal Notebook is so big.
            It contains many scripts and config files that enhance and personalise my OS.
        </p>
        <p>Now, I cannot imagine going back to Windows. I am still using Windows, but purely for entertainment like
            video games.</p>

    </main>

    <?php
        $page = "linux";
        include 'comments.php';
    ?>

</body>

</html>
