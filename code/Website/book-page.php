<?php
  $bookDir = 'sqlite:books.db';
  $itemDir = 'sqlite:items.db';
  $bookdb  = new PDO($bookDir) or die("Database 404: Error code 4060");
  $itemdb  = new PDO($itemDir) or die("Database 404: Error code 4060");
  $book = $_GET['book'];
  $search = "%".$book."%";

  $getBook=<<<SQL
    SELECT * from BOOKS
    WHERE Title = :book;
SQL;
  $getChapters=<<<SQL
    SELECT ID from ITEMS
    WHERE ID LIKE '$search'
    ORDER BY length(ID), ID;
SQL;

  #This is for fixing the possibility of sql injections
  $rows = $bookdb->prepare($getBook);
  $rows->bindParam(':book', $book);
  $rows->execute();
  $rows->setFetchMode(PDO::FETCH_ASSOC);
  $row = $rows->fetch();

  #This grabs all the needed information from the database
  $chapters = $row["Chapters"];
  $length = $row["Pages"];
  $picture = $row["Img"];
  $img = "img/".$picture;

  #This grabs all the chapters the book has
  $rows = $itemdb->query($getChapters);
?>

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>MSU Archives</title>
  <link rel="stylesheet" type="text/css" href="css/global.css" />
  <link rel="stylesheet" type="text/css" href="css/book-page.css" />
</head>
<nav>
  <ul>
    <li><a href="index.html">Main</a></li><!-- Goes into the main .html file -->
    <li class="backli"><a onclick="goBack()">Back</a></li><!-- Goes back to previous page -->
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
        <ul>
          <li id="links">
            <a class="contact" href="https://www.lib.montana.edu/digital/contact.php?_ga=2.146077181.811359499.1534877159-1076287462.1511386704" title="contact Montana State University (MSU) Library">Contact Us</a>
          </li>

          <li id="info">
            © Copyright 2018
            <span property="copyrightHolder publisher"><a href="https://www.lib.montana.edu/digital/">Montana State University (MSU) Library</a></span>
          </li>
        </ul>
        </div>
      </div>
    </div>
  </div>
</body>
</html>

<!-- This is built in js for letting the user jump back to their previous page -->
<script>
function goBack() {
    window.history.back();
}
</script>

<!--https://stackoverflow.com/questions/871858/php-pass-variable-to-next-page-->
<!--https://www.acunetix.com/blog/articles/prevent-sql-injection-vulnerabilities-in-php-applications/-->
