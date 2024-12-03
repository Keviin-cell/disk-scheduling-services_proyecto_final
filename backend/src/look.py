def look(arm_position, lrequests):
    """
    LOOK Disk Scheduling Algorithm

    Args:
        arm_position (int): arm position
        lrequests (list<int>): request list
    """
    # Ordenar las solicitudes de menor a mayor
    lrequests.sort()
    
    # Dividir las solicitudes en dos partes: las que están a la izquierda y las que están a la derecha
    left = [r for r in lrequests if r < arm_position]
    right = [r for r in lrequests if r > arm_position]
    
    # Si hay solicitudes a la derecha, mover a la derecha primero
    total_distance = 0
    sequence = [arm_position]
    current_pos = arm_position
    
    if right:
        # Mover hacia la derecha
        for r in right:
            total_distance += abs(r - current_pos)
            current_pos = r
            sequence.append(current_pos)
    
    # Luego, si hay solicitudes a la izquierda, mover hacia la izquierda
    if left:
        left.reverse()  # Invertir para mover de vuelta
        for r in left:
            total_distance += abs(r - current_pos)
            current_pos = r
            sequence.append(current_pos)
    
    average = total_distance / len(lrequests)
    
    return {
        "sequence": sequence,
        "average": average,
        "distance": total_distance,
    }
