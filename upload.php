<html>

<head>Загрузка  файлов на сервер</head>

<body>

  <form  enctype="multipart/form-data" action=""  method="post">

  <input  type="hidden" name="MAX_FILE_SIZE" value="300000"  />

  <input  type="file" name="uploadFile"/>

  <input  type="submit" name="upload" value="Загрузить"/>

  </form>

<?php

  print_r($_FILES);


  if(isset($_POST['upload'])){

  $folder = 'path/to/folder/';

  $uploadedFile = $folder.basename($_FILES['uploadFile']['name']);

  if(is_uploaded_file($_FILES['uploadFile']['tmp_name'])){

  if(move_uploaded_file($_FILES['uploadFile']['tmp_name'],

    $uploadedFile))

  {

     echo Файл загружен;

  }

  else

  {

     echo Во  время загрузки файла произошла ошибка;

  }

  }

  else

  {

   echo 'Файл не  загружен';

  }

  }

?>

</body>

</html>
