# ChatBot con LLM Local

**Trabajo Práctico Final - Linux | UNSAM 2025**

## Descripción

Este proyecto implementa un chatbot con inteligencia artificial que funciona completamente local, sin necesidad de conexión a internet ni servicios externos como ChatGPT. Toda la inferencia del modelo se ejecuta en tu propia máquina aprovechando la GPU NVIDIA mediante CUDA.

La arquitectura está basada en Docker Compose con dos servicios principales: un servidor Flask que expone la interfaz web y la API REST, y llama-swap que gestiona la carga/descarga automática de modelos LLM utilizando llama.cpp como motor de inferencia optimizado para GPU.

## Arquitectura

El flujo de comunicación es simple: el usuario interactúa con una interfaz web servida por Flask en el puerto 5000, que envía las consultas a llama-swap (puerto 8090), el cual a su vez ejecuta llama.cpp con el modelo Qwen2.5-Coder 32B cargado en GPU. llama-swap implementa un sistema inteligente de gestión de recursos que descarga el modelo de la memoria GPU después de 5 minutos de inactividad.

```
Usuario -> Flask :5000 -> llama-swap :8090 -> llama.cpp (GPU)
```

## Uso

```bash
# Levantar
docker-compose up -d

# Ver logs
docker-compose logs -f

# Acceder
http://localhost:5000

# Detener
docker-compose down
```
