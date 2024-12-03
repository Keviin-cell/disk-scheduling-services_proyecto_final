def scan(arm_position, lrequests, tracks, debug=False):
    """
    SCAN Disk Scheduling Algorithm

    Args:
        arm_position (int): Position of the arm.
        lrequests (list<int>): List of requests (cylinders).
        tracks (int): Number of tracks on the disk.
    """
    distance = 0
    n = len(lrequests)
    left = [x for x in lrequests if x < arm_position]  # Solicitudes a la izquierda del brazo
    right = [x for x in lrequests if x >= arm_position]  # Solicitudes a la derecha del brazo

    left.sort()   # Ordena las solicitudes a la izquierda
    right.sort()  # Ordena las solicitudes a la derecha

    # Mover hacia la izquierda primero
    distance += arm_position - left[0] if left else 0
    current_pos = left[0] if left else arm_position
    for req in reversed(left):
        distance += abs(req - current_pos)
        current_pos = req
        #if debug:
            #print("> Moving to", current_pos)

    # Luego mover hacia la derecha
    distance += right[-1] - current_pos if right else 0
    current_pos = right[-1] if right else arm_position
    for req in right:
        distance += abs(req - current_pos)
        current_pos = req
        #if debug:
            #print("> Moving to", current_pos)

    average = distance / n if n > 0 else 0
    return {
        "sequence": [arm_position] + left + right,
        "average": average,
        "distance": distance,
    }
