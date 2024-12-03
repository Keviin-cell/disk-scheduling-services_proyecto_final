def sstf(arm_position, lrequests, debug=False):
    """
    Shortest Seek Time First (SSTF) implementation

    Args:
        arm_position (int): Initial position of the arm
        lrequests (list<int>): List of track requests
        debug (bool): If True, prints detailed steps
    """
    distance = 0  # Distancia total recorrida
    current_pos = arm_position  # Posición actual del brazo
    sequence = [arm_position]  # Secuencia de posiciones del brazo
    requests = lrequests[:]  # Copia de las solicitudes para no modificar la original

    while requests:
        # Encuentra la solicitud más cercana a la posición actual
        closest_request = min(requests, key=lambda x: abs(x - current_pos))
        distance += abs(closest_request - current_pos)  # Incrementa la distancia
        current_pos = closest_request  # Actualiza la posición actual
        sequence.append(current_pos)  # Añade la posición a la secuencia
        requests.remove(closest_request)  # Elimina la solicitud procesada
        if debug: print("> ", current_pos, "seeked")

    average = distance / len(lrequests)  # Calcula el promedio de distancia

    return {
        "sequence": sequence,
        "average": average,
        "distance": distance,
    }

# Ejemplo de uso
# print(sstf(96, [125, 17, 23, 67, 90, 128, 189, 115, 97], debug=True))
