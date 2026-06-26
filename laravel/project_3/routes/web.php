<?php

use Illuminate\Support\Facades\Route;
use Illuminate\Http\Request;

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

Auth::routes();

Route::get('/home', [App\Http\Controllers\HomeController::class, 'index'])->name('home');

//profile
 Route::get('profile', [App\Http\Controllers\ProfileController::class, 'index'])->name('profile');
 Route::put('profile/update', [App\Http\Controllers\ProfileController::class, 'update'])->name('profile.update');

//post
// Route::get('posts', [App\Http\Controllers\PostController::class, 'index'])->name('posts');
// Route::get('posts/trashed', [App\Http\Controllers\PostController::class, 'postsTrashed'])->name('posts.trashed');
// Route::get('posts/create', [App\Http\Controllers\PostController::class, 'create'])->name('post.create');
// Route::post('posts/store', [App\Http\Controllers\PostController::class, 'store'])->name('post.store');
// Route::get('posts/show/{slug}', [App\Http\Controllers\PostController::class, 'show'])->name('post.show');
// Route::put('posts/edit/{id}', [App\Http\Controllers\PostController::class, 'edit'])->name('post.edit');
// Route::get('posts/update/{id}', [App\Http\Controllers\PostController::class, 'update'])->name('post.update');
// Route::get('posts/destroy/{id}', [App\Http\Controllers\PostController::class, 'destroy'])->name('post.destroy');
// Route::get('posts/hdelete/{id}', [App\Http\Controllers\PostController::class, 'hdelete'])->name('post.hdelete');
// Route::get('posts/restore/{id}', [App\Http\Controllers\PostController::class, 'restore'])->name('post.restore');
