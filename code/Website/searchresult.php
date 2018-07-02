<?php
  $searchword = $_GET['searchword'];

  #This is for fixing the possibility of sql injections
  function prepdb($db, $sql, $filler){
    $rows = $db->prepare($sql);
    $rows->bindParam(':fill', $filler);
    $rows->execute();
    $rows->setFetchMode(PDO::FETCH_ASSOC);
    $row = $rows->fetch();
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
    SELECT * from BOOKS
    WHERE Title LIKE :fill;
SQL;

  $getChapters=<<<SQL
    SELECT ID from ITEMS
    WHERE ID LIKE :fill
    ORDER BY length(ID), ID;
SQL;

  $getKeywords=<<<SQL
    SELECT Keyword from RELATIONS
    WHERE Keyword LIKE :fill;
SQL;

$keywords = prepdb($keyworddb, $getKeywords, $search);
$chapters = $keywords["SourceFile"];

$relations = array();
foreach ($chapters as $chapter) {
  if(!(in_array($chapter, $relations)))
  {
    array_push($relations, $chapter);
  }
}

$books = prepdb($bookdb, $getBooks, $search);
$chapters = prepdb($itemdb, $getChapters, $search);



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
      <div id="Top-Content">
        <h2> Related Items </h2>
          <div id=Search-Item>
            <img src="img/related1.jpg" alt="Book related to This House of Sky">
            <span> Chapter 1 </span>
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
