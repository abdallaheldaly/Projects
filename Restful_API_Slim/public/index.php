<?php
use Psr\Http\Message\ResponseInterface as Response;
use Psr\Http\Message\ServerRequestInterface as Request;
use Slim\Factory\AppFactory;

require __DIR__ . '/../vendor/autoload.php';

$app = AppFactory::create();

require __DIR__ . '/../API/args.php';
require __DIR__ . '/../API/jsonresponse.php';
require __DIR__ . '/../API/multipleMrthods.php';
require __DIR__ . '/../API/optional.php';
require __DIR__ . '/../API/others.php';
require __DIR__ . '/../API/pust.php';
require __DIR__ . '/../API/put&delete.php';


$app->run();