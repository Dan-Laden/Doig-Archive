<?php
  $bookDir = 'sqlite:books.db';
  $itemDir = 'sqlite:items.db';
  $bookdb  = new PDO($bookDir) or die("Database 404: Error code 4060");
  $itemdb  = new PDO($itemDir) or die("Database 404: Error code 4060");
  $book = "This House of Sky"; #Look into routing for changing what is actually going on in the url
  $search = "%".$book."%";
  $getBook=<<<SQL
    SELECT * from BOOKS
    WHERE Title='$book';
SQL;
$getChapters=<<<SQL
  SELECT ID from ITEMS
  WHERE ID LIKE '$search'
  ORDER BY ID;
SQL;
  $rows = $bookdb->query($getBook);
  $row = $rows->fetch();
  $chapters = $row["Chapters"];
  $length = $row["Pages"];
  $img = $row["Img"];

  $rows = $itemdb->query($getChapters);
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
    <li><a href="index.html">Main</a></li><!-- Goes into the main .html file -->
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
        <div id="Book-Picture">
          <?php echo("<h1>$book</h1>");
          echo("<img src=$img alt='A book by Ivan Doig'>");
          ?>
        </div>
        <!--                                                                         -->

        <!-- This div contains all the metadata information for the item -->
        <div id="Book-Content">
          <ul>
            <!-- The Title -->
            <li><p class="metadata-title">
              <strong>Title </strong>
                <?php echo("<span class='metadata-field' property='name'>$book</span>"); ?>
            </p></li>

            <!-- The abstract -->
            <li><p class="metadata-chapters"><?php #TODO TODO TODO ?>
              <strong>Chapters</strong>
              <!--echo("<span class='metadata-field' property='name'>$text</span>"); -->
              <ul>
              <?php
                foreach ($rows as $row)
                {
                  $url = "item-page.php?item=".$row[0];
                  echo("<li><a href='$url'>$row[0]</a></li>");
                }
              ?>
              </ul>
            </p></li>

            <!-- The page length of the document -->
            <li><p class="metadata-length">
              <strong>Length</strong>
              <?php echo("<span class='metadata-field' property='name'>$length</span>"); ?>
            </p></li>

            <!-- This is the date the item was created -->
            <li><p class="metadata-created">
              <strong>Date Created</strong>
              <span class="metadata-field" property="name">
                May 28, 2018
              </span>
            </p></li>

          </ul>
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
  </div>
</body>
</html>
