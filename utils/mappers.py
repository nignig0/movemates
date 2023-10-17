from models.trip import Trip

def documentToTrip(dbTrip: Trip):
    return {
        '_id': str(dbTrip['_id']),
        'user_id': str(dbTrip['user_id']),
        'trip_type': dbTrip['trip_type'],
        'destination': dbTrip['destination'],
        'meet_up_spot': dbTrip['meet_up_spot'],
        'rt_meet_up_spot': dbTrip['rt_meet_up_spot'],
        'departure_time': str(dbTrip['departure_time']),
        'rt_departure_time': str(dbTrip['rt_departure_time']),
        'travel_buddies': dbTrip['travel_buddies'],
        'estimated_cost_of_trip': dbTrip['estimated_cost_of_trip'],
        'active': dbTrip['active']

    }