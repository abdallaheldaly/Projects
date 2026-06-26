<?php
use Psr\Http\Message\ResponseInterface as Response;
use Psr\Http\Message\ServerRequestInterface as Request;
use Slim\Factory\AppFactory;

//put

$app->put('/testput' ,function($Request ,$Response){

$data=$Request->getParsedBody();
$username=$data['UserName'];
$password=$data['Password'];
$response->getBody()->write('$username your password is $password');

});

//Delete

$app->delete('/testdelete' ,function($Request ,$Response){

$data=$Request->getParsedBody();
$username=$data['UserName'];
$password=$data['Password'];
$Response->getBody()->write('$username your password is $password with  Delete tast demo');

});
