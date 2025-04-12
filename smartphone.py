class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours
        self.is_on = False
        
    def power_on(self):
        if not self.is_on:
            self.is_on = True
            return f"{self.brand} {self.model} is now powered on!"
        return "Phone is already on."
    
    def install_app(self, app_name, size):
        if size > self.storage:
            return "Not enough storage!"
        self.storage -= size
        return f"{app_name} installed successfully!"
    
    def check_storage(self):
        return f"Remaining storage: {self.storage}GB"

class FlagshipPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, camera_mp):
        super().__init__(brand, model, storage, battery_life)
        self.camera_mp = camera_mp
        self.facial_recognition = True
        
    def take_photo(self):
        return f"Taking a high-quality {self.camera_mp}MP photo!"
    
    def power_on(self):  # Overriding the parent method
        if not self.is_on:
            self.is_on = True
            return f"Flagship {self.brand} {self.model} boots up with fancy animation!"
        return "Phone is already on."