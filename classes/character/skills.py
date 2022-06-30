class Skills():
    def __init__(
        self,
        # Fighting Skills
        _brawling,
        _evasion,
        _marksmanship,
        _melee_weapon,
        # Awareness Skills
        _concentration,
        _perception,
        _tracking,
        # Control Skills
        _driving,
        # Body Skills
        _athletics,
        _stealth,
        # Technique Skills
        _basic_tech,
        _cybertech,
        _first_aid,
        # Performance_skills
        _play_instrument,
        # Education Skills
        _education,
        _local_expert,
        # social skills
        _bribery,
        _conversation,
        _human_perception,
        _interrogation,
        _persuasion,
        # Role Abilities
    ) -> None:

        self._brawling = _brawling
        self._evasion = _evasion
        self._marksmanship = _marksmanship
        self._melee_weapon = _melee_weapon
        self._concentration = _concentration
        self._perception = _perception
        self._tracking = _tracking
        self._driving = _driving
        self._athletics = _athletics
        self._stealth = _stealth
        self._basic_tech = _basic_tech
        self._cybertech = _cybertech
        self._first_aid = _first_aid
        self._play_instrument = _play_instrument
        self._education = _education
        self._local_expert = _local_expert
        self._bribery = _bribery
        self._conversation = _conversation
        self._human_perception = _human_perception
        self._interrogation = _interrogation
        self._persuasion = _persuasion

    # getter methods

    def get_brawling(self):
        return self._brawling

    def get_evasion(self):
        return self._evasion

    def get_marksmanship(self):
        return self._marksmanship

    def get_melee_weapon(self):
        return self._melee_weapon

    def get_concentration(self):
        return self._concentration

    def get_perception(self):
        return self._perception

    def get_tracking(self):
        return self._tracking

    def get_driving(self):
        return self._driving

    def get_athletics(self):
        return self._athletics

    def get_stealth(self):
        return self._stealth

    def get_basic_tech(self):
        return self._basic_tech

    def get_cybertech(self):
        return self._cybertech

    def get_first_aid(self):
        return self._first_aid

    def get_play_instrument(self):
        return self._play_instrument

    def get_education(self):
        return self._education

    def get_local_expert(self):
        return self._local_expert

    def get_bribery(self):
        return self._bribery

    def get_conversation(self):
        return self._conversation

    def get_human_perception(self):
        return self._human_perception

    def get_interrogation(self):
        return self._interrogation

    def get_persuasion(self):
        return self._persuasion

    # setter metods

    def set_brawling(self, new_brawling):
        self._brawling = new_brawling
        return self._brawling

    def set_evasion(self, new_evasion):
        self._evasion = new_evasion
        return self._evasion

    def set_marksmanship(self, new_marksmanship):
        self._marksmanship = new_marksmanship
        return self._marksmanship

    def set_melee_weapon(self, new_melee_weapon):
        self._melee_weapon = new_melee_weapon
        return self._melee_weapon

    def set_concentration(self, new_concentration):
        self._concentration = new_concentration
        return self._concentration

    def set_perception(self, new_perception):
        self._perception = new_perception
        return self._perception

    def set_tracking(self, new_tracking):
        self._tracking = new_tracking
        return self._tracking

    def set_driving(self, new_driving):
        self._driving = new_driving
        return self._driving

    def set_athletics(self, new_athletics):
        self._athletics = new_athletics
        return self._athletics

    def set_stealth(self, new_stealth):
        self._stealth = new_stealth
        return self._stealth

    def set_basic_tech(self, new_basic_tech):
        self._basic_tech = new_basic_tech
        return self._basic_tech

    def set_cybertech(self, new_cybertech):
        self._cybertech = new_cybertech
        return self._cybertech

    def set_first_aid(self, new_first_aid):
        self._first_aid = new_first_aid
        return self._first_aid

    def set_play_instrument(self, new_play_instrument):
        self._play_instrument = new_play_instrument
        return self._play_instrument

    def set_education(self, new_education):
        self._education = new_education
        return self._education

    def set_local_expert(self, new_local_expert):
        self._local_expert = new_local_expert
        return self._local_expert

    def set_bribery(self, new_bribery):
        self._bribery = new_bribery
        return self._bribery

    def set_conversation(self, new_conversation):
        self._conversation = new_conversation
        return self._conversation

    def set_human_perception(self, new_human_perception):
        self._human_perception = new_human_perception
        return self._human_perception

    def set_interrogation(self, new_interrogation):
        self._interrogation = new_interrogation
        return self._interrogation

    def set_persuasion(self, new_persuasion):
        self._persuasion = new_persuasion
        return self._persuasion
