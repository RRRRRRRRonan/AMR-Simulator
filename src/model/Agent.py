from enum import Enum

class State(Enum):
    """
    state = static, running.
    ## state, FSM finite state machine.
    - idle / init
    - run after accept
    - pausing, cross section.
    - idle / accomplished
    """
    Idle = 0
    OnDuty = 1
    Pausing = 2
    

class Agent:
    """
    parameters, specifications,
    talk to center control

    mins_to_charged_full
    mins_alive
    mins_working
    mins_time_to_die

    acceloration_rate
    deceloration_rate
    goForward
    turnClockwise
    turnCounterClockwise
    multithread
    """

    def __init__(self, _type, seq_num):
        self.type = _type
        self.id = _type + str(seq_num)
        self.state = State.Idle
        self.odometer = 0
        self.idle_time_so_far = 0
        self.busy_time_so_far = 0
        self.init_location()
        self.moving_speed = 0.5 # m/s
        self.rising_arm_speed = 0.1 # m/s
        self.dropping_arm_speed = 0.1 # m/s
        self.turning_time = 1 # s

        self.fetching_time = 1 # s
        self.dispatching_time = 1 # s


    def init_location(self, location = None):
        if not location:
            location = (0,0)
        self.location = location


    def set_location(self, location):
        self.location = location

    def increment_odometer(self):
        self.odometer += 1

    def update_odometer(self, travelled_distance):
        self.odometer += travelled_distance

    def idle_time_accumulated(self):
        self.idle_time_so_far += 1

    def update_busy_time_accumulated(self, time_duration):
        self.busy_time_so_far += time_duration 

    def update_state(self, state_str):
        if "Idle" in state_str:
            self.state = State.Idle
        elif "OnDuty" in state_str:
            self.state = State.OnDuty
        elif "Pausing" in state_str:
            self.state = State.Pausing


