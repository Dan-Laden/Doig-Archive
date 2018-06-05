<?php
  $keyword = $_GET['keyword'];
 ?>
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>MSU Archives</title>
  <link rel="stylesheet" type="text/css" href="css/global.css" />
    <link rel="stylesheet" type="text/css" href="css/relation-page.css" />
</head>
<nav>
  <ul>
    <li><a href="index.html">Main</a></li><!-- Goes into the main .html file -->
    <li class="backli"><a onclick="goBack()">Back</a></li><!-- Goes back to previous page -->
  </ul>
</nav>

<body>
  <div id="Main">
    main
    <div id="Content">
      <?php echo("<h1>$keyword</h1>");  ?>
      <h4> __________________________________ </h4>
      <div id="Top-Content">
        <h2> Related Items </h2>

        <!-- Each row contains 4 items that have a close relation value to the keyword found this is generated so the max is 12 the minimum is none -->
        <div id="Row">
          <div id=Related-Item>
            <img src="img/related1.jpg" alt="Book related to This House of Sky">
            <span> Chapter 1 </span>
          </div>
          <div id=Related-Item>
            <img src="img/related1.jpg" alt="Book related to This House of Sky">
            <span> Chapter 2 </span>
          </div>
          <div id=Related-Item>
            <img src="img/related1.jpg" alt="Book related to This House of Sky">
            <span> Chapter 3 </span>
          </div>
          <div id=Related-Item>
            <img src="img/related1.jpg" alt="Book related to This House of Sky">
            <span> Chapter 4 </span>
          </div>
        </div>

        <!-- Row 2/3-->
        <div id="Row">
          <div id=Related-Item>
            <img src="img/related2.jpg" alt="Book related to This House of Sky">
            <span> Chapter 5 </span>
          </div>
          <div id=Related-Item>
            <img src="img/related2.jpg" alt="Book related to This House of Sky">
            <span> Chapter 6 </span>
          </div>
          <div id=Related-Item>
            <img src="img/related2.jpg" alt="Book related to This House of Sky">
            <span> Chapter 7 </span>
          </div>
          <div id=Related-Item>
            <img src="img/related2.jpg" alt="Book related to This House of Sky">
            <span> Chapter 8 </span>
          </div>
        </div>

        <!-- Row 3/3-->
        <div id="Row">
          <div id=Related-Item>
            <img src="img/related3.jpg" alt="Book related to This House of Sky">
            <span> Chapter 9 </span>
          </div>
          <div id=Related-Item>
            <img src="img/related3.jpg" alt="Book related to This House of Sky">
            <span> Chapter 10 </span>
          </div>
          <div id=Related-Item>
            <img src="img/related3.jpg" alt="Book related to This House of Sky">
            <span> Chapter 11 </span>
          </div>
          <div id=Related-Item>
            <img src="img/related3.jpg" alt="Book related to This House of Sky">
            <span> Chapter 12 </span>
          </div>
        </div>
      </div>
      <div id="Bottom-Content">

        <!-- This button lets users go back to the main collect rather than having to scroll back up -->
        <a href="index.html">
          <button id="menu-return">
            Menu
          </button>
        </a>
      </div>
    </div>
  </div>
</body>

<!-- This is built in js for letting the user jump back to their previous page -->
<script>
function goBack() {
    window.history.back();
}
</script>
