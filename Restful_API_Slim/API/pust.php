<?php
use Psr\Http\Message\ResponseInterface as Response;
use Psr\Http\Message\ServerRequestInterface as Request;
use Slim\Factory\AppFactory;

$app->get('/hello/{name}', function (Request $Request, Response $Response, array $args) {
    $name = $args['name'];
    $Response->getBody()->write("Hello, $name");
    return $Response;
});

$app->get('/id/{id}', function (Request $Request, Response $Response, array $args) {
    $id = $args['id'];
    $Response->getBody()->write("Hello, $id");
    return $Response;
});

$app->post('/tast/{name}', function (Request $a1, Request $a2){
$data=$a1->getParsedBody();
$inputdata=[];
$inputdata['name']=filter_var($data['name'], FILTER_SANITIZE_STRING);
$inputdata['id']=filter_var($data['id'], FILTER_SANITIZE_STRING);
$a2->getBody()->write('daer ' .$inputdata['name'].'your phone unmber is ' .$inputdata['phone']);

});