<?php

$app->get('/regular/{id:[0-9]+}/{name:[a-z]=}',function($Request ,$Response ,$args){
$id=$args['id'];
$name=$args['name'];
$Response->getBody()->write('this id=$id,the name is $name');
});

$app->group('/grouptest', function($Request ,$Response) use($app){
$app->get('' ,function($Request ,$Response){
$Response->getBody()->write('GET EMPTY METHOD');
});

$app->put('' ,function($Request ,$Response){
$Response->getBody()->write('PUT EMPTY METHOD');
});

$app->get('/{id}' ,function($Request ,$Response ,$args){
$id=$args['id'];
$Response->getBody()->write('GET WHIS id=$di');
});

$app->post('/postdata' ,function($Request ,$Response ,$args){
$Response->getBody()->write('post method');
});
});

$app->group('/API' ,function($req ,$res) use($app){

$app->group('/V1' ,function($req ,$res) use($app){

$app->get('/getuser' ,function($req ,$res){
echo'getuser V1';
});

$app->pust('/adduser' ,function($req ,$res){
echo'adduser V1';
});
});
});