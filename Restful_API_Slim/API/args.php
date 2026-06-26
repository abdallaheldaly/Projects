<?php
use Psr\Http\Message\ResponseInterface as Response;
use Psr\Http\Message\ServerRequestInterface as Request;
use Slim\Factory\AppFactory;

$app->get('/testargs/{Name}/{phone}', function ($Request,$Response, array $args) {
    $Name = $args['Name'];
    $phone = $args['phone'];
    $Response->getBody()->write("thes is a test for args, $Name you phone numbor is $phone");
    return $Response;
});