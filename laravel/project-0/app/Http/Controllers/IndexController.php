<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class IndexController extends Controller
{
    public function index(){
        return view("index");
    }

    public function show($id){
        return "my id is " . $id;
    }

    public function sum($idsum){
        return 10 + $idsum;
    }
}
