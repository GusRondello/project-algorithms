def study_schedule(permanence_period, target_time):
    p = len(permanence_period)
    count = 0
    if target_time == 0 or target_time is None:
        return None

    for index in range(0, p):
        login = permanence_period[index][0]
        logout = permanence_period[index][1]
        if not type(login) == int or not type(logout) == int:
            return None
        elif login <= target_time <= logout:
            count += 1
    return count
