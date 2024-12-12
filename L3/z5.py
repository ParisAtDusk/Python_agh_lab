class State:
    def __init__(self, name, transitions, output):
        """
        Initialize a state.

        :param name: The name of the state (e.g., 'A').
        :param transitions: A dictionary mapping inputs to next states.
        :param output: The output value of the state (Moore) or for a given transition (Mealy).
        """
        self.name = name
        self.transitions = transitions  # {input: next_state}
        self.output = output            # Static (Moore) or dynamic (Mealy, dependent on input)

    def get_name(self):
        return self.name

    def get_output(self, input_value=None):
        """Get output; for Mealy, it depends on the input."""
        if isinstance(self.output, dict):
            return self.output.get(input_value, None)  # Mealy: input-dependent output
        return self.output  # Moore: static output

    def next_state(self, input_value):
        """Determine the next state based on input."""
        return self.transitions.get(input_value, None)


class StateMachine:
    def __init__(self, states, initial_state):
        """
        Initialize the FSM.

        :param states: A dictionary of state name to State object.
        :param initial_state: The initial state name.
        """
        self.states = states
        self.current_state = self.states[initial_state]

    def get_current_state(self):
        return self.current_state

    def process_input(self, input_value):
        """
        Process an input and transition to the next state.

        :param input_value: Input value to process.
        """
        print(f"Current State: {self.current_state.get_name()}")
        print(f"Input: {input_value}")

        # Fetch output (Moore: static, Mealy: based on input)
        output = self.current_state.get_output(input_value)
        print(f"Output: {output}")

        # Transition to the next state
        next_state_name = self.current_state.next_state(input_value)
        if next_state_name:
            self.current_state = self.states[next_state_name]
        else:
            print("No valid transition for this input.")


# Mealy Machine
# Dictionary in outputs defines it as Mealy Machine; otherwise as Moore
state_A = State("A", transitions={0: "B", 1: "C"}, output={0: 10, 1: 20})  # Mealy output
state_B = State("B", transitions={0: "A", 1: "C"}, output={0: 30, 1: 40})
state_C = State("C", transitions={0: "C", 1: "A"}, output={0: 50, 1: 60})

# Create State Machine instance
states = {"A": state_A, "B": state_B, "C": state_C}
fsm = StateMachine(states, initial_state="A")

# Process input sequence
inputs = [0, 1, 1, 0, 1]
for inp in inputs:
    fsm.process_input(inp)
    print("---")



# Moore Machine
state_A = State("A", transitions={0: "B", 1: "C"}, output=10)  # Static output for Moore
state_B = State("B", transitions={0: "A", 1: "C"}, output=20)
state_C = State("C", transitions={0: "C", 1: "A"}, output=30)

states = {"A": state_A, "B": state_B, "C": state_C}
fsm = StateMachine(states, initial_state="A")

inputs = [0, 1, 1, 0, 1]
print("Starting FSM (Moore Machine):")
for inp in inputs:
    print(f"State Output: {fsm.get_current_state().get_output()}")
    fsm.process_input(inp)
    print("---")

