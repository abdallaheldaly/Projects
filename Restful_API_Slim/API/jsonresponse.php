<?php
use Psr\Http\Message\ResponseInterface as Response;
use Psr\Http\Message\ServerRequestInterface as Request;
use Slim\Factory\AppFactory;

$app->get('/jsontast/{FerstName}/{LastName}' ,function($Request ,$Response ,$args){
    $FerstName = $args['FerstName'];
    $LastName  = $args['LastName'];
    $out =[];
$out['Status'] = 200;
$out['Message'] = 'This is JSON Response Test';
$out['FerstName'] = $FerstName;
$out['LastName'] = $LastName;
$Response->getBody()->write(json_encode($out));
});
