@yield('content')
	@section('content')
	@stop

return view('pages.index', ['data'=>$arr, 'name'=>'dexter']); //from controller
	{{ print_r($data) }}
	{{ $name }}

{{ $data }} // will escape html

{!! $html !!} // will render html

@foreach ($arr as $val)
	{{ $val }}
@endforeach

@if ()
@endif

@unless ()
@endunless