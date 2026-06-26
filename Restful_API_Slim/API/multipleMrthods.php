<?php
use Psr\Http\Message\ResponseInterface as Response;
use Psr\Http\Message\ServerRequestInterface as Request;
use Slim\Factory\AppFactory;

$app->map(['PUT' ,'GET'],'/multipleMrthodsTest/{id}',function($Request ,$Response){

$id=$args['id'];
if ($Request->isPut()){
    $Response->getBody()->write('This di=$di will be updated');
}

if ($Request->isGet()){
    $Response->getBody()->write('This di=$di will be retrived');
}
});