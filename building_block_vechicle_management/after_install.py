from building_block_vechicle_management.utils.vehicle.vehicle import vehicle_customization
from building_block_vechicle_management.utils.vehicle_log.vehicle_log import vehicle_log_customization

def after_install():
    vehicle_customization()
    vehicle_log_customization()