from transitions import Machine

class ProjectState(Machine):
    states = ['live', 'not_live']
    transitions = [
        {'trigger': 'go_live', 'source': 'not_live', 'dest': 'live'},
        {'trigger': 'go_not_live', 'source': 'live', 'dest': 'not_live'}
    ]
    


# if __name__ == '__main__':
#     p = ProjectState()