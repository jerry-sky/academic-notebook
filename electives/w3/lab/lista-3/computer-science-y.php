<!DOCTYPE html>
<html lang="en-GB">

<head>

    <title>Computer science–y</title>

    <?php
        include 'default-head.php'
    ?>

</head>

<body>

    <?php
        include 'navbar.php'
    ?>

    <main>

        <h1>Computer science–related stuff</h1>

        <h2>VYROW</h2>
        <p><em>View Your Repository On the Web</em></p>
        <p>Simple GitHub Action that renders all Markdown documents in given repository to HTML documents. It may be
            used as a frontend of the repository that is more based around notes or documents in general rather based
            around normal source code.</p>
        <p>It uses Pandoc for rendering Markdown documents and Pandoc-KaTeX to render LaTeX expressions inside these
            Markdown documents. The rest of the program is based around Bash scripts for <a
                href="https://github.com/jerry-sky/vyrow/blob/master/install-pandoc-katex.sh">installing needed
                programs</a> and <a
                href="https://github.com/jerry-sky/vyrow/blob/master/install-pandoc-katex.sh">rendering the
                documents</a>.</p>
        <a href="https://github.com/marketplace/actions/vyrow">VYROW on GH Action Marketplace</a>

        <h2>Restaurant Rush (unreleased)</h2>
        <p>A Unity game where the player needs to serve food to the canteen clients as quickly as possible, ninja-style.
            My involvement here was creating 3D assets for the game. I also helped a little in the organisational stuff.
        </p>
        <a href="https://github.com/Qarian/Restaurant-rush">GitHub repository</a>

        <h2>Repository notebooks</h2>
        <h3>Personal Notebook</h3>
        <p>I’ve created my personal notebook to organise my notes into one place. Additionally, I keep all of my config
            files and various scripts.</p>
        <a href="https://personal.jerry-sky.me/">website</a>
        <p>Highlights:</p>
        <ul>
            <li>First setup script — after a fresh OS installation this script installs some basic stuff to get started.
            </li>
            <li>
                <p>Installation scripts for various programs.</p>
                <p>e.g. <a
                        href="https://github.com/jerry-sky/personal-notebook/blob/master/config/src/scripts/install-blender.sh">installation
                        script for Blender 3D:</a></p>
                <pre>
#!/bin/bash

printf "\n\033[1mBlender\033[0m\n"

ftp_url="https://ftp.nluug.nl/pub/graphics/blender/release/"

# get the remote directory of the latest Blender version
rem_dir="$(curl -s $ftp_url | perl -nle 'print $& if /Blender\d\.\d{2}/g' | tail -n 1)"

# get the name of the remote archive
rem_arc="$(curl -s -L $ftp_url$rem_dir | perl -nle 'print $& if /blender\-\d\.\d{2}\.\d{1,2}\-linux64\.tar\.xz/g' | tail -n 1)"

printf "\n\033[1mDownloading…\033[0m\n"
echo "Archive: $rem_arc"

if [ -z "$rem_arc" ]; then
    echo 'error: couldn’t download Blender — extracted filename is empty'
    exit 1
fi

# download the archive
archive="/tmp/blender.tar.xz"
curl --output "$archive" "$ftp_url$rem_dir/$rem_arc"

printf "\n\033[1mInstalling…\033[0m\n"
# unpack the archive
cd "/tmp"
unpacked="/tmp/${rem_arc%\.tar\.xz}"
tar -xf "$archive"
# copy the program (application) metadata
sudo cp "$unpacked/blender.desktop" "/usr/share/applications/blender.desktop"
sudo update-desktop-database /usr/share/applications
# copy the program data
sudo mkdir -p "/opt/blender"
sudo cp -r -- $unpacked/* "/opt/blender/"
# link the executable
cd "/usr/bin"
sudo ln -fs "/opt/blender/blender" "blender"
                </pre>
            </li>
            <li><a href="https://github.com/jerry-sky/personal-notebook/tree/master/config/second-keyboard">Second
                    keyboard setup — using Keebie.py for transforming my second USB keyboard as a big shortcut
                    matrix.</a></li>
        </ul>

        <h3>Academic notebook</h3>
        <p>This repository holds almost all of my academic efforts that I’ve gathered throughout my studies at my uni.
            It contains both the notes (Markdown + LaTeX) and programs (source code).</p>
        <a href="https://academic.jerry-sky.me/">website</a>

        <h2>E-commerce website</h2>
        <p>(previous version, no longer in use)</p>
        <p>I’ve created a simple online store for my father’s business. It worked pretty well for a while and amounted
            to pretty acceptable sale numbers. However, a ready-to-go solution that you can buy is better, because it
            has more features — a product made by single person cannot compete with a product made by a big team of
            people that worked on in for years.</p>
        <p>Technologies I’ve used include:</p>
        <ul>
            <li>TypeScript,</li>
            <li>Angular,</li>
            <li>ExpressJS,</li>
            <li>MySQL,</li>
            <li>Bash,</li>
            <li>and other.</li>
        </ul>
        <p>The website had frontend made in Angular (both the main customer website and the admin panel). The backend
            was running on TypeScript-turbocharged ExpressJS. All the data was stored in a MySQL database.</p>

        <h2>My minuscule involvement in random open-source projects</h2>
        <p>I’ve helped (a little bit) in two random projects that were just related to what I was working on.</p>
        <p><a href="https://github.com/allista/WakatimeBlender">WakaTime Blender</a> a Blender plugin that tracks user
            activity and reports it back to WakaTime.</p>
        <p><a href="https://github.com/jgm/pandoc/">Pandoc</a> is a markup converter that accepts many various markup
            languages. I needed that one thing for my other project to work (VYROW) so I’ve created a pull request with
            a suggestion about a small thing in the HTML5 template.</p>

    </main>

    <?php
        $page = "computer-science-y";
        include 'comments.php';
    ?>

</body>

</html>
