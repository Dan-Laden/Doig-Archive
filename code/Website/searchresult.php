<?php
  $searchword = $_GET['searchword'];
  $fuzzySearch = $_GET['Match'];

  #This is for fixing the possibility of sql injections
  function prepdb($db, $sql, $filler){
    $rows = $db->prepare($sql);
    $rows->bindParam(':fill', $filler);
    $rows->execute();
    $rows->setFetchMode(PDO::FETCH_ASSOC);
    $row = $rows->fetchAll();
    return $row;
  }

  $bookDir = 'sqlite:books.db';
  $itemDir = 'sqlite:items.db';
  $keywordDir = 'sqlite:relation.db';
  $bookdb  = new PDO($bookDir) or die("Database 404: Error code 4060");
  $itemdb  = new PDO($itemDir) or die("Database 404: Error code 4060");
  $keyworddb  = new PDO($keywordDir) or die("Database 404: Error code 4060");

  if($fuzzySearch == 'off')
  {
      $search = $searchword;
  } else {
    $search = "%".$searchword."%";
  };




#These are the three databases that get queried when searching
  $getBooks=<<<SQL
    SELECT Title from BOOKS
    WHERE Title LIKE :fill;
SQL;

  $getChapters=<<<SQL
    SELECT ID from ITEMS
    WHERE ID LIKE :fill
    ORDER BY length(ID), ID;
SQL;

  $getKeywords=<<<SQL
    SELECT * from RELATIONS
    WHERE Keyword LIKE :fill
    ORDER BY Weight;
SQL;

$keywords = prepdb($keyworddb, $getKeywords, $search);

#instead of getting if the keyword exists this finds what item the keyword appears in
$relations = array();
foreach ($keywords as $keyword) {
  $chapter = $keyword["SourceFile"];
  if(!(in_array($chapter, $relations)))
  {
    array_push($relations, $chapter);
  }
}

#these are where the results are stored
$books = prepdb($bookdb, $getBooks, $search);
$chapters = prepdb($itemdb, $getChapters, $search);

#counts the number of results that spawn
$numResults = count($books) + count($chapters) + count($relations);
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
      <?php echo("<h1>$searchword</h1>");  ?>
      <h4> __________________________________ </h4>
      <?php echo("<h4>$numResults results have been found</h4>");  ?>
      <div id="Top-Content">
        <h2> Related Items </h2>
          <div id="Search-Item">
            <ul>
            <?php
              #<img src="img/related1.jpg" alt="Book related to This House of Sky">
              #<span> Chapter 1 </span>
              foreach ($books as $book)
              {
                echo("<div id ='Result-Item'>");
                echo("<div id ='Result-Img'>");
                $picture = $book["Img"];
                $img = "img/".$picture;
                echo("<img src=$img alt='A book by Ivan Doig'>");
                echo("</div><div id ='Result-Link'>");
                $title = $book["Title"];
                $url = "book-page.php?book=".$title;
                echo("<li><a href='$url'>$title</a></li></div></div>");
              }

              foreach ($chapters as $chapter)
              {
                echo("<div id ='Result-Item'>");
                echo("<div id ='Result-Img'>");
                $img = $book["Img"];
                echo("<img src=$img alt='A book by Ivan Doig'>");
                echo("</div><div id ='Result-Link'>");
                $id = $chapter["ID"];
                $url = "item-page.php?item=".$id;
                echo("<li><a href='$url'>$id</a></li></div></div>");
              }

              foreach ($relations as $relation)
              {
                echo("<div id ='Result-Item'>");
                echo("<div id ='Result-Img'>");
                echo("</div><div id ='Result-Link'>");
                $source = $relation;
                $url = "item-page.php?item=".$source;
                echo("<li><a href='$url'>$source</a></li></div></div>");
              }
            ?>
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
</body>

<!-- This is built in js for letting the user jump back to their previous page -->
<script>
function goBack() {
    window.history.back();
}
</script>
