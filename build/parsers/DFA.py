class DFA_STATE:
    def __init__(self,state,transitions_dict,accepting):
        self.state = state        
        self.transitions = transitions_dict
        self.accepting = accepting #Whether the state is an accepting state
    def transition(self,alpha):
        return self.transitions[alpha]
class DFA:
    def __init__(self):
        self.states = {}
        self.current_state = -1
    def add_state(self,state_val,transitions,accepting):        
        self.states[state_val] = (DFA_STATE(state_val,transitions,accepting))
        if(self.current_state==-1):
            #If DFA not initialized
            self.current_state = state_val
    def next(self,alpha):
        if(self.current_state==-1):
            raise Exception("DFA not initialized")
        else:
            self.current_state = self.states[self.current_state].transition(alpha)
