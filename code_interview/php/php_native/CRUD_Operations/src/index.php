<?php
$tasks = json_decode(file_get_contents('data/tasks.json'), true) ?: [];
?>

<!DOCTYPE html>
<html>
<head>
    <title>Task Manager</title>
</head>
<body>
    <h1>Task Manager</h1>
    
    <!-- Create Form -->
    <form action="create.php" method="POST">
        <input type="text" name="task" required>
        <button type="submit">Add Task</button>
    </form>

    <h2>Tasks List</h2>
    <ul>
        <?php foreach ($tasks as $id => $task): ?>
            <li>
                <?= htmlspecialchars($task) ?>
                <a href="edit.php?id=<?= $id ?>">Edit</a>
                <a href="delete.php?id=<?= $id ?>">Delete</a> 
            </li>
        <?php endforeach; ?> 
    </ul>
</body>
</html>