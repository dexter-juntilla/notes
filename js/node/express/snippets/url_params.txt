var http =require('http');
var express = require('express');
var app = express();

app.get('/products/:category(\\d+)',function(req, res, next){
	res.end(req.param(category));
});

http.createServer(app).listen(8000);