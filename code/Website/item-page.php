<?php
  $dir = 'sqlite:items.db';
  $itemdb  = new PDO($dir) or die("Database 404: Error code 4060");
  $item = $_GET['item'];

  $getItem=<<<SQL
    SELECT * from ITEMS
    WHERE ID=:item;
SQL;

  #This is for fixing the possibility of sql injections
  $rows = $itemdb->prepare($getItem);
  $rows->bindParam(':item', $item);
  $rows->execute();
  $rows->setFetchMode(PDO::FETCH_ASSOC);
  $row = $rows->fetch();

  #This grabs all the needed information from the database
  $keywords = explode("; ", $row["Keyword"]);
  $text = implode(' ', array_slice(explode(' ', $row["RawText"]), 0, 50));
  $length = $row["Pages"];
  $book = $row["RelatedBook"];
  $img = $row["Img"];
  $sentiment = $row["Emotion"];
  $geoloc = explode("; ", $row["Geolocation"]);
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
    <li><img src="img/logo.png" alt='MSU Logo'><a href="index.html">Main</a></li><!-- Goes into the main .html file -->
    <?php
      $book = str_replace("-", " ", $book);
      $url = "book-page.php?book=".$book;
      echo("<li><a href='$url'>$book</a></li>")
    ?> <!-- Goes to the item page for the book -->
    <li class="backli"><a onclick="goBack()">Back</a></li><!-- Goes back to previous page -->
  </ul>
</nav>

<!-- This is a comment -->

<body>
  <div id="Main">
    <div id="Content">
      <div id="Top-Content">

        <!-- This div contains a picture of the item along with it's designated name -->
        <div id="Item-Picture">
          <?php echo("<h1>$item</h1>");
          echo("<img src=$img alt='A book by Ivan Doig'>");
          ?>
        </div>
        <!--                                                                         -->

        <!-- This div contains all the metadata information for the item -->
        <div id="Item-Content">
          <ul>
            <!-- The Title -->
            <div><li><p class="metadata-title">
              <strong>Title </strong>
                <?php echo("<span class='metadata-field' property='name'>$item</span>"); ?>
            </p></li></div>

            <!-- The abstract -->
            <div><li><p class="metadata-abstract">
              <strong>Raw Text Example </strong>
              <?php echo("<span class='metadata-field' property='name'>$text</span>"); ?>
            </p></li></div>

            <!-- The genre the item falls into -->
            <div><li><p class="metadata-genre">
              <strong>Sentiment Value </strong>
              <span class="metadata-field" property="name">
                <?php echo("<span class='metadata-field' property='name'>$sentiment</span>"); ?>
              </span>
            </p></li></div>

            <!-- The page length of the document -->
            <div><li><p class="metadata-length">
              <strong>Length </strong>
              <?php echo("<span class='metadata-field' property='name'>$length</span>"); ?>
            </p></li><div>

            <!-- The unique item id -->
            <div><li><p class="metadata-id">
              <strong>Object ID </strong>
              <span class="metadata-field" property="name">
                821f03288846297c2cf43c34766a38f7
              </span>
            </p></li><div>

            <!-- This is the date the item was created -->
            <div><li><p class="metadata-created">
              <strong>Date Created </strong>
              <span class="metadata-field" property="name">
                April 30, 2018
              </span>
            </p></li></div>

            <!-- The book this chapter comes from -->
            <div><li><p class="metadata-book">
              <strong>Related Book </strong>
              <?php echo("<span class='metadata-field' property='name'>$book</span>"); ?>
            </p></li></div>

            <!-- The keywords of the document from python -->
            <div><li><p class="metadata-keywords">
              <strong>Keywords</strong>
              <span class="metadata-field" property="name">
                <?php
                for ($i=0; $i < 20 ; $i++) {
                  if ($keywords[$i]){
                    $url = "relation-page.php?keyword=".$keywords[$i];
                    echo("<a href='$url'>$keywords[$i]</a>; ");
                  } else {
                    break;
                  }

                }
                ?>
              </span>
            </p></li></div>

            <!-- The geolocations of the document from python -->
            <div><li><p class="metadata-geolocations">
              <strong>Geolocations </strong>
              <span class="metadata-field" property="name">
                <?php
                for ($i=0; $i < 10 ; $i++) {
                  if ($geoloc[$i]) {
                    $url = "relation-page.php?keyword=".$geoloc[$i];
                    echo("<a href='$url'>$geoloc[$i]</a>; ");
                  } else {
                    break;
                  }

                }
                ?>
              </span>
            </p></li></div>
          </ul>
        </div>
      </div>
      <div id="Bottom-Content">
        <!-- These are the documents that have the closest relation number to the item -->
        <div id="Related-Content">
          <!-- <h1> More Like This </h1>
          <div id="Related-Books">
            <img src="img/related1.jpg" alt="Book related to This House of Sky">
            <img src="img/related2.jpg" alt="Book related to This House of Sky">
            <img src="img/related3.jpg" alt="Book related to This House of Sky">
          </div> -->
        </div>
        <div id="Link-Content">
          <ul>
            <li id="links">
              <a class="contact" href="http://www.lib.montana.edu/digital/contact.html?_ga=2.71626970.811359499.1534877159-1076287462.1511386704" title="contact Montana State University (MSU) Library">Contact Us</a>
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

<!-- https://www.geeksforgeeks.org/php-str_replace-function/ -->
<!-- https://stackoverflow.com/questions/11219931/how-to-force-div-element-to-keep-its-contents-inside-container -->
<!-- http://php.net/manual/en/function.str-replace.php -->
<!-- http://php.net/manual/en/control-structures.else.php -->
<!-- https://www.afterhoursprogramming.com/tutorial/php/break-and-continue/ -->
<!--https://stackoverflow.com/questions/15481911/linking-to-a-specific-part-of-a-web-page -->
<!--https://stackoverflow.com/questions/5456626/php-pdo-returning-single-row-->
<!--https://stackoverflow.com/questions/871858/php-pass-variable-to-next-page-->
<!--https://stackoverflow.com/questions/5956610/how-to-select-first-10-words-of-a-sentence-->
<!--https://www.acunetix.com/blog/articles/prevent-sql-injection-vulnerabilities-in-php-applications/-->
