<?php
  $keyword = $_GET['keyword'];

  #This is for fixing the possibility of sql injections
  function prepdb($db, $sql, $filler){
    $rows = $db->prepare($sql);
    $rows->bindParam(':fill', $filler);
    $rows->execute();
    $rows->setFetchMode(PDO::FETCH_ASSOC);
    $row = $rows->fetchAll();
    return $row;
  }


  $keywordDir = 'sqlite:relation.db';
  $itemDir = 'sqlite:items.db';
  $keyworddb  = new PDO($keywordDir) or die("Database 404: Error code 4060");
  $itemdb  = new PDO($itemDir) or die("Database 404: Error code 4060");

  $getChapters=<<<SQL
    SELECT * from ITEMS
    WHERE ID LIKE :fill
    ORDER BY length(ID), ID;
SQL;

  $getKeywords=<<<SQL
    SELECT * from RELATIONS
    WHERE Keyword LIKE :fill
    ORDER BY Weight;
SQL;

  $keywords = prepdb($keyworddb, $getKeywords, $keyword);


  #instead of getting if the keyword exists this finds what item the keyword appears in
  $relations = array();
  foreach ($keywords as $keyword) {
    $chapter = $keyword["SourceFile"];
    if(!(in_array($chapter, $relations)))
    {
      array_push($relations, $chapter);
    }
  }

  $rel_images = array();
  foreach ($relations as $relation) {
    $item = prepdb($itemdb, $getChapters, $relation);
    $img = $item[0]["Img"];
    array_push($rel_images, $img);
  }

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
        <?php
          $index = 0;
          foreach ($relations as $relation) {
            if($index === 0)
            {
              echo("<div id='Row'>");
            }
            elseif("integer" === gettype($index/4))
            {
              echo("</div><div id='Row'>");
            }
            $url = "item-page.php?item=".$relation;
            $htmlstring = <<<HEREDOC
              <div id=Related-Item>
                <a href="$url"><img src="$rel_images[$index]" alt="cover of $relation">
                <span> $relation </span></a>
              </div>
HEREDOC;
            echo($htmlstring);
            ++$index;
          }


         ?>


      </div>
      <div id="Bottom-Content"> <!-- Code from original https://arc.lib.montana.edu/ivan-doig/item pages -->
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
</body>
<!-- This is built in js for letting the user jump back to their previous page -->
<script>
function goBack() {
    window.history.back();
}
</script>
