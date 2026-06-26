<?php


$app->get('/password[/{id}]' ,function($requ ,$resp ,$args){
$id=$args['id'];
if (is_null(id)){
$requ->getBody()->write('Ths id is null');
}
else{
$resp->getBody()->write('THS $id=id');
}
   
}); 

$app->get('/password[/{year}[/{month}]]' ,function($requ ,$resp ,$args){
    
$year=$args['year'];
$month=$args['month'];


if (is_null(year)){
$requ->getBody()->write('Ths year and month are is null');

}
else{
if(is_null($month)){
    
$requ->getBody()->write('Ths year=$year month are is null');
}
else{
$requ->getBody()->write('Ths year=$year month=$month');
}}

});
$app->get('/unlimited/optional[/{parms:.*}]',function($req ,$res ,$args){
$parms=explode('/', $req->getAttribute('parms'));
  
if (empty($parms[0])){
$res->getBody()->write("The parms list is null");
}
else{
$out="";
foreach ($parms as $key => $value) {
$out=$out." " ."$key => $value";
}
$res->getBody()->write($out);	
}
});
