@extends('layouts.app')
@section('content')

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>profile</title>
</head>

<body>
  <div class='container'style="padding-top: 3%">
    <form action="{{route('profile.update')}}" method="POST">
    @csrf
    @method('PUT')
      <div>
          <div class="mb-3">
            <label for="exampleFormControlInput1" class="form-label">Name</label>
            <input type="text" name="name" class="form-control" id="exampleFormControlInput1" value="{{$user->name}}">
          </div>

          <div class="mb-3">
            <label for="exampleFormControlInput1" class="form-label">city</label>
            <input type="text" name="city" class="form-control" id="exampleFormControlInput1" value="{{$user->city}}">
          </div>

          <select class="form-select" aria-label="Gender">
            <option value="1">Male</option>
            <option value="2">Female</option>
          </select> 

          <div>
            <div class="mb-3">
              <label for="exampleFormControlTextarea1" class="form-label">CV</label>
              <textarea class="form-control" id="exampleFormControlTextarea1" rows="3">
              {{$user->cv}}
              </textarea>
          </div>

          <div class="mb-3">
            <label for="exampleFormControlInput1" class="form-label">Email address in linkedin</label>
            <input type="text" name="linkedin" class="form-control" id="exampleFormControlInput1" value="{{$user->linkedin}}">
          </div>

          <div class="mb-3">
            <label for="exampleFormControlInput1" class="form-label">Password</label>
            <input type="password" name="password" class="form-control" id="exampleFormControlInput1" value="{{$user->name}}">
          </div>

          <div class="mb-3">
            <label for="exampleFormControlInput1" class="form-label">Confirm Password</label>
            <input type="password" name="confirm_password" class="form-control" id="exampleFormControlInput1" value="{{$user->name}}">
          </div>

          <div class="form-group">
            <button type="submit" class="btn btn-success">update</button>
          </div>

        </div>
      </div>
    </form>
  </div>
</body>
</html>

@endsection 