<?php
  $dir = 'sqlite:relation.db';
  $db  = new PDO($dir) or die("Database 404: Error code 4060");
  $item = "ECrelationtest.txt"; #Look into routing for changing what is actually going on in the url
  $sql=<<<SQL
    SELECT Keyword from relations
    WHERE SourceFile='$item';
SQL;
  $rows = $db->query($sql);
  foreach ($rows as $row) {
    #var_dump($row);
  }

?>

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>MSU Archives</title>
  <link rel="stylesheet" type="text/css" href="css/global.css" />
  <link rel="stylesheet" type="text/css" href="css/item-page.css" />
</head>
<nav>
  <ul>
    <li><a href="GridMenu-master/index.html">Main</a></li><!-- Goes into the main .html file -->
    <li><a href="/css/">Book That</a></li><!-- Goes to the item page for the book -->
    <li><a href="/js/">Chapter List</a></li><!-- Goes to the list of all chapters in the book -->
  </ul>
</nav>

<!-- This is a comment -->

<body>
  <div id="Main">
    main
    <div id="Content">
      content
      <div id="Top-Content">

        <!-- This div contains a picture of the item along with it's designated name -->
        <div id="Item-Picture">
          <h1>Chapter N, Book That</h1>
          <img src="img/book.jpg" alt="A book by Ivan Doig">
        </div>
        <!--                                                                         -->

        <!-- This div contains all the metadata information for the item -->
        <div id="Item-Content">
          <ul>
            <!-- The Title -->
            <li><p class="metadata-title">
              <strong>Title </strong>
              <span class="metadata-field" property="name">
                This House of Sky
              </span>
            </p></li>

            <!-- The abstract -->
            <li><p class="metadata-abstract">
              <strong>Abstract </strong>
              <span class="metadata-field" property="name">
                Lorem ipsum ornare ac feugiat libero lacinia sed, laoreet potenti egestas nisi dolor netus tortor, rhoncus nunc proin sem pretium placerat morbi habitant tempor feugiat faucibus enim.
                Himenaeos bibendum class ege
              </span>
            </p></li>

            <!-- The genre the item falls into -->
            <li><p class="metadata-genre">
              <strong>Genre </strong>
              <span class="metadata-field" property="name">
                Non-Fictional, Montana
              </span>
            </p></li>

            <!-- The page length of the document -->
            <li><p class="metadata-length">
              <strong>Length </strong>
              <span class="metadata-field" property="name">
                135 pages
              </span>
            </p></li>

            <!-- The unique item id -->
            <li><p class="metadata-id">
              <strong>Object ID </strong>
              <span class="metadata-field" property="name">
                821f03288846297c2cf43c34766a38f7
              </span>
            </p></li>

            <!-- This is the date the item was created -->
            <li><p class="metadata-created">
              <strong>Date Created </strong>
              <span class="metadata-field" property="name">
                April 30, 2018
              </span>
            </p></li>

            <!-- The book this chapter comes from -->
            <li><p class="metadata-book">
              <strong>Related Book </strong>
              <span class="metadata-field" property="name">
                This House of Sky
              </span>
            </p></li>

            <!-- The keywords of the document from python -->
            <li><p class="metadata-keywords">
              <strong>Keywords </strong>
              <span class="metadata-field" property="name">
                <a href="relation-page.php?[variable name]=value">Father</a>;
                <a href="relation-page.php">Jenny</a>;
                <a href="relation-page.php">Forrest</a>;
                <a href="relation-page.php">Abe</a>;
                <a href="relation-page.php">Chris</a>;
                <a href="relation-page.php">Dog</a>
              </span>
            </p></li>

            <!-- The geolocations of the document from python -->
            <li><p class="metadata-geolocations">
              <strong>Geolocations </strong>
              <span class="metadata-field" property="name">
                Bridger, MT, US; Bozeman, MT, US; Dillon, MT, US
              </span>
            </p></li>
          </ul>
        </div>
      </div>
      <div id="Bottom-Content">

        <!-- These are the documents that have the closest relation number to the item -->
        <div id="Related-Content">
          <h1> More Like This </h1>
          <div id="Related-Books">
            <img src="img/related1.jpg" alt="Book related to This House of Sky">
            <img src="img/related2.jpg" alt="Book related to This House of Sky">
            <img src="img/related3.jpg" alt="Book related to This House of Sky">
          </div>

          <!-- This button lets users go back to the main collect rather than having to scroll back up -->
          <a href="GridMenu-master/index.html">
            <button id="menu-return">
              Menu
            </button>
          </a>
        </div>
      </div>
    </div>
  </div>
</body>
</html>

<!--https://stackoverflow.com/questions/15481911/linking-to-a-specific-part-of-a-web-page -->
