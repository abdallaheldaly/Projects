<?php
$tasks = json_decode(file_get_contents('data/tasks.json'), true);

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $id = $_POST['id'];
    $tasks[$id] = $_POST['task'];
    file_put_contents('data/tasks.json', json_encode($tasks));
    header('Location: index.php');
    exit;
}

$id = $_GET['id'];
$task = $tasks[$id] ?? '';
?>

<!DOCTYPE html>
<html>
<head>
    <title>Edit Task</title>
</head>
<body>
    <h1>Edit Task</h1>
    <form method="POST">
        <input type="hidden" name="id" value="<?= $id ?>">
        <input type="text" name="task" value="<?= htmlspecialchars($task) ?>" required>
        <button type="submit">Update</button>
    </form>
</body>
</html>