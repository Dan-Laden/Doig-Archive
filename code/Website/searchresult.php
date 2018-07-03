<?php
  $searchword = $_GET['searchword'];

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

  $search = "%".$searchword."%";


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
    WHERE Keyword LIKE :fill;
SQL;

$keywords = prepdb($keyworddb, $getKeywords, $search);

$relations = array();
foreach ($keywords as $keyword) {
  $chapter = $keyword["SourceFile"];
  if(!(in_array($chapter, $relations)))
  {
    array_push($relations, $chapter);
  }
}

$books = prepdb($bookdb, $getBooks, $search);
$chapters = prepdb($itemdb, $getChapters, $search);

$numResults = count($books) + count($chapters) + count($relations);

#var_dump($books);
#var_dump($chapters);
#var_dump($relations);
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
          <div id=Search-Item>
            <ul>
            <?php
              #<img src="img/related1.jpg" alt="Book related to This House of Sky">
              #<span> Chapter 1 </span>
              foreach ($books as $book)
              {
                $title = $book["Title"];
                $url = "book-page.php?book=".$title;
                echo("<li><a href='$url'>$title</a></li>");
              }

              foreach ($chapters as $chapter)
              {
                $id = $chapter["ID"];
                $url = "item-page.php?item=".$id;
                echo("<li><a href='$url'>$id</a></li>");
              }

              foreach ($relations as $relation)
              {
                $source = $relation;
                $url = "item-page.php?item=".$source;
                echo("<li><a href='$url'>$source</a></li>");
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
