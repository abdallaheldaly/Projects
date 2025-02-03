<?php
$tasks = json_decode(file_get_contents('data/tasks.json'), true) ?: [];
$newTask = $_POST['task'];

if (!empty($newTask)) {
    $tasks[] = $newTask;
    file_put_contents('data/tasks.json', json_encode($tasks));
}

header('Location: index.php'); 
exit();
?>