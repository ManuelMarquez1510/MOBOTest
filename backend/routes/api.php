<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Api\itemController;
//Se exponen las rutas para la API RESTful de items
Route::get('/items',[itemController::class, 'index']);
Route::get('/items/{id}',[itemController::class, 'show']);
Route::post('/items',[itemController::class, 'store']);
Route::put('/items/{id}',[itemController::class, 'update']);
Route::delete('/items/{id}',[itemController::class, 'destroy']);