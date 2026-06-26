<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Profile; //Models
use Auth;
use Illuminate\Support\Facades\Hash;

class ProfileController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $user = Auth::user();
        $id = Auth::id();
        if ($user->profile == null) {
           $profile = Profile::create([
            'user_id'=> $id,
            'city'   => 'giza',
            'gender' => '',
            'cv'	 => '',
            'linkedin' => 'https://www.linkedin.com',
           ]);
        }
        return view('users.profile')->with('user',$user);
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, s$id)
    {
        $this->validate($request,[
            'name'  => 'required',
            'city'  => 'required',
            'gender'=> 'required',
            'cv'	=> 'required',
        ]);



        $user = Auth::user();
        $user->name = $request->name ;
        $user->profile->city = $request->city ;
        $user->profile->gender = $request->gender ;
        $user->profile->cv = $request->cv ;
        $user->save();
        $user->profile->save();

        if ($request->has('password')) {
            $user->password = Hash::make($request->password);
            $user->save();
        }

     return redirect()->back();

    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        //
    }
}
