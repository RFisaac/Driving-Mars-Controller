class RoverConfig:
    CONFIGURATIONS = {
        'orange': {
            'color': (255, 165, 0),
            'commands': {
                'a': 'forward',
                'b': 'backward',
                'c': 'right',
                'd': 'left',
                'e': 'stop',
                '0': 'on'
            }
        },
        'green': {
            'color': (0, 255, 0),
            'commands': {
                'p': 'forward',
                'q': 'backward',
                'r': 'right',
                's': 'left',
                't': 'stop',
                '3': 'on'
            }
        },
        'blue': {
            'color': (0, 0, 255),
            'commands': {
                'k': 'forward',
                'l': 'backward',
                'm': 'right',
                'n': 'left',
                'o': 'stop',
                '2': 'on'
            }
        },
        'red': {
            'color': (255, 0, 0),
            'commands': {
                'j': 'forward',
                'f': 'backward',
                'g': 'right',
                'h': 'left',
                'i': 'stop',
                '1': 'on'
            }
        }
    }
    
    def __init__(self):
        self.colors = list(self.CONFIGURATIONS.keys())
        self.current_color_index = self._load_saved_color()
        
    def _load_saved_color(self):
        """Load saved color index from file."""
        try:
            with open('rover_color.txt', 'r') as f:
                saved_index = int(f.read().strip())
                # Validate the loaded index
                if 0 <= saved_index < len(self.colors):
                    return saved_index
        except:
            pass
        return 0  # Default to first color if file doesn't exist or is invalid
        
    def _save_color(self):
        """Save current color index to file."""
        try:
            with open('rover_color.txt', 'w') as f:
                f.write(str(self.current_color_index))
        except:
            pass  # Fail silently if we can't write the file
        
    @property
    def current_config(self):
        return self.CONFIGURATIONS[self.colors[self.current_color_index]]
    
    @property
    def current_color(self):
        return self.current_config['color']
    
    @property
    def current_commands(self):
        return self.current_config['commands']
    
    def next_color(self):
        """Switch to next color configuration."""
        self.current_color_index = (self.current_color_index + 1) % len(self.colors)
        self._save_color()  # Save the new color index
        return self.colors[self.current_color_index]

    def get_command_type(self, char):
        """Convert received character to command type."""
        return self.current_commands.get(char)