<?php //1-OPEN
/**
 * 

 * The template for displaying Search Results pages.
*
* @package ThemeGrill
* @subpackage ColorMag
* @since ColorMag 1.0
*/


include ('class_bancodedados.php');
$banco = new banco_de_dados (); // instancia a classe banco_de_dados
// ///////////include//////////////////////////////////////////////

// atribui a variavel $conexao com o valor retornado da funcao
$conexao = $banco->conecta ();
// verifica se conexao feita com sucesso, valor esse retornado em $conexao[0](TRUE ou FALSE)
if ($conexao [0] == true) {
	// atribui variavel $mysqli com a conexao, valor esse retornado em $conexao[1]
	$mysqli = $conexao [1];
} else {
	// cria e atribui array, com $conexao[0]->TRUE ou FALSE, e $conexao[2]->contendo o erro
	$response = array (
			'success' => $conexao [0],
			'message' => $conexao [2]
	);
	//echo json_encode ( $response );
	exit ();
}
// ###################################################FIM CONEXAO COM O BD##############################################################################

// ///////////include////////////////////////////////////////////
include ('class_operacoes_sql.php');
$operacoes_sql = new operacoes_sql (); // instancia a classe operacoes_sql
// ###############################################################
include ('class_datas.php');
$datas = new datas (); // instancia a classe datas
// ###############################################################
// //////////////////////////////////////////////////////////////
include ('class_funcoes.php');
$funcoes = new funcoes ();

////1-CLOSE
?>

<?php get_header();// loading the header ?>

<?php //2-OPEN
//f($_REQUEST['submit']){
$name = $_GET['s'];

// SET TIME ZONE FOR TABLENAME
$date_ini = 'table';
//print "<CENTER>$date_ini</CENTER>"; 

$date_end = date('Y-m-d H-i-s');
$date_end = str_replace("-","_",$date_end); //replace string for name in mysql table
$date_end = str_replace(" ","_",$date_end);
//print "<CENTER>$date_end</CENTER>"; 

$date_all = $date_ini . ' ' . $date_end;
$date_all = str_replace(" ","",$date_all);
//print "<CENTER>$date_all</CENTER>"; 

// CREATING NEW TABLE FROM QUERY USING DATE
//$date_all = 'testing';
//$sele = "CREATE TABLE $date_all(ID VARCHAR(20),title1 VARCHAR(300),PRIMARY KEY(ID))";
//$sele = "CREATE TABLE testing10(ID VARCHAR(20),title1 VARCHAR(300),PRIMARY KEY(ID))";
//$sele = "CREATE TABLE testing10 SELECT `task_ID`, `task_name`  FROM `fund`  LIMIT 3 OFFSET 0";
//$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );

// CREATING NEW TABLE FROM QUERY
//$sele = "CREATE TABLE Comments_show(doi1 VARCHAR(200),title1 VARCHAR(300),author1 VARCHAR(200),year1 VARCHAR(20),doi2 VARCHAR(200),title2 VARCHAR(300),author2 VARCHAR(200),year2 VARCHAR(20),ID mediumint(9),PRIMARY KEY(ID))";
//$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
//
// CREATING NEW TABLE FROM QUERY
//$sele = "CREATE TABLE Results_query(tablename1 VARCHAR(200),http1 VARCHAR(500),doi1 VARCHAR(200),title1 VARCHAR(300),author1 VARCHAR(200),year1 VARCHAR(20),citation VARCHAR(3000),note1 VARCHAR(2000),doi2 VARCHAR(200),title2 VARCHAR(300),author2 VARCHAR(200),year2 VARCHAR(20),ID mediumint(9),PRIMARY KEY(ID))";
//$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );

// TABLE (EMPTY COLUMNS)
//$sele = "UPDATE Comments_show SET doi1 = '',title1 = '',author1 = '',year1 = '',doi2 = '',title2 = '',author2 = '',year2 = '',ID = ''";
$sele = "DELETE FROM Results_query";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );

$LIMIT = 100;


$string_insert1 = "INSERT INTO Results_query (tablename1,http1,doi1,title1,author1,year1,citation,note1,doi2,title2,author2,year2,ID) VALUES";
$counter_array = 0;

$string_insert2 = " ('YOU SEARCHED FOR = $name', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', '$counter_array')";
$string_insert = $string_insert1 . ' ' . $string_insert2;
$sele = $string_insert;
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );

// TABLE Letters (FILL COLUMNS)
$counter_array = $counter_array + 1;
$sele = "SELECT * FROM Letters WHERE title1 LIKE '%$name%' LIMIT $LIMIT OFFSET 0;"; // OBS: Comments and Remarks (use title2)
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {	    
//////		echo '<h4>';
	while($row = $result[1]->fetch_assoc ()) {
//		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
				$doi1 = $row['doi1'];
				$title1 = $row['title1'];
				$author1 = $row['author1'];
				$year1 = $row['year1'];
				//$doi2 = $row['doi2'];
				//$title2 = $row['title2'];
				//$author2 = $row['author2'];
				//$year2 = $row['year2'];
				$http1 = $row['http1'];
				//$citation = $row['citation'];
				//$note1 = $row['note1'];
				//$ID = $row['ID'];
				
				$tablename1_array[$counter_array] = 'WL-Letters';
				$doi1_array[$counter_array] = $doi1;
				$title1_array[$counter_array] = $title1;
				$author1_array[$counter_array] = $author1;
				$year1_array[$counter_array] = $year1;
				$doi2_array[$counter_array] = 'N/A';
				$title2_array[$counter_array] = 'N/A';
				$author2_array[$counter_array] = 'N/A';
				$year2_array[$counter_array] = 'N/A';
				$http1_array[$counter_array] = $http1;
				$citation_array[$counter_array] = 'N/A';
				$note1_array[$counter_array] = 'N/A';
				$ID_array[$counter_array] = $counter_array;
		
		 //print "<CENTER>$title1</CENTER>"; 
		 //echo "<br />\n";	
		 $counter_array = $counter_array+1;
		}
//////		echo '</h4>';
	}
$string_insert1 = "INSERT INTO Results_query (tablename1,http1,doi1,title1,author1,year1,citation,note1,doi2,title2,author2,year2,ID) VALUES";
$loop_n =  sizeof($title1_array)+1;
for($i=1; $i<=$loop_n; $i++){
//echo "The number is " . $i . "<br>";
$i1 = $i - 1;
$string_insert2 = " ('$tablename1_array[$i1]', ''$http1_array[$i1]', '$doi1_array[$i1]', '$title1_array[$i1]', '$author1_array[$i1]', '$year1_array[$i1]', '$citation_array[$i1]', '$note1_array[$i1]', '$doi2_array[$i1]', '$title2_array[$i1]', '$author2_array[$i1]', '$year2_array[$i1]', '$ID_array[$i1]')";
$string_insert = $string_insert1 . ' ' . $string_insert2;
$sele = $string_insert;
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
}
//unset($http1_array);unset($doi1_array);unset($title1_array);unset($author1_array);unset($year1_array);unset($citation_array);unset($note1_array);unset($doi2_array);unset($title2_array);unset($author2_array);unset($year2_array);unset($ID_array); 
//print_r($title1_array);


// TABLE Notes-positive (FILL COLUMNS)
$counter_array = $counter_array;
$sele = "SELECT * FROM Notes_positive WHERE title1 LIKE '%$name%' LIMIT $LIMIT OFFSET 0;"; // OBS: Comments and Remarks (use title2)
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {	    
//////		echo '<h4>';
	while($row = $result[1]->fetch_assoc ()) {
//		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
				$doi1 = $row['doi1'];
				$title1 = $row['title1'];
				$author1 = $row['author1'];
				$year1 = $row['year1'];
				//$doi2 = $row['doi2'];
				//$title2 = $row['title2'];
				//$author2 = $row['author2'];
				//$year2 = $row['year2'];
				//$http1 = $row['http1'];
				//$citation = $row['citation'];
				$note1 = $row['note1'];
				//$ID = $row['ID'];
				
				$tablename1_array[$counter_array] = 'WL-Notes (positive)';
				$doi1_array[$counter_array] = $doi1;
				$title1_array[$counter_array] = $title1;
				$author1_array[$counter_array] = $author1;
				$year1_array[$counter_array] = $year1;
				$doi2_array[$counter_array] = 'N/A';
				$title2_array[$counter_array] = 'N/A';
				$author2_array[$counter_array] = 'N/A';
				$year2_array[$counter_array] = 'N/A';
				$http1_array[$counter_array] = 'N/A';
				$citation_array[$counter_array] = 'N/A';
				$note1_array[$counter_array] = $note1;
				$ID_array[$counter_array] = $counter_array;
		
		 //print "<CENTER>$title1</CENTER>"; 
		 //echo "<br />\n";	
		 $counter_array = $counter_array+1;
		}
//////		echo '</h4>';
	}
$string_insert1 = "INSERT INTO Results_query (tablename1,http1,doi1,title1,author1,year1,citation,note1,doi2,title2,author2,year2,ID) VALUES";
$loop_n =  sizeof($title1_array)+1;
//for($i=1; $i<=$loop_n; $i++){
for($i=1; $i<=$loop_n; $i++){
//echo "The number is " . $i . "<br>";
$i1 = $i - 1;
$string_insert2 = " ('$tablename1_array[$i1]', '$http1_array[$i1]', '$doi1_array[$i1]', '$title1_array[$i1]', '$author1_array[$i1]', '$year1_array[$i1]', '$citation_array[$i1]', '$note1_array[$i1]', '$doi2_array[$i1]', '$title2_array[$i1]', '$author2_array[$i1]', '$year2_array[$i1]', '$ID_array[$i1]')";
$string_insert = $string_insert1 . ' ' . $string_insert2;
$sele = $string_insert;	
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
}
//unset($http1_array);unset($doi1_array);unset($title1_array);unset($author1_array);unset($year1_array);unset($citation_array);unset($note1_array);unset($doi2_array);unset($title2_array);unset($author2_array);unset($year2_array);unset($ID_array); 
//print_r($title1_array);
//



// TABLE Notes_negative (FILL COLUMNS)
$counter_array = $counter_array;
$sele = "SELECT * FROM Notes_negative WHERE title1 LIKE '%$name%' LIMIT $LIMIT OFFSET 0;"; // OBS: Comments and Remarks (use title2)
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {	    
//////		echo '<h4>';
	while($row = $result[1]->fetch_assoc ()) {
//		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
				$doi1 = $row['doi1'];
				$title1 = $row['title1'];
				$author1 = $row['author1'];
				$year1 = $row['year1'];
				//$doi2 = $row['doi2'];
				//$title2 = $row['title2'];
				//$author2 = $row['author2'];
				//$year2 = $row['year2'];
				//$http1 = $row['http1'];
				//$citation = $row['citation'];
				$note1 = $row['note1'];
				//$ID = $row['ID'];
				
				$tablename1_array[$counter_array] = 'WL-Notes (negative)';
				$doi1_array[$counter_array] = $doi1;
				$title1_array[$counter_array] = $title1;
				$author1_array[$counter_array] = $author1;
				$year1_array[$counter_array] = $year1;
				$doi2_array[$counter_array] = 'N/A';
				$title2_array[$counter_array] = 'N/A';
				$author2_array[$counter_array] = 'N/A';
				$year2_array[$counter_array] = 'N/A';
				$http1_array[$counter_array] = 'N/A';
				$citation_array[$counter_array] = 'N/A';
				$note1_array[$counter_array] = $note1;
				$ID_array[$counter_array] = $counter_array;
		
		 //print "<CENTER>$title1</CENTER>"; 
		 //echo "<br />\n";	
		 $counter_array = $counter_array+1;
		}
//////		echo '</h4>';
	}
$string_insert1 = "INSERT INTO Results_query (tablename1,http1,doi1,title1,author1,year1,citation,note1,doi2,title2,author2,year2,ID) VALUES";
$loop_n =  sizeof($title1_array)+1;
//for($i=1; $i<=$loop_n; $i++){
for($i=1; $i<=$loop_n; $i++){
//echo "The number is " . $i . "<br>";
$i1 = $i - 1;
$string_insert2 = " ('$tablename1_array[$i1]', '$http1_array[$i1]', '$doi1_array[$i1]', '$title1_array[$i1]', '$author1_array[$i1]', '$year1_array[$i1]', '$citation_array[$i1]', '$note1_array[$i1]', '$doi2_array[$i1]', '$title2_array[$i1]', '$author2_array[$i1]', '$year2_array[$i1]', '$ID_array[$i1]')";
$string_insert = $string_insert1 . ' ' . $string_insert2;
$sele = $string_insert;	
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
}
//unset($http1_array);unset($doi1_array);unset($title1_array);unset($author1_array);unset($year1_array);unset($citation_array);unset($note1_array);unset($doi2_array);unset($title2_array);unset($author2_array);unset($year2_array);unset($ID_array); 
//print_r($title1_array);
//


// TABLE Comments (FILL COLUMNS)
$counter_array = $counter_array;
$sele = "SELECT * FROM Comments WHERE title2 LIKE '%$name%' LIMIT 100 OFFSET 0;"; // OBS: Comments and Remarks (use title2)
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {	    
//////		echo '<h4>';
	while($row = $result[1]->fetch_assoc ()) {
//		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
				$doi1 = $row['doi1'];
				$title1 = $row['title1'];
				$author1 = $row['author1'];
				$year1 = $row['year1'];
				$doi2 = $row['doi2'];
				$title2 = $row['title2'];
				$author2 = $row['author2'];
				$year2 = $row['year2'];
				//$http1 = $row['http1'];
				//$citation = $row['citation'];
				//$note1 = $row['note1'];
				//$ID = $row['ID'];
				
				$tablename1_array[$counter_array] = 'WL-Comments';
				$doi1_array[$counter_array] = $doi1;
				$title1_array[$counter_array] = $title1;
				$author1_array[$counter_array] = $author1;
				$year1_array[$counter_array] = $year1;
				$doi2_array[$counter_array] = $doi2;
				$title2_array[$counter_array] = $title2;
				$author2_array[$counter_array] = $author2;
				$year2_array[$counter_array] = $year2;
				$http1_array[$counter_array] = 'N/A';
				$citation_array[$counter_array] = 'N/A';
				$note1_array[$counter_array] = 'N/A';
				$ID_array[$counter_array] = $counter_array;
		
		 //print "<CENTER>$title1</CENTER>"; 
		 //echo "<br />\n";	
		 $counter_array = $counter_array+1;
		}
//////		echo '</h4>';
	}
$string_insert1 = "INSERT INTO Results_query (tablename1,http1,doi1,title1,author1,year1,citation,note1,doi2,title2,author2,year2,ID) VALUES";
$loop_n =  sizeof($title1_array)+1;
for($i=1; $i<=$loop_n; $i++){
//echo "The number is " . $i . "<br>";
$i1 = $i - 1;
$string_insert2 = " ('$tablename1_array[$i1]', '$http1_array[$i1]', '$doi1_array[$i1]', '$title1_array[$i1]', '$author1_array[$i1]', '$year1_array[$i1]', '$citation_array[$i1]', '$note1_array[$i1]', '$doi2_array[$i1]', '$title2_array[$i1]', '$author2_array[$i1]', '$year2_array[$i1]', '$ID_array[$i1]')";
$string_insert = $string_insert1 . ' ' . $string_insert2;
$sele = $string_insert;
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
}
//unset($http1_array);unset($doi1_array);unset($title1_array);unset($author1_array);unset($year1_array);unset($citation_array);unset($note1_array);unset($doi2_array);unset($title2_array);unset($author2_array);unset($year2_array);unset($ID_array); 
//print_r($title1_array);


// TABLE Retracted (FILL COLUMNS)
$counter_array = $counter_array;
$sele = "SELECT * FROM Retracted WHERE title1 LIKE '%$name%' LIMIT $LIMIT OFFSET 0;"; // OBS: Comments and Remarks (use title2)
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {	    
//////		echo '<h4>';
	while($row = $result[1]->fetch_assoc ()) {
//		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
				$doi1 = $row['doi1'];
				$title1 = $row['title1'];
				$author1 = $row['author1'];
				$year1 = $row['year1'];
				//$doi2 = $row['doi2'];
				//$title2 = $row['title2'];
				//$author2 = $row['author2'];
				//$year2 = $row['year2'];
				//$http1 = $row['http1'];
				//$citation = $row['citation'];
				//$note1 = $row['note1'];
				//$ID = $row['ID'];
				
				$tablename1_array[$counter_array] = 'WL-Retracted';
				$doi1_array[$counter_array] = $doi1;
				$title1_array[$counter_array] = $title1;
				$author1_array[$counter_array] = $author1;
				$year1_array[$counter_array] = $year1;
				$doi2_array[$counter_array] = 'N/A';
				$title2_array[$counter_array] = 'N/A';
				$author2_array[$counter_array] = 'N/A';
				$year2_array[$counter_array] = 'N/A';
				$http1_array[$counter_array] = 'N/A';
				$citation_array[$counter_array] = 'N/A';
				$note1_array[$counter_array] = 'N/A';
				$ID_array[$counter_array] = $counter_array;
		
		 //print "<CENTER>$title1</CENTER>"; 
		 //echo "<br />\n";	
		 $counter_array = $counter_array+1;
		}
//////		echo '</h4>';
	}
$string_insert1 = "INSERT INTO Results_query (tablename1,http1,doi1,title1,author1,year1,citation,note1,doi2,title2,author2,year2,ID) VALUES";
$loop_n =  sizeof($title1_array)+1;
for($i=1; $i<=$loop_n; $i++){
//echo "The number is " . $i . "<br>";
$i1 = $i - 1;
$string_insert2 = " ('$tablename1_array[$i1]', '$http1_array[$i1]', '$doi1_array[$i1]', '$title1_array[$i1]', '$author1_array[$i1]', '$year1_array[$i1]', '$citation_array[$i1]', '$note1_array[$i1]', '$doi2_array[$i1]', '$title2_array[$i1]', '$author2_array[$i1]', '$year2_array[$i1]', '$ID_array[$i1]')";
$string_insert = $string_insert1 . ' ' . $string_insert2;
$sele = $string_insert;
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
}
//unset($http1_array);unset($doi1_array);unset($title1_array);unset($author1_array);unset($year1_array);unset($citation_array);unset($note1_array);unset($doi2_array);unset($title2_array);unset($author2_array);unset($year2_array);unset($ID_array); 
//print_r($title1_array);



// TABLE Citing-retracted (FILL COLUMNS)
$counter_array = $counter_array;
$sele = "SELECT * FROM CitingRetracted WHERE title1 LIKE '%$name%' LIMIT $LIMIT OFFSET 0;"; // OBS: Comments and Remarks (use title2)
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {	    
//////		echo '<h4>';
	while($row = $result[1]->fetch_assoc ()) {
//		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
				$doi1 = $row['doi1'];
				$title1 = $row['title1'];
				$author1 = $row['author1'];
				$year1 = $row['year1'];
				$doi2 = $row['doi2'];
				$title2 = $row['title2'];
				$author2 = $row['author2'];
				$year2 = $row['year2'];
				//$http1 = $row['http1'];
				//$citation = $row['citation'];
				//$note1 = $row['note1'];
				//$ID = $row['ID'];
				
				$tablename1_array[$counter_array] = 'WL-Citing-retracted';
				$doi1_array[$counter_array] = $doi1;
				$title1_array[$counter_array] = $title1;
				$author1_array[$counter_array] = $author1;
				$year1_array[$counter_array] = $year1;
				$doi2_array[$counter_array] = $doi2;
				$title2_array[$counter_array] = $title2;
				$author2_array[$counter_array] = $author2;
				$year2_array[$counter_array] = $year2;
				$http1_array[$counter_array] = 'N/A';
				$citation_array[$counter_array] = 'N/A';
				$note1_array[$counter_array] = 'N/A';
				$ID_array[$counter_array] = $counter_array;
		
		 //print "<CENTER>$title1</CENTER>"; 
		 //echo "<br />\n";	
		 $counter_array = $counter_array+1;
		}
//////		echo '</h4>';
	}
$string_insert1 = "INSERT INTO Results_query (tablename1,http1,doi1,title1,author1,year1,citation,note1,doi2,title2,author2,year2,ID) VALUES";
$loop_n =  sizeof($title1_array)+1;
for($i=1; $i<=$loop_n; $i++){
//echo "The number is " . $i . "<br>";
$i1 = $i - 1;
$string_insert2 = " ('$tablename1_array[$i1]', '$http1_array[$i1]', '$doi1_array[$i1]', '$title1_array[$i1]', '$author1_array[$i1]', '$year1_array[$i1]', '$citation_array[$i1]', '$note1_array[$i1]', '$doi2_array[$i1]', '$title2_array[$i1]', '$author2_array[$i1]', '$year2_array[$i1]', '$ID_array[$i1]')";
$string_insert = $string_insert1 . ' ' . $string_insert2;
$sele = $string_insert;
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
}
//unset($http1_array);unset($doi1_array);unset($title1_array);unset($author1_array);unset($year1_array);unset($citation_array);unset($note1_array);unset($doi2_array);unset($title2_array);unset($author2_array);unset($year2_array);unset($ID_array); 
//print_r($title1_array);
//


// TABLE Remarks-unclassified (FILL COLUMNS)
$counter_array = $counter_array;
$sele = "SELECT * FROM Remark2 WHERE title2 LIKE '%$name%' LIMIT $LIMIT OFFSET 0;"; // OBS: Comments and Remarks (use title2)
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {	    
//////		echo '<h4>';
	while($row = $result[1]->fetch_assoc ()) {
//		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
				$doi1 = $row['doi1'];
				$title1 = $row['title1'];
				$author1 = $row['author1'];
				$year1 = $row['year1'];
				$doi2 = $row['doi2'];
				$title2 = $row['title2'];
				$author2 = $row['author2'];
				$year2 = $row['year2'];
				//$http1 = $row['http1'];
				$citation = $row['citation'];
				//$note1 = $row['note1'];
				//$ID = $row['ID'];
				
				$tablename1_array[$counter_array] = 'WL-Citations (unclassified)';
				$doi1_array[$counter_array] = $doi1;
				$title1_array[$counter_array] = $title1;
				$author1_array[$counter_array] = $author1;
				$year1_array[$counter_array] = $year1;
				$doi2_array[$counter_array] = $doi2;
				$title2_array[$counter_array] = $title2;
				$author2_array[$counter_array] = $author2;
				$year2_array[$counter_array] = $year2;
				$http1_array[$counter_array] = 'N/A';
				$citation_array[$counter_array] = $citation;
				$note1_array[$counter_array] = 'N/A';
				$ID_array[$counter_array] = $counter_array;
		
		 //print "<CENTER>$title1</CENTER>"; 
		 //echo "<br />\n";	
		 $counter_array = $counter_array+1;
		}
//////		echo '</h4>';
	}
$string_insert1 = "INSERT INTO Results_query (tablename1,http1,doi1,title1,author1,year1,citation,note1,doi2,title2,author2,year2,ID) VALUES";
$loop_n =  sizeof($title1_array)+1;
for($i=1; $i<=$loop_n; $i++){
//echo "The number is " . $i . "<br>";
$i1 = $i - 1;
$string_insert2 = " ('$tablename1_array[$i1]', '$http1_array[$i1]', '$doi1_array[$i1]', '$title1_array[$i1]', '$author1_array[$i1]', '$year1_array[$i1]', '$citation_array[$i1]', '$note1_array[$i1]', '$doi2_array[$i1]', '$title2_array[$i1]', '$author2_array[$i1]', '$year2_array[$i1]', '$ID_array[$i1]')";
$string_insert = $string_insert1 . ' ' . $string_insert2;
$sele = $string_insert;
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
}
//unset($http1_array);unset($doi1_array);unset($title1_array);unset($author1_array);unset($year1_array);unset($citation_array);unset($note1_array);unset($doi2_array);unset($title2_array);unset($author2_array);unset($year2_array);unset($ID_array); 
//print_r($title1_array);
//



// TABLE Remarks-positive (FILL COLUMNS)
$counter_array = $counter_array;
$sele = "SELECT * FROM remark_positive WHERE title2 LIKE '%$name%' LIMIT $LIMIT OFFSET 0;"; // OBS: Comments and Remarks (use title2)
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {	    
//////		echo '<h4>';
	while($row = $result[1]->fetch_assoc ()) {
//		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
				$doi1 = $row['doi1'];
				$title1 = $row['title1'];
				$author1 = $row['author1'];
				$year1 = $row['year1'];
				$doi2 = $row['doi2'];
				$title2 = $row['title2'];
				$author2 = $row['author2'];
				$year2 = $row['year2'];
				//$http1 = $row['http1'];
				$citation = $row['citation'];
				//$note1 = $row['note1'];
				//$ID = $row['ID'];
				
				$tablename1_array[$counter_array] = 'WL-Citations (positive)';
				$doi1_array[$counter_array] = $doi1;
				$title1_array[$counter_array] = $title1;
				$author1_array[$counter_array] = $author1;
				$year1_array[$counter_array] = $year1;
				$doi2_array[$counter_array] = $doi2;
				$title2_array[$counter_array] = $title2;
				$author2_array[$counter_array] = $author2;
				$year2_array[$counter_array] = $year2;
				$http1_array[$counter_array] = 'N/A';
				$citation_array[$counter_array] = $citation;
				$note1_array[$counter_array] = 'N/A';
				$ID_array[$counter_array] = $counter_array;
		
		 //print "<CENTER>$title1</CENTER>"; 
		 //echo "<br />\n";	
		 $counter_array = $counter_array+1;
		}
//////		echo '</h4>';
	}
$string_insert1 = "INSERT INTO Results_query (tablename1,http1,doi1,title1,author1,year1,citation,note1,doi2,title2,author2,year2,ID) VALUES";
$loop_n =  sizeof($title1_array)+1;
for($i=1; $i<=$loop_n; $i++){
//echo "The number is " . $i . "<br>";
$i1 = $i - 1;
$string_insert2 = " ('$tablename1_array[$i1]', '$http1_array[$i1]', '$doi1_array[$i1]', '$title1_array[$i1]', '$author1_array[$i1]', '$year1_array[$i1]', '$citation_array[$i1]', '$note1_array[$i1]', '$doi2_array[$i1]', '$title2_array[$i1]', '$author2_array[$i1]', '$year2_array[$i1]', '$ID_array[$i1]')";
$string_insert = $string_insert1 . ' ' . $string_insert2;
$sele = $string_insert;
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
}
//unset($http1_array);unset($doi1_array);unset($title1_array);unset($author1_array);unset($year1_array);unset($citation_array);unset($note1_array);unset($doi2_array);unset($title2_array);unset($author2_array);unset($year2_array);unset($ID_array); 
//print_r($title1_array);
//



// TABLE Remarks-neutral (FILL COLUMNS)
$counter_array = $counter_array;
$sele = "SELECT * FROM remark_neutral WHERE title2 LIKE '%$name%' LIMIT $LIMIT OFFSET 0;"; // OBS: Comments and Remarks (use title2)
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {	    
//////		echo '<h4>';
	while($row = $result[1]->fetch_assoc ()) {
//		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
				$doi1 = $row['doi1'];
				$title1 = $row['title1'];
				$author1 = $row['author1'];
				$year1 = $row['year1'];
				$doi2 = $row['doi2'];
				$title2 = $row['title2'];
				$author2 = $row['author2'];
				$year2 = $row['year2'];
				//$http1 = $row['http1'];
				$citation = $row['citation'];
				//$note1 = $row['note1'];
				//$ID = $row['ID'];
				
				$tablename1_array[$counter_array] = 'WL-Citations (neutral)';
				$doi1_array[$counter_array] = $doi1;
				$title1_array[$counter_array] = $title1;
				$author1_array[$counter_array] = $author1;
				$year1_array[$counter_array] = $year1;
				$doi2_array[$counter_array] = $doi2;
				$title2_array[$counter_array] = $title2;
				$author2_array[$counter_array] = $author2;
				$year2_array[$counter_array] = $year2;
				$http1_array[$counter_array] = 'N/A';
				$citation_array[$counter_array] = $citation;
				$note1_array[$counter_array] = 'N/A';
				$ID_array[$counter_array] = $counter_array;
		
		 //print "<CENTER>$title1</CENTER>"; 
		 //echo "<br />\n";	
		 $counter_array = $counter_array+1;
		}
//////		echo '</h4>';
	}
$string_insert1 = "INSERT INTO Results_query (tablename1,http1,doi1,title1,author1,year1,citation,note1,doi2,title2,author2,year2,ID) VALUES";
$loop_n =  sizeof($title1_array)+1;
for($i=1; $i<=$loop_n; $i++){
//echo "The number is " . $i . "<br>";
$i1 = $i - 1;
$string_insert2 = " ('$tablename1_array[$i1]', '$http1_array[$i1]', '$doi1_array[$i1]', '$title1_array[$i1]', '$author1_array[$i1]', '$year1_array[$i1]', '$citation_array[$i1]', '$note1_array[$i1]', '$doi2_array[$i1]', '$title2_array[$i1]', '$author2_array[$i1]', '$year2_array[$i1]', '$ID_array[$i1]')";
$string_insert = $string_insert1 . ' ' . $string_insert2;
$sele = $string_insert;
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
}
//unset($http1_array);unset($doi1_array);unset($title1_array);unset($author1_array);unset($year1_array);unset($citation_array);unset($note1_array);unset($doi2_array);unset($title2_array);unset($author2_array);unset($year2_array);unset($ID_array); 
//print_r($title1_array);
//


// TABLE Remarks-caveat (FILL COLUMNS)
$counter_array = $counter_array;
$sele = "SELECT * FROM remark_positive WHERE title2 LIKE '%$name%' LIMIT $LIMIT OFFSET 0;"; // OBS: Comments and Remarks (use title2)
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {	    
//////		echo '<h4>';
	while($row = $result[1]->fetch_assoc ()) {
//		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
				$doi1 = $row['doi1'];
				$title1 = $row['title1'];
				$author1 = $row['author1'];
				$year1 = $row['year1'];
				$doi2 = $row['doi2'];
				$title2 = $row['title2'];
				$author2 = $row['author2'];
				$year2 = $row['year2'];
				//$http1 = $row['http1'];
				$citation = $row['citation'];
				//$note1 = $row['note1'];
				//$ID = $row['ID'];
				
				$tablename1_array[$counter_array] = 'WL-Citations (negative)';
				$doi1_array[$counter_array] = $doi1;
				$title1_array[$counter_array] = $title1;
				$author1_array[$counter_array] = $author1;
				$year1_array[$counter_array] = $year1;
				$doi2_array[$counter_array] = $doi2;
				$title2_array[$counter_array] = $title2;
				$author2_array[$counter_array] = $author2;
				$year2_array[$counter_array] = $year2;
				$http1_array[$counter_array] = 'N/A';
				$citation_array[$counter_array] = $citation;
				$note1_array[$counter_array] = 'N/A';
				$ID_array[$counter_array] = $counter_array;
		
		 //print "<CENTER>$title1</CENTER>"; 
		 //echo "<br />\n";	
		 $counter_array = $counter_array+1;
		}
//////		echo '</h4>';
	}
$string_insert1 = "INSERT INTO Results_query (tablename1,http1,doi1,title1,author1,year1,citation,note1,doi2,title2,author2,year2,ID) VALUES";
$loop_n =  sizeof($title1_array)+1;
for($i=1; $i<=$loop_n; $i++){
//echo "The number is " . $i . "<br>";
$i1 = $i - 1;
$string_insert2 = " ('$tablename1_array[$i1]', '$http1_array[$i1]', '$doi1_array[$i1]', '$title1_array[$i1]', '$author1_array[$i1]', '$year1_array[$i1]', '$citation_array[$i1]', '$note1_array[$i1]', '$doi2_array[$i1]', '$title2_array[$i1]', '$author2_array[$i1]', '$year2_array[$i1]', '$ID_array[$i1]')";
$string_insert = $string_insert1 . ' ' . $string_insert2;
$sele = $string_insert;
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
}
//unset($http1_array);unset($doi1_array);unset($title1_array);unset($author1_array);unset($year1_array);unset($citation_array);unset($note1_array);unset($doi2_array);unset($title2_array);unset($author2_array);unset($year2_array);unset($ID_array); 
//print_r($title1_array);
//


// TABLE Improper-citation (FILL COLUMNS)
$counter_array = $counter_array;
$sele = "SELECT * FROM ImproperCitation WHERE title1 LIKE '%$name%' LIMIT $LIMIT OFFSET 0;"; // OBS: Comments and Remarks (use title2)
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {	    
//////		echo '<h4>';
	while($row = $result[1]->fetch_assoc ()) {
//		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
				$doi1 = $row['doi1'];
				$title1 = $row['title1'];
				$author1 = $row['author1'];
				$year1 = $row['year1'];
				$doi2 = $row['doi2'];
				$title2 = $row['title2'];
				$author2 = $row['author2'];
				$year2 = $row['year2'];
				//$http1 = $row['http1'];
				$citation = $row['citation'];
				//$note1 = $row['note1'];
				//$ID = $row['ID'];
				
				$tablename1_array[$counter_array] = 'WL-Improper-citation';
				$doi1_array[$counter_array] = $doi1;
				$title1_array[$counter_array] = $title1;
				$author1_array[$counter_array] = $author1;
				$year1_array[$counter_array] = $year1;
				$doi2_array[$counter_array] = $doi2;
				$title2_array[$counter_array] = $title2;
				$author2_array[$counter_array] = $author2;
				$year2_array[$counter_array] = $year2;
				$http1_array[$counter_array] = 'N/A';
				$citation_array[$counter_array] = $citation;
				$note1_array[$counter_array] = 'N/A';
				$ID_array[$counter_array] = $counter_array;
		
		 //print "<CENTER>$title1</CENTER>"; 
		 //echo "<br />\n";	
		 $counter_array = $counter_array+1;
		}
//////		echo '</h4>';
	}
$string_insert1 = "INSERT INTO Results_query (tablename1,http1,doi1,title1,author1,year1,citation,note1,doi2,title2,author2,year2,ID) VALUES";
$loop_n =  sizeof($title1_array)+1;
for($i=1; $i<=$loop_n; $i++){
//echo "The number is " . $i . "<br>";
$i1 = $i - 1;
$string_insert2 = " ('$tablename1_array[$i1]', '$http1_array[$i1]', '$doi1_array[$i1]', '$title1_array[$i1]', '$author1_array[$i1]', '$year1_array[$i1]', '$citation_array[$i1]', '$note1_array[$i1]', '$doi2_array[$i1]', '$title2_array[$i1]', '$author2_array[$i1]', '$year2_array[$i1]', '$ID_array[$i1]')";
$string_insert = $string_insert1 . ' ' . $string_insert2;
$sele = $string_insert;
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
}
//unset($http1_array);unset($doi1_array);unset($title1_array);unset($author1_array);unset($year1_array);unset($citation_array);unset($note1_array);unset($doi2_array);unset($title2_array);unset($author2_array);unset($year2_array);unset($ID_array); 
//print_r($title1_array);
//
//
//






// CREATING VARIABLES FOR COUNTERS
$counter1 = 0;
$counter2 = 0;
$counter3 = 0;
$counter4 = 0;
$counter5 = 0;
$counter6 = 0;
$counter7 = 0;
$counter8 = 0;
$counter9 = 0;
$counter10 = 0;
$counter11 = 0;

// COUNTING ELEMENTS FROM TABLES (COUNTERS)
// Letters
$sele = "SELECT * FROM Letters WHERE title1 LIKE '%$name%'";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
	while($row = $result[1]->fetch_assoc ()) {
		//$counter1++;
		$counter1 = $counter1+1;
	}
	}

// Notes_positive
$sele = "SELECT * FROM Notes_positive WHERE title1 LIKE '%$name%'";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
	while($row = $result[1]->fetch_assoc ()) {
		//$counter2++;
		$counter2 = $counter2+1;
	}
	}
// Notes_negative
$sele = "SELECT * FROM Notes_negative WHERE title1 LIKE '%$name%'";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
	while($row = $result[1]->fetch_assoc ()) {
		//$counter3++;
		$counter3 = $counter3+1;
	}
	}
// Comments
$sele = "SELECT * FROM Comments WHERE title2 LIKE '%$name%'";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {	    
	while($row = $result[1]->fetch_assoc ()) {
		//$counter4++;
		$counter4 = $counter4+1;
	}
	}
// Retracted
$sele = "SELECT * FROM Retracted WHERE title1 LIKE '%$name%'";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
	while($row = $result[1]->fetch_assoc ()) {
		//$counter5++;
		$counter5 = $counter5+1;
	}
	}
// Citing-retracted
$sele = "SELECT * FROM CitingRetracted WHERE title1 LIKE '%$name%'";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
	while($row = $result[1]->fetch_assoc ()) {
		//$counter6++;
		$counter6 = $counter6+1;
	}
	}
// Remarks
$sele = "SELECT * FROM Remark2 WHERE title2 LIKE '%$name%'";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
	while($row = $result[1]->fetch_assoc ()) {
		//$counter7++;
		$counter7 = $counter7+1;
	}
	}
// Remarks (positive)
$sele = "SELECT * FROM remark_positive WHERE title2 LIKE '%$name%'";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
	while($row = $result[1]->fetch_assoc ()) {
		//$counter8++;
		$counter8 = $counter8+1;
	}
	}
// Remarks (neutral)
$sele = "SELECT * FROM remark_neutral WHERE title2 LIKE '%$name%'";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
	while($row = $result[1]->fetch_assoc ()) {
		//$counter9++;
		$counter9 = $counter9+1;
	}
	}
// Remarks (caveat)
$sele = "SELECT * FROM remark_negative WHERE title2 LIKE '%$name%'";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
	while($row = $result[1]->fetch_assoc ()) {
		//$counter10++;
		$counter10 = $counter10+1;
	}
	}
// Improper-citations
$sele = "SELECT * FROM ImproperCitation WHERE title1 LIKE '%$name%'";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
	while($row = $result[1]->fetch_assoc ()) {
		//$counter11++;
		$counter11 = $counter11+1;
	}
	}



$counter_all = $counter1 + $counter2 + $counter3 + $counter4 + $counter5 + $counter6 + $counter7 + $counter8 + $counter9 + $counter10 + $counter11;

if ($counter_all > 0) {
// headings
//echo "<br />\n";
//echo '<div style="font-size:22px; text-align: center;">We provide a maximum of <strong>ten</strong> results in this page, but all results are available in each database of Wikiletters.</div>';
//echo "<br />\n";
}
//2-CLOSE
?>

<?php //3-OPEN
// DISPLAYING THE RESULTS IN TABLES //

$counter_option = 1;
if ($counter_option == 1) {
if ($counter_all > 0) {
echo "<br />\n";
$counter1s = (string)$counter1;
$counter2s = (string)$counter2;
$counter3s = (string)$counter3;
$counter4s = (string)$counter4;
$counter5s = (string)$counter5;
$counter6s = (string)$counter6;
$counter7s = (string)$counter7;
$counter8s = (string)$counter8;
$counter9s = (string)$counter9;
$counter10s = (string)$counter10;
$counter11s = (string)$counter11;
//<div id="second" style="text-align: center;">get_search_form();</div>

// echo "[wpdatatable id=1 title1=".$row['testing']."]"; NOT WORKING
//echo "[insert_php] [wpdatatable id=1] [/insert_php]"; NOT WORKING
	
	
echo '<div style="font-size:22px; text-align: center;">This search-box will simultaneously check an <strong>article title</strong> or <strong>word(s)</strong> in all our databases.</div>';
//echo '<div style="font-size:22px; text-align: center;">(Letters, Comments, Retracted, Citing-retracted, Remarks, and Notes).</div>';
get_search_form();
//echo "<br />\n";
//
//echo '<div style="border: 1px solid #aaa;"></div>';

	
// spaces due to fixed heading
echo "<br />\n";
echo "<br />\n";

	
	
		echo '<h4>';
		echo '<p>';
		echo '<table class="greenTableResult"> <b><center>In searching for "'.$name.'", Wikiletters has found a total of "'.$counter_all.'" pieces of information.</center></b>';
		echo '<p>';
		echo '<tr>';
		echo '<th bgcolor="#b1b1c9">Letters</th>';
		echo '<th bgcolor="#ddd7d7">Notes (positive)</th>';
		echo '<th bgcolor="#ddd7d7">Notes (caveat)</th>';
		echo '<th bgcolor="#9398bf">Comments</th>';
		echo '<th bgcolor="#cbd1ed">Retracted</th>';
		echo '<th bgcolor="#cbd1ed">Citing-retracted</th>';
		echo '<th bgcolor="#9bb9f7">Citations (unclassified)</th>';
		echo '<th bgcolor="#9bb9f7">Citations (positive)</th>';
		echo '<th bgcolor="#9bb9f7">Citations (neutral)</th>';
		echo '<th bgcolor="#9bb9f7">Citations (negative)</th>';
		echo '<th bgcolor="#9398bf">Improper-citations</th>';
		echo '</tr>';
		echo '<tr>';
		echo '<td bgcolor="#b1b1c9">'.$counter1s.'</th>';
		echo '<td bgcolor="#ddd7d7">'.$counter2s.'</th>';
		echo '<td bgcolor="#ddd7d7">'.$counter3s.'</th>';
		echo '<td bgcolor="#9398bf">'.$counter4s.'</th>';
		echo '<td bgcolor="#cbd1ed">'.$counter5s.'</th>';
		echo '<td bgcolor="#cbd1ed">'.$counter6s.'</th>';
		echo '<td bgcolor="#9bb9f7">'.$counter7s.'</th>';
		echo '<td bgcolor="#9bb9f7">'.$counter8s.'</th>';
		echo '<td bgcolor="#9bb9f7">'.$counter9s.'</th>';
		echo '<td bgcolor="#9bb9f7">'.$counter10s.'</th>';
		echo '<td bgcolor="#9398bf">'.$counter11s.'</th>';
		echo '</tr>';
//3-CLOSE
?>

<?php
		echo '</tr>';
		echo '</table>';
		echo '</p>';
		echo '</h4>';
		//echo "<br />\n";

} // if ($counter_option == 1) {
} // if ($counter_all > 0) {
?>

<?php
if ($counter_all > 0) {
//echo "<br />\n";
echo '<div style="font-size:22px; text-align: center;">The tables below provide per database, a maximum of <strong>ten rows</strong> related to your search.</div>';
//echo '<div style="font-size:22px; text-align: center;">If you are not redirected to complete results in approximately <strong>20 seconds</strong>, please (<a href="https://wikiletters.org/download-query/" target="_blank">Click here</a>).</div>';
//echo "<br />\n";
//

echo '<html> <head> <meta http-equiv="refresh" content="255;url=https://wikiletters.org/download-query/" target="_blank"/> </head> <body>'; // same tab WORKING

//

	
// BELOW DID NOT WORK
//echo "<script language=\\"javascript\\">window.open(\\"https://wikiletters.org/download-query/\\",\\"_blank\\");</script>"; // NOT WORKING
//echo "<meta http-equiv="refresh" content="5; url=javascript:window.open('https://wikiletters.org/download-query/','_blank');">" // NOT WORKING
//echo "<script type="text/javascript" language="Javascript">window.open('https://wikiletters.org/query-empty/');</script>" // NOT WORKING
//echo "<script type="text/javascript">window.open('https://wikiletters.org/download-query/');</script>" // NOT WORKING
//
//
} else {
header("Location: https://wikiletters.org/query-empty/");
}
?>

<p style="font-size:22px; text-align:center;">You will be redirected in approximately <span id="counter">300</span> second(s) to the page containing all results ready for download.</p>
<script type="text/javascript">
function countdown() {
     var i = document.getElementById('counter');
     // if (parseInt(i.innerHTML)<=0) {
     //    location.href = 'https://wikiletters.org/download-query/';
     // }
     i.innerHTML = parseInt(i.innerHTML)-1;
}
setInterval(function(){ countdown(); },1000);
</script>

<?php
echo '<div style="font-size:22px; text-align: center;">To shortly get all results in various format, then please (<a href="https://wikiletters.org/download-query/" target="_blank">Click here</a>).</div>';
echo '<div style="font-size:12px; text-align: center;">Prototype page to reduce time on IIS or Apache (<a href="https://wikiletters.org/search_download.php/" target="_blank">Please do not use this button</a>).</div>';
?>

<?php //4-OPEN
echo "<br />\n";
// CREATING THE TABLES

// TALBE Letters
$sele = "SELECT * FROM Letters WHERE title1 LIKE '%$name%' LIMIT 10 OFFSET 0;";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
		echo '<h4>';
		echo '<p>';
		echo '<table class="greenTableResult"> <b><center> Letters </center></b>';
		echo '<p>';
		echo '<tr>';
		echo '<th bgcolor="#BAE1FF">Title</th>';
		echo '<th bgcolor="#BAE1FF">Author(s)</th>';
		echo '</tr>';
	while($row = $result[1]->fetch_assoc ()) {
		echo '<tr>';
		echo '<td bgcolor="#BAE1FF"> '.utf8_encode ($row['title1']);
		echo '<td bgcolor="#BAE1FF"> '.utf8_encode ($row['author1']);
		echo '</tr>';
	}
		echo '</table>';
		echo '</p>';
		echo '</h4>';
	}


// TALBE Notes_positive
$sele = "SELECT * FROM Notes_positive WHERE title1 LIKE '%$name%' LIMIT 10 OFFSET 0;";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
		echo '<h4>';
		echo '<p>';
		echo '<table class="greenTableResult"> <b><center> Notes (positive) </center></b>';
		echo '<p>';
		echo '<tr>';
		echo '<th bgcolor="#a0d2ff">Title</th>';
		echo '<th bgcolor="#a0d2ff">Author(s)</th>';
		echo '</tr>';	
	while($row = $result[1]->fetch_assoc ()) {
		echo '<tr>';
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['author1']);
		echo '</tr>';
	}
		echo '</table>';
		echo '</p>';
		echo '</h4>';
	}

// TALBE Notes_negative
$sele = "SELECT * FROM Notes_negative WHERE title1 LIKE '%$name%' LIMIT 10 OFFSET 0;";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
		echo '<h4>';
		echo '<p>';
		echo '<table class="greenTableResult"> <b><center> Notes (caveat and critiques) </center></b>';
		echo '<p>';
		echo '<tr>';
		echo '<th bgcolor="#a0d2ff">Title</th>';
		echo '<th bgcolor="#a0d2ff">Author(s)</th>';
		echo '</tr>';	
	while($row = $result[1]->fetch_assoc ()) {
		echo '<tr>';
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['author1']);
		echo '</tr>';
	}
		echo '</table>';
		echo '</p>';
		echo '</h4>';
	}


// TABLE Comments
$sele = "SELECT * FROM Comments WHERE title2 LIKE '%$name%' LIMIT 10 OFFSET 0;";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {	    
		echo '<h4>';
		echo '<p>';
		echo '<table class="greenTableResult"> <b><center> Comments </center></b>';
		echo '<p>';
		echo '<tr>';
		echo '<th bgcolor="#a0d2ff">Title (Article citing)</th>';
		echo '<th bgcolor="#a0d2ff">Author(s) (Article citing)</th>';
		echo '<th bgcolor="#b7ffd1">Title (Article being cited)</th>';
		echo '<th bgcolor="#b7ffd1">Author(s) (Article being cited)</th>';
		//echo '<th >Title Cited </th>';a
		//echo '<th >Author(s) Cited</th>';
		echo '</tr>';
	while($row = $result[1]->fetch_assoc ()) {
		echo '<tr>';
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['author1']);
		echo '<td bgcolor="#b7ffd1"> '.utf8_encode ($row['title2']);
		echo '<td bgcolor="#b7ffd1"> '.utf8_encode ($row['author2']);
		//echo '<td> '.utf8_encode ($row['title2']);
		//echo '<td> '.utf8_encode ($row['author2']);
		echo '</tr>';
		}
		echo '</table>';
		echo '</p>';
		echo '</h4>';
	}

// TALBE Retracted
$sele = "SELECT * FROM Retracted WHERE title1 LIKE '%$name%' LIMIT 10 OFFSET 0;";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
		echo '<h4>';
		echo '<p>';
		echo '<table class="greenTableResult"> <b><center> Retracted </center></b>';
		echo '<p>';
		echo '<tr>';
		echo '<th bgcolor="#a0d2ff">Title</th>';
		echo '<th bgcolor="#a0d2ff">Author(s)</th>';
		echo '</tr>';	
	while($row = $result[1]->fetch_assoc ()) {
		echo '<tr>';
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['author1']);
		echo '</tr>';
	}
		echo '</table>';
		echo '</p>';
		echo '</h4>';
	}

// TABLE CitingRetracted
$sele = "SELECT * FROM CitingRetracted WHERE title1 LIKE '%$name%' LIMIT 10 OFFSET 0;";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
		echo '<h4>';
		echo '<p>';
		echo '<table class="greenTableResult"> <b><center> Citing-Retracted </center></b>';
		echo '<p>';
		echo '<tr>';
		echo '<th bgcolor="#a0d2ff">Title (Article citing)</th>';
		echo '<th bgcolor="#a0d2ff">Author(s) (Article citing)</th>';
		echo '<th bgcolor="#b7ffd1">Title (Article being cited)</th>';
		echo '<th bgcolor="#b7ffd1">Author(s) (Article being cited)</th>';
		//echo '<th >Title Cited </th>';
		//echo '<th >Author(s) Cited</th>';
		echo '</tr>'; 
	while($row = $result[1]->fetch_assoc ()) {
		echo '<tr>';
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['author1']);
		echo '<td bgcolor="#b7ffd1"> '.utf8_encode ($row['title2']);
		echo '<td bgcolor="#b7ffd1"> '.utf8_encode ($row['author2']);
		//echo '<td> '.utf8_encode ($row['title2']);
		//echo '<td> '.utf8_encode ($row['author2']);
		echo '</tr>';
	}
		echo '</table>';
		echo '</p>';
		echo '</h4>';
	}

// TABLE Remark
$sele = "SELECT * FROM Remark2 WHERE title2 LIKE '%$name%' LIMIT 10 OFFSET 0;";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
		echo '<h4>';
		echo '<p>';
		echo '<table class="greenTableResult"> <b><center> Citations (unclassified) </center></b>';
		echo '<p>';
		echo '<tr>';
		echo '<th bgcolor="#a0d2ff">Title (Article citing)</th>';
		echo '<th bgcolor="#a0d2ff">Author(s) (Article citing)</th>';
		echo '<th bgcolor="#b7ffd1">Title (Article being cited)</th>';
		echo '<th bgcolor="#b7ffd1">Author(s) (Article being cited)</th>';
		//echo '<th >Title Cited</th>';
		//echo '<th >Author(s) Cited</th>';
		echo '</tr>';
	while($row = $result[1]->fetch_assoc ()) {
		echo '<tr>';
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['author1']);
		echo '<td bgcolor="#b7ffd1"> '.utf8_encode ($row['title2']);
		echo '<td bgcolor="#b7ffd1"> '.utf8_encode ($row['author2']);
		//echo '<td> '.utf8_encode ($row['title2']);
		//echo '<td> '.utf8_encode ($row['author2']);
		echo '</tr>';
	}
		echo '</table>';
		echo '</p>';
		echo '</h4>';
	}

// TABLE remark_positive
$sele = "SELECT * FROM remark_positive WHERE title2 LIKE '%$name%' LIMIT 10 OFFSET 0;";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
		echo '<h4>';
		echo '<p>';
		echo '<table class="greenTableResult"> <b><center> Citations (positive and relevant) </center></b>';
		echo '<p>';
		echo '<tr>';
		echo '<th bgcolor="#a0d2ff">Title (Article citing)</th>';
		echo '<th bgcolor="#a0d2ff">Author(s) (Article citing)</th>';
		echo '<th bgcolor="#b7ffd1">Title (Article being cited)</th>';
		echo '<th bgcolor="#b7ffd1">Author(s) (Article being cited)</th>';
		//echo '<th >Title Cited</th>';
		//echo '<th >Author(s) Cited</th>';
		echo '</tr>';
	while($row = $result[1]->fetch_assoc ()) {
		echo '<tr>';
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['author1']);
		echo '<td bgcolor="#b7ffd1"> '.utf8_encode ($row['title2']);
		echo '<td bgcolor="#b7ffd1"> '.utf8_encode ($row['author2']);
		//echo '<td> '.utf8_encode ($row['title2']);
		//echo '<td> '.utf8_encode ($row['author2']);
		echo '</tr>';
	}
		echo '</table>';
		echo '</p>';
		echo '</h4>';
	}

// TABLE remark_neutral
$sele = "SELECT * FROM remark_neutral WHERE title2 LIKE '%$name%' LIMIT 10 OFFSET 0;";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
		echo '<h4>';
		echo '<p>';
		echo '<table class="greenTableResult"> <b><center> Citations (neutral) </center></b>';
		echo '<p>';
		echo '<tr>';
		echo '<th bgcolor="#a0d2ff">Title (Article citing)</th>';
		echo '<th bgcolor="#a0d2ff">Author(s) (Article citing)</th>';
		echo '<th bgcolor="#b7ffd1">Title (Article being cited)</th>';
		echo '<th bgcolor="#b7ffd1">Author(s) (Article being cited)</th>';
		//echo '<th >Title Cited</th>';
		//echo '<th >Author(s) Cited</th>';
		echo '</tr>';
	while($row = $result[1]->fetch_assoc ()) {
		echo '<tr>';
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['author1']);
		echo '<td bgcolor="#b7ffd1"> '.utf8_encode ($row['title2']);
		echo '<td bgcolor="#b7ffd1"> '.utf8_encode ($row['author2']);
		//echo '<td> '.utf8_encode ($row['title2']);
		//echo '<td> '.utf8_encode ($row['author2']);
		echo '</tr>';
	}
		echo '</table>';
		echo '</p>';
		echo '</h4>';
	}

// TABLE remark_negative
$sele = "SELECT * FROM remark_negative WHERE title2 LIKE '%$name%' LIMIT 10 OFFSET 0;";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
		echo '<h4>';
		echo '<p>';
		echo '<table class="greenTableResult"> <b><center> Citations (negative) </center></b>';
		echo '<p>';
		echo '<tr>';
		echo '<th bgcolor="#a0d2ff">Title (Article citing)</th>';
		echo '<th bgcolor="#a0d2ff">Author(s) (Article citing)</th>';
		echo '<th bgcolor="#b7ffd1">Title (Article being cited)</th>';
		echo '<th bgcolor="#b7ffd1">Author(s) (Article being cited)</th>';
		//echo '<th >Title Cited</th>';
		//echo '<th >Author(s) Cited</th>';
		echo '</tr>';
	while($row = $result[1]->fetch_assoc ()) {
		echo '<tr>';
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['author1']);
		echo '<td bgcolor="#b7ffd1"> '.utf8_encode ($row['title2']);
		echo '<td bgcolor="#b7ffd1"> '.utf8_encode ($row['author2']);
//		echo '<td> '.utf8_encode ($row['title2']);
//		echo '<td> '.utf8_encode ($row['author2']);
		echo '</tr>';
	}
		echo '</table>';
		echo '</p>';
		echo '</h4>';
	}


// TABLE ImproperCitation
$sele = "SELECT * FROM ImproperCitation WHERE title1 LIKE '%$name%' LIMIT 10 OFFSET 0;";
$result = $operacoes_sql->select_dados ( $sele, '', $mysqli );
	if ($result [0] == true) {
		echo '<h4>';
		echo '<p>';
		echo '<table class="greenTableResult"> <b><center> Improper-citations </center></b>';
		echo '<p>';
		echo '<tr>';
		echo '<th bgcolor="#a0d2ff">Title (Article citing)</th>';
		echo '<th bgcolor="#a0d2ff">Author(s) (Article citing)</th>';
		echo '<th bgcolor="#b7ffd1">Title (Article being cited)</th>';
		echo '<th bgcolor="#b7ffd1">Author(s) (Article being cited)</th>';
		//echo '<th >Title Cited</th>';
		//echo '<th >Author(s) Cited</th>';
		echo '</tr>';
	while($row = $result[1]->fetch_assoc ()) {
		echo '<tr>';
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['title1']);
		echo '<td bgcolor="#a0d2ff"> '.utf8_encode ($row['author1']);
		echo '<td bgcolor="#b7ffd1"> '.utf8_encode ($row['title2']);
		echo '<td bgcolor="#b7ffd1"> '.utf8_encode ($row['author2']);
//		echo '<td> '.utf8_encode ($row['title2']);
//		echo '<td> '.utf8_encode ($row['author2']);
		echo '</tr>';
	}
		echo '</table>';
		echo '</p>';
		echo '</h4>';
	}





// CLOSING THE PHP CODE PART
	$mysqli->close ();

//$counter_all = $counter1 + $counter2 + $counter3 + $counter4 + $counter5 + $counter6 + $counter7;

//4-CLOSE
?>

<?php //5-OPEN
//if ($counter_all == 0) {
// // This is in the PHP to provide a simple message on page
//echo "Our sincere apologies, but WikiLetters has not reached the article you are looking for. We very much appreciate your understanting."; 

// // This is in the PHP to provide a simple message on page
//echo "<br />\n";
//echo "<br />\n";
//echo "<br />\n";
//$message = "Our sincere apologies, but WikiLetters has not reached the article you are looking for. We very much appreciate your understanting.";
//echo $message;

// // This is in the PHP to provide a simple message on page
// //echo "<br />\n";
//echo "<br />\n";
//echo "<br />\n";
//$message = "Our sincere apologies, but WikiLetters has not reached the article you are looking for. We very much appreciate your understanting.";
//echo "<style='font size=22px;face=Arial;font-weight: bold;'>";
//print "<CENTER>$message</CENTER>";    
	  
// // This is in the PHP to provide a simple message on page
//echo "<br />\n";
//echo "<br />\n";
//echo '<div style="font-size:22px;color:black; text-align: center;">Our sincere apologies, but WikiLetters has not reached the article you are looking for. We very much appreciate your understanding. </div>';
//echo '<div style="font-size:22px; text-align: center;">Our sincere apologies, but WikiLetters has not reached the article you are looking for. We very much appreciate your understanding. </div>';

//}
//5-CLOSE
?>

<?php //6-OPEN
echo "<br />\n";
//echo '<div style="font-size:22px; text-align: center;">The search-box below can be used for searching other articles. </div>';
//6-CLOSE
//return $name;
?>

<!-- HTML short comment: -->
<!-- 
HTML long
comment
-->

<!-- <p>&nbsp;</p>          -->
<!--<hr style="height: 2px; border-top: 2px solid #ffffff;">       -->
<!--<p>&nbsp;</p>       -->
<?php get_footer(); // loading the footer?>