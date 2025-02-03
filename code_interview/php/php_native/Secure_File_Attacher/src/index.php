<?php
// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['delete'])) {
        // Handle file deletion
        $fileToDelete = $_POST['delete'];
        if (file_exists($fileToDelete) && strpos($fileToDelete, 'uploads/') === 0) {
            unlink($fileToDelete);
        }
    } else {
        // Handle file upload
        if (isset($_FILES['file']) && $_FILES['file']['error'] === UPLOAD_ERR_OK) {
            $tmpName = $_FILES['file']['tmp_name'];
            $fileName = 'uploads/' . time() . '_' . basename($_FILES['file']['name']);
            
            // Validate file type (example: allow images only)
            $allowed = ['jpg', 'jpeg', 'png', 'gif', 'pdf'];
            $ext = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));
            
            if (in_array($ext, $allowed)) {
                move_uploaded_file($tmpName, $fileName);
            }
        }
    }
}

// Get list of uploaded files
$files = glob('uploads/*');
?>
<!DOCTYPE html>
<html>
<head>
    <title>File Manager</title>
</head>
<body>
    <h1>File Upload</h1>
    
    <!-- Upload Form -->
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>

    <h2>Uploaded Files</h2>
    <!-- File List -->
    <ul>
        <?php foreach ($files as $file): ?>
            <li>
                <a href="<?= $file ?>"><?= basename($file) ?></a>
                (<?= date('Y-m-d H:i:s', filemtime($file)) ?>)
                <form method="post" style="display: inline;">
                    <button type="submit" name="delete" value="<?= $file ?>">Delete</button>
                </form>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>