# TODO Make meaning into a class or object
# lambda args: sum([int(arg) for arg in args])
meaning = {
    'add': {
        'type': 'instruct',
        'action': '+'
    },
    'sub': {
        'type': 'instruct',
        'action': '-'
    },
    'print': {
        'type': 'syn',
        'action': 'print'
    },
    ':': {
        'type': 'op',
        'action': 'perform'
    },
    ',': {
        'type': 'op',
        'action': 'perform'
    },
    ';': {
        'type': 'syn',
        'action': 'end'
    }
}
