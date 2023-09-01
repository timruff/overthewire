<?php
	$passwd="5555";
	
	echo(gettype($passwd));
    echo("<br>");
	
	$type=strcmp($passwd,"1234");
    echo("<br>");

	echo(gettype($type));
	echo("<br>");
	echo($type);
	echo("<br>");

	if(!strcmp($passwd,"1234"))
    {
        echo "mot de passe 1234";
    }
    else
    {
            echo "mauvais mot de passe";
    }
?>