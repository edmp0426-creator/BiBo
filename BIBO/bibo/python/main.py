from arduino.app_utils import App
from arduino.app_bricks.video_objectdetection import VideoObjectDetection

# Inicializamos el Brick. 
# confidence=0.6 significa que ignorará todo lo que tenga menos de 60% de seguridad
detection_stream = VideoObjectDetection(confidence=0.6, debounce_sec=0.0)

# Esta función se ejecuta cada vez que la cámara detecta algo
def procesar_detecciones(detections: dict):
    for clase, objetos in detections.items():
        for objeto in objetos:
            # Extraemos el nombre de la clase (hoja sana, necrosis, plaga, etc.)
            nombre = clase
            # Extraemos la confianza (ej. 85%)
            seguridad = round(objeto.get('confidence', 0) * 100)
            
            print(f"¡Atención! Detectado: {nombre} con un {seguridad}% de seguridad.")
            
            # ¡Aquí está la magia! Si detecta una enfermedad, puedes hacer algo
            if nombre == "necrosis" or nombre == "plaga":
                print(">> ALERTA ENVIADA AL INVERNADERO <<")
                # Aquí enviarías un comando a la matriz LED del UNO Q 
                # o a un relé para activar una alarma/pesticida.

# Conectamos la función al flujo de video
detection_stream.on_detect_all(procesar_detecciones)

# Arrancamos la aplicación
App.run()