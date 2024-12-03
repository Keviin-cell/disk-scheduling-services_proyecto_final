def cscan(arm_position, lrequests, tracks, debug=False):
    """
    C-SCAN Disk Scheduling Algorithm

    Args:
        arm_position (int): Position of the arm.
        lrequests (list<int>): List of requests (cylinders).
        tracks (int): Number of tracks on the disk.
    """
    distance = 0
    n = len(lrequests)
    left = [x for x in lrequests if x < arm_position]  # Solicitudes a la izquierda
    right = [x for x in lrequests if x >= arm_position]  # Solicitudes a la derecha

    left.sort()   # Ordena las solicitudes a la izquierda
    right.sort()  # Ordena las solicitudes a la derecha

    # Mover hacia la derecha primero
    distance += right[-1] - arm_position if right else 0
    current_pos = right[-1] if right else arm_position
    for req in right:
        distance += abs(req - current_pos)
        current_pos = req
        if debug:
            print("> Moving to", current_pos)

    # Después salta al principio y mueve hacia la izquierda
    distance += (tracks - 1) - current_pos if right else 0
    current_pos = 0 if right else arm_position
    for req in reversed(left):
        distance += abs(req - current_pos)
        current_pos = req
        if debug:
            print("> Moving to", current_pos)

    average = distance / n if n > 0 else 0
    return {
        "sequence": [arm_position] + right + left,
        "average": average,
        "distance": distance,
    }
