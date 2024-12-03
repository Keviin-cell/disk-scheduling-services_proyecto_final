def clook(arm_position, lrequests):
    """
    CLOOK Disk Scheduling Algorithm

    Args:
        arm_position (int): arm position
        lrequests (list<int>): request list
    """
    # Ordenar las solicitudes de menor a mayor
    lrequests.sort()
    
    # Dividir las solicitudes en dos partes: las que están a la izquierda y las que están a la derecha
    left = [r for r in lrequests if r < arm_position]
    right = [r for r in lrequests if r > arm_position]
    
    total_distance = 0
    sequence = [arm_position]
    current_pos = arm_position

    # Primero, mover hacia la derecha si hay solicitudes a la derecha
    if right:
        for r in right:
            total_distance += abs(r - current_pos)
            current_pos = r
            sequence.append(current_pos)
    
    # Después, regresar al inicio y mover hacia la izquierda si hay solicitudes a la izquierda
    if left:
        # Regresar al primer cilindro y mover hacia la izquierda
        total_distance += abs(current_pos - right[0])  # Regresar al primer cilindro a la derecha
        current_pos = right[0]
        for r in reversed(left):  # Recorrer las solicitudes a la izquierda en orden inverso
            total_distance += abs(r - current_pos)
            current_pos = r
            sequence.append(current_pos)

    average = total_distance / len(lrequests)
    
    return {
        "sequence": sequence,
        "average": average,
        "distance": total_distance,
    }
