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
        <h1>Metaheuristic algorithms</h1>
    </header>

    <main>

        <p>I find metaheuristic algorithms fascinating.
            I am certainly not proficient in this field, but I just find it interesting.</p>
        <p>The field studies methods for finding solutions to problems that cannot be solved through conventional means.
            For example, finding the lowest point of a four dimensional function that cannot be differentiated through
            conventional mathematical analysis. You can then apply a metaheuristic algorithm that will find a reasonable
            solution in a reasonable amount of time.The solution it finds may be not perfect, and may not be the best
            solution, but it will find <em>something</em> instead of trying every possible combination.</p>
        <p>The quality of the solution, or the proximity of the output solution to the actual global best solution is
            the main target of study of metaheuristics.
            Designing an algorithm that will best fit the situation we are in.
            One can say, that it all boils down to random guesses (because a lot of metaheuristic algorithms use
            randomisation), but a good algorithm will improve its search every time a new better solution is found.
            It is random, but far from completely random guessing.
        </p>

    </main>

    <?php
        $page = "metaheuristics";
        include 'comments.php';
    ?>

</body>

</html>
