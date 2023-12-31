from models.trip import Trip

def documentToTrip(dbTrip: Trip):
    return {
        '_id': str(dbTrip['_id']),
        'limit': dbTrip['limit'],
        'user_id': str(dbTrip['user_id']),
        'trip_type': dbTrip['trip_type'],
        'destination': dbTrip['destination'],
        'meet_up_spot': dbTrip['meet_up_spot'],
        'rt_meet_up_spot': dbTrip['rt_meet_up_spot'],
        'departure_time': str(dbTrip['departure_time']),
        'rt_departure_time': None if not dbTrip['rt_departure_time'] else str(dbTrip['rt_departure_time']),
        'travel_buddies':  [str(buddy) for buddy in dbTrip['travel_buddies']] if dbTrip['travel_buddies'] else [],
        'estimated_cost_of_trip': dbTrip['estimated_cost_of_trip'],
        'active': dbTrip['active'],
        'created_at': None if 'created_at' not in dbTrip.keys() else  str(dbTrip['created_at']),
        'updated_at':  None if 'created_at' not in dbTrip.keys() else  str(dbTrip['created_at']),
    }