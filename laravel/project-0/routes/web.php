<?php

use App\Http\Controllers\AppController;
use Illuminate\Support\Facades\Route;

use App\Http\Controllers\IndexController;

use App\Http\Controllers\UsersController;


/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

// Route::get('home', function(){
//     return 'home Abdallah';
// });


// Route::view('index1', 'index');

Route::get('/IndexController', [IndexController::class ,'index']);

//Route::get('/app{id}', [IndexController::class ,'show']);

Route::get('/appsum{idsum}', [IndexController::class ,'sum']);


Route::get('/users', [UsersController::class ,'users']);
Route::get('/users/{id}', [UsersController::class ,'users_id']);

