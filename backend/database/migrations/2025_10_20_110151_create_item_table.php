<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {   //Se crea la tabla item, con sus respectivos campos, tipo de  datos y restricciones
        Schema::create('item', function (Blueprint $table) {
            $table->id(); 
            $table->string('nombre');
            $table->text('descripcion')->nullable(); 
            $table->enum('estado', ['activo', 'inactivo'])->default('activo'); 
            $table->timestamp('fecha_creacion')->useCurrent(); 
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('item');
    }
};
