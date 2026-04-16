EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(time_taken):
    """Calculate remaining bake time."""
    return EXPECTED_BAKE_TIME - time_taken


def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time based on number of layers."""
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed cooking time."""
    return (PREPARATION_TIME * number_of_layers) + elapsed_bake_time