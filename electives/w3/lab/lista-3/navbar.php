
<nav>
    <noscript class="no-js">
        <div class="margin"></div>
        <input type="checkbox" name="dropdown" id="dropdown-button">
        <label for="dropdown-button" class="no-select">
            <span class="close">close</span><span class="open">open</span>&nbsp;menu
        </label>
        <?php
            include 'navbar-content.php'
        ?>
    </noscript>
    <div class="standard">
        <button class="dropdown-button">•••</button>
        <?php
            include 'navbar-content.php'
        ?>
    </div>
</nav>

<script src="js/navbar.js"></script>
