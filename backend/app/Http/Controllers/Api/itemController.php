<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;
use App\Models\Item;    

class itemController extends Controller
{
    //Se obtiene la lista de items en caso de que la lista sea vacia, se retorna un mensaje de error
    public function index(){
        $items = Item::all();
        if($items->isEmpty()){
            $resp  = [
                'message' => 'No se encontraron items',
                'status' => 'error',
                'code' => 200,
            ];
            return response()->json($resp, 200);
        }
        $resp = [
            'message' => 'Items obtenidos correctamente',
            'status' => 'success',
            'code' => 200,
            'data' => $items,
        ];
        return response()->json($resp, 200);
    }
    //Se obtiene un item mediante el id en caso de que el item no exista, se retorna un mensaje de error
    public function show($id){
        $item = Item::find($id);
        if(!$item){
            $resp = [
                'message' => 'No se encontró el item',
                'status' => 'error',
                'code' => 404,
            ];
            return response()->json($resp, 404);
        }   
        $resp = [
            'message' => 'Item obtenido correctamente',
            'status' => 'success',
            'code' => 200,
            'data' => $item,
        ];
        return response()->json($resp, 200);
    }
    
    //Se crea un nuevo item en caso de que los datos de entrada sean validos y no haya ningun error se retorna un mensaje de exito
    public function store(Request $request){
        $validator = Validator::make($request->all(), [
            'nombre' => 'required|string',
            'descripcion' => 'nullable|string',
            'estado' => 'required|in:activo,inactivo',
        ]);
        if($validator->fails()){
            $resp = [
                'message' => 'Error en la validacion de los datos',
                'status' => 'error',
                'code' => 400,
                'errors' => $validator->errors(),
            ];
            return response()->json($resp, 400);
        }
            $item = Item::create($validator->validated());
            $resp = [
            'message' => 'Item creado correctamente',
            'status' => 'success',
            'code' => 201,
            'data' => $item,
        ];
        return response()->json($resp, 201);        
    }
    //Se actualiza un item mediante el id en caso de que los datos de entrada sean validos y no haya ningun error se retorna un mensaje de exito    
    public function update(Request $request, $id){  
        $validator = Validator::make($request->all(), [
            'nombre' => 'required|string',
            'descripcion' => 'nullable|string',
            'estado' => 'required|in:activo,inactivo',
        ]);
        if($validator->fails()){
            $resp = [
                'message' => 'Error en la validacion de los datos',
                'status' => 'error',
                'code' => 400,
                'errors' => $validator->errors(),
            ];
            return response()->json($resp, 400);
        }
        $item = Item::find($id);
        if(!$item){
            $resp = [
                'message' => 'No se encontro el item',
                'status' => 'error',
                'code' => 404,
            ];
            return response()->json($resp, 404);
        }
        $item->update($validator->validated());
        $resp = [
            'message' => 'Item actualizado correctamente',
            'status' => 'success',
            'code' => 200,
            'data' => $item,
        ];
        return response()->json($resp, 200);
    }
    //Se elimina un item mediante el id en caso de que el item no exista, se retorna un mensaje de error
    public function destroy($id){
        $item = Item::find($id);
        if(!$item){
            $resp = [
                'message' => 'No se encontro el item',
                'status' => 'error',
                'code' => 404,
            ];
            return response()->json($resp, 404);
        }
        $item->delete();
        $resp = [
            'message' => 'Item eliminado correctamente',
            'status' => 'success',
            'code' => 200,
        ];
        return response()->json($resp, 200);
    }
}
