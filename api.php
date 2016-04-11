<?php
$json = '{"env":1,"assignment_id":2,"code_id":3,"klee_code":4,"c_code":5}';


$obj = json_decode($json);
$klee_code  = base64_decode($obj->{'klee_code'});
$c_code  = base64_decode($obj->{'c_code'});

$old_path = getcwd();
echo $old_path;
chdir('/home/klee/ATG');
$output = shell_exec('echo '.$klee_code.' > klee.c');
$output = shell_exec('echo '.$c_code.' > c.c');
$output = shell_exec('./Run.sh klee.c c.c');
echo $output;

$out_file = fopen("/home/klee/ATG/output", "r") or die("Unable to open file!");
echo fread($myfile,filesize("/home/klee/ATG/output"));
fclose($myfile);


chdir($old_path);

?>

