<html>
    <head>
        <title>Iot 2 Home</title>
    </head>
    <body>
        <?php 
            echo "<p>Lendo dados de Velocidade da Internet</p>";
            echo "ID - Data / Hora - Equipamento - Download - Upload";
            echo "<br>";

            $user = "root"; 
            $password = "Wall@1979"; 
            $database = "homeiot"; 

            # O hostname deve ser sempre localhost 
            $hostname = "locahost";
 
            # Conexão MySQL com PHP 7
            $conexao = mysqli_connect('localhost','root','Wall@1979');
            $banco = mysqli_select_db($conexao,'homeiot');
            mysqli_set_charset($conexao,'utf8');
 
            $sql = mysqli_query($conexao,"select * from iot_speedtest order by id desc") or die("Erro");
            
            while($dados=mysqli_fetch_assoc($sql))
                {   
                    echo $dados['id']." - ".$dados['timestamp']." - ".$dados['host']." - ".$dados['download']." - ".$dados['upload'].'<br>';
                }
        ?>
    </body>
</html>